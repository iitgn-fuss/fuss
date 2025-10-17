#!/usr/bin/env python3
"""
Google Scholar Publication Fetcher
Fetches publications from multiple Google Scholar profiles and updates publications.md
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from typing import List, Dict, Set, Tuple
from urllib.parse import urljoin, quote
import sys

# Configuration
GOOGLE_SCHOLAR_PROFILES = [
    "https://scholar.google.com/citations?user=JX0CWckAAAAJ&hl=en&oi=sra",
    # Add more profiles here as needed
]

TEAM_MEMBERS = [
    "Abhishek Bichhawat",
    "A Bichhawat",
    "Gayatri Priyadarsini",
    "Gayatri Priyadarsini Kancherla",
    "GP Kancherla",
    "G Priyadarsini",
    "Subhrajit Das",
    "S Das",
    "Sreyashi Karmakar",
    "S Karmakar",
    "Krupa Rajani",
    "K Rajani",
]

PUBLICATIONS_FILE = "content/publications.md"

# User-Agent to avoid blocking
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def fetch_scholar_profile(profile_url: str, max_papers: int = 100, max_retries: int = 3) -> List[Dict]:
    """Fetch all publications from a Google Scholar profile (handles pagination and retries)."""
    publications = []
    
    # Add parameters to show all papers
    if '?' in profile_url:
        base_url = profile_url + f"&cstart=0&pagesize={max_papers}"
    else:
        base_url = profile_url + f"?cstart=0&pagesize={max_papers}"
    
    for attempt in range(max_retries):
        try:
            print(f"Fetching profile (attempt {attempt + 1}/{max_retries}): {base_url}")
            response = requests.get(base_url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all publication entries
            pub_rows = soup.find_all('tr', class_='gsc_a_tr')
            print(f"Found {len(pub_rows)} publication entries")
            
            if len(pub_rows) == 0 and attempt < max_retries - 1:
                print("No publications found, retrying...")
                time.sleep(3)
                continue
            
            for idx, row in enumerate(pub_rows, 1):
                try:
                    # Extract title and link
                    title_elem = row.find('a', class_='gsc_a_at')
                    if not title_elem:
                        continue
                        
                    title = title_elem.text.strip()
                    pub_link = urljoin("https://scholar.google.com", title_elem.get('href', ''))
                    
                    # Extract authors
                    authors_elem = row.find('div', class_='gs_gray')
                    authors = authors_elem.text.strip() if authors_elem else ""
                    
                    # Extract venue and year
                    venue_elem = authors_elem.find_next_sibling('div', class_='gs_gray') if authors_elem else None
                    venue_year = venue_elem.text.strip() if venue_elem else ""
                    
                    # Extract year from the right column
                    year_elem = row.find('span', class_='gsc_a_h')
                    year = year_elem.text.strip() if year_elem else ""
                    
                    # Try to get more details from the publication page (with retry)
                    pub_details = fetch_publication_details(pub_link, max_retries=3)
                    
                    publication = {
                        'title': title,
                        'authors': authors,
                        'venue': venue_year,  # This is the short venue from main page
                        'year': year,
                        'link': pub_link,
                        'details': pub_details
                    }
                    
                    publications.append(publication)
                    
                    # Show full title if available
                    display_title = pub_details.get('full_title', title)
                    print(f"  [{idx}/{len(pub_rows)}] ✓ {display_title[:70]}... ({year})")
                    
                    # Be respectful with rate limiting
                    time.sleep(1.5)
                    
                except Exception as e:
                    print(f"  ✗ Error parsing publication {idx}: {e}")
                    continue
            
            print(f"✓ Successfully fetched {len(publications)} publications from profile\n")
            break  # Success, exit retry loop
            
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"✗ Error fetching profile (attempt {attempt + 1}): {e}")
                print(f"Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print(f"✗ Failed to fetch profile after {max_retries} attempts: {e}\n")
                import traceback
                traceback.print_exc()
    
    return publications


def fetch_publication_details(pub_url: str, max_retries: int = 3) -> Dict:
    """Fetch additional details from a publication page with retry logic."""
    details = {
        'abstract': '',
        'pdf_link': '',
        'venue_full': '',
        'publication_type': 'Conference',  # Default
        'full_title': ''  # Store complete title with special chars
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(pub_url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract full title with all special characters
            title_elem = soup.find('a', class_='gsc_oci_title_link')
            if not title_elem:
                title_elem = soup.find('div', id='gsc_oci_title')
            if title_elem:
                # Get the text and decode HTML entities properly
                full_title = title_elem.get_text(strip=True)
                # Replace common entity issues
                full_title = full_title.replace('&#8902;', '⋆')  # Star operator
                full_title = full_title.replace('DY⋆', 'DY⋆')  # Ensure DY⋆ is preserved
                details['full_title'] = full_title
            
            # Try to find PDF link - check multiple possible locations
            pdf_link = soup.find('a', class_='gsc_oci_title_ggi')
            if pdf_link and pdf_link.get('href'):
                details['pdf_link'] = pdf_link.get('href')
            else:
                # Try alternative: look for "View PDF" or similar links
                all_links = soup.find_all('a', href=True)
                for link in all_links:
                    href = link.get('href', '')
                    if '.pdf' in href.lower() or 'pdf' in link.text.lower():
                        details['pdf_link'] = href
                        break
            
            # Extract full venue information - try multiple fields
            venue_value = None
            
            # Method 1: Look for "Publication" field
            venue_field = soup.find('div', class_='gsc_oci_field', string='Publication')
            if not venue_field:
                # Try regex match for fields containing "Publication"
                venue_field = soup.find('div', class_='gsc_oci_field', string=re.compile(r'Publication', re.IGNORECASE))
            
            if venue_field:
                venue_value = venue_field.find_next_sibling('div', class_='gsc_oci_value')
            
            # Method 2: Look for "Conference" or "Journal" field
            if not venue_value:
                for field_name in ['Conference', 'Journal', 'Book', 'Source']:
                    field = soup.find('div', class_='gsc_oci_field', string=re.compile(field_name, re.IGNORECASE))
                    if field:
                        venue_value = field.find_next_sibling('div', class_='gsc_oci_value')
                        break
            
            if venue_value:
                details['venue_full'] = venue_value.text.strip()
                
                # Determine publication type based on venue
                venue_lower = details['venue_full'].lower()
                if 'journal' in venue_lower or 'transactions' in venue_lower or 'letters' in venue_lower:
                    details['publication_type'] = 'Journal'
                elif 'workshop' in venue_lower or 'wksp' in venue_lower:
                    details['publication_type'] = 'Workshop'
                elif 'arxiv' in venue_lower or 'preprint' in venue_lower or 'corr' in venue_lower:
                    details['publication_type'] = 'Preprint'
                elif 'symposium' in venue_lower or 'conference' in venue_lower or 'proceedings' in venue_lower:
                    details['publication_type'] = 'Conference'
            
            # Success - break retry loop
            break
            
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"    Retry {attempt + 1}/{max_retries} for {pub_url[:50]}...")
                time.sleep(2)  # Wait before retry
            else:
                print(f"    Warning: Could not fetch details from {pub_url[:50]}...: {e}")
    
    return details


def normalize_title(title: str) -> str:
    """Normalize title for comparison (remove punctuation, lowercase, extra spaces)."""
    # Remove punctuation and convert to lowercase
    normalized = re.sub(r'[^\w\s]', '', title.lower())
    # Remove extra whitespace
    normalized = ' '.join(normalized.split())
    return normalized


def are_titles_similar(title1: str, title2: str, threshold: float = 0.9) -> bool:
    """Check if two titles are similar enough to be considered duplicates."""
    norm1 = normalize_title(title1)
    norm2 = normalize_title(title2)
    
    # Exact match after normalization
    if norm1 == norm2:
        return True
    
    # Check if one is substring of other (for abbreviated titles)
    if norm1 in norm2 or norm2 in norm1:
        # Only consider it similar if the shorter one is at least 80% of the longer
        min_len = min(len(norm1), len(norm2))
        max_len = max(len(norm1), len(norm2))
        if min_len / max_len > 0.8:
            return True
    
    return False


def is_valid_publication(pub: Dict) -> bool:
    """Check if an entry is a valid publication (not a committee, editorial, etc.)."""
    title = pub['title'].lower()
    
    # Filter out non-paper entries
    invalid_patterns = [
        'program committee',
        'editorial board',
        'organizing committee',
        r'^\d{4}$',  # Just a year
        'proceedings of',  # Usually just proceedings without paper
        r'©.*ieee.*doi',  # Copyright notices
        'owen arden',  # List of people (committee members)
        'buildSec',  # Conference names without papers
        r'^[a-z&\s]+\d{4}$',  # Conference acronyms like "CSF 2021"
    ]
    
    for pattern in invalid_patterns:
        if re.search(pattern, title, re.IGNORECASE):
            return False
    
    # Must have authors
    if not pub.get('authors') or len(pub['authors']) < 3:
        return False
    
    return True


def remove_duplicates(publications: List[Dict]) -> List[Dict]:
    """Remove duplicate publications and invalid entries based on title similarity."""
    unique_pubs = []
    seen_titles = []
    
    for pub in publications:
        # First check if it's a valid publication
        if not is_valid_publication(pub):
            print(f"  Filtering out non-paper: {pub['title'][:60]}...")
            continue
        
        is_duplicate = False
        for seen_title in seen_titles:
            if are_titles_similar(pub['title'], seen_title):
                is_duplicate = True
                print(f"  Removing duplicate: {pub['title']}")
                break
        
        if not is_duplicate:
            unique_pubs.append(pub)
            seen_titles.append(pub['title'])
    
    print(f"✓ Removed {len(publications) - len(unique_pubs)} duplicates/invalid entries\n")
    return unique_pubs


def extract_existing_titles(publications_file: str) -> Set[str]:
    """Extract normalized titles from existing publications.md file."""
    existing_titles = set()
    
    try:
        with open(publications_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all publication titles (looking for h3 with class pub-title)
        soup = BeautifulSoup(content, 'html.parser')
        title_elements = soup.find_all('h3', class_='pub-title')
        
        for elem in title_elements:
            title = elem.text.strip()
            normalized = normalize_title(title)
            existing_titles.add(normalized)
        
        print(f"✓ Found {len(existing_titles)} existing publications\n")
        
    except FileNotFoundError:
        print(f"✗ Could not find {publications_file}\n")
    except Exception as e:
        print(f"✗ Error reading existing publications: {e}\n")
    
    return existing_titles


def highlight_team_members(authors: str) -> str:
    """Add HTML span highlighting to team members in author list."""
    result = authors
    for member in TEAM_MEMBERS:
        # Create regex pattern to match the name (case-insensitive, with word boundaries)
        pattern = r'\b' + re.escape(member) + r'\b'
        replacement = f'<span class="author-highlight">{member}</span>'
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    return result


def determine_pub_type_class(pub_type: str) -> str:
    """Return the CSS class for publication type badge."""
    type_map = {
        'Conference': 'pub-type-conference',
        'Journal': 'pub-type-journal',
        'Workshop': 'pub-type-workshop',
        'Preprint': 'pub-type-preprint'
    }
    return type_map.get(pub_type, 'pub-type-conference')


def generate_publication_html(pub: Dict) -> str:
    """Generate HTML for a single publication."""
    pub_type = pub['details'].get('publication_type', 'Conference')
    pub_type_class = determine_pub_type_class(pub_type)
    
    # Use full title from details if available, otherwise use the short title
    # This ensures special characters like DY⋆ are preserved
    title = pub['details'].get('full_title', pub['title'])
    if not title or len(title) < 3:
        title = pub['title']
    
    # Escape HTML but preserve certain special chars
    import html as html_module
    title = html_module.escape(title)
    
    # Highlight team members in authors
    authors_html = highlight_team_members(pub['authors'])
    
    # Generate venue information - prefer detailed venue, fall back to short venue
    venue_full = pub['details'].get('venue_full', '')
    venue_short = pub.get('venue', '')
    
    # Use the more detailed one
    if venue_full and len(venue_full) > len(venue_short):
        venue = venue_full
    elif venue_short:
        venue = venue_short
    else:
        venue = "Publication venue information not available"
    
    # Parse venue to extract conference/journal name and location
    # Common patterns: "Conference Name, Year" or "Conference Name (Acronym), Location, Year"
    venue_parts = venue.split(',')
    if len(venue_parts) >= 1:
        venue_name = venue_parts[0].strip()
        venue_location = ', '.join(venue_parts[1:]).strip() if len(venue_parts) > 1 else ""
    else:
        venue_name = venue
        venue_location = ""
    
    # Escape HTML in venue
    venue_name = html_module.escape(venue_name)
    if venue_location:
        venue_location = html_module.escape(venue_location)
    
    html = f'''  <div class="publication-card">
    <span class="pub-type-badge {pub_type_class}">{pub_type}</span>
    <h3 class="pub-title">{title}</h3>
    <p class="pub-authors">
      {authors_html}
    </p>
    <p class="pub-venue">'''
    
    if venue_name != "Publication venue information not available":
        html += f'''<strong>{venue_name}</strong>'''
        if venue_location:
            html += f''', {venue_location}'''
    else:
        html += f'''<em>{venue_name}</em>'''
    
    if pub['year']:
        html += f''', {pub['year']}'''
    
    html += f'''
    </p>
    <div class="pub-links">'''
    
    # Add PDF link if available
    if pub['details'].get('pdf_link'):
        pdf_url = pub['details']['pdf_link']
        # Make sure it's a full URL
        if not pdf_url.startswith('http'):
            pdf_url = 'https://' + pdf_url if not pdf_url.startswith('//') else 'https:' + pdf_url
        html += f'''
      <a href="{html_module.escape(pdf_url)}" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>'''
    
    # Add Google Scholar link
    if pub['link']:
        html += f'''
      <a href="{html_module.escape(pub['link'])}" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>'''
    
    html += '''
    </div>
  </div>

'''
    
    return html


def insert_publications(publications_file: str, new_publications: List[Dict]):
    """Insert new publications into publications.md, organized by year."""
    try:
        with open(publications_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Group publications by year
        pubs_by_year = {}
        for pub in new_publications:
            year = pub['year'] if pub['year'] else 'Unknown'
            if year not in pubs_by_year:
                pubs_by_year[year] = []
            pubs_by_year[year].append(pub)
        
        # Sort years in descending order
        sorted_years = sorted([y for y in pubs_by_year.keys() if y != 'Unknown'], 
                            key=lambda x: int(x) if x.isdigit() else 0, 
                            reverse=True)
        
        if 'Unknown' in pubs_by_year:
            sorted_years.append('Unknown')
        
        # Generate HTML for each year
        insertions = []
        for year in sorted_years:
            # Check if year section exists
            year_pattern = f'<h2 class="year-header">{year}</h2>'
            
            if year_pattern in content:
                # Year section exists, insert after the h2
                print(f"  Adding {len(pubs_by_year[year])} publications to existing {year} section")
                
                # Find the position right after the year header
                year_pos = content.find(year_pattern)
                insert_pos = content.find('\n', year_pos) + 1
                
                # Skip to after any existing publications in this section
                # Find the next year section or end of content
                next_year_pos = content.find('<div class="year-section">', insert_pos)
                if next_year_pos == -1:
                    next_year_pos = content.find('</div>\n\n</div>', insert_pos)
                
                # Find the last </div> before the next section
                search_end = next_year_pos if next_year_pos != -1 else len(content)
                last_pub_end = content.rfind('</div>\n\n  <div class="publication-card">', 
                                            insert_pos, search_end)
                
                if last_pub_end != -1:
                    insert_pos = last_pub_end + len('</div>\n\n')
                else:
                    # No existing publications, insert right after year header
                    insert_pos = content.find('\n', year_pos) + 1
                
                # Generate HTML for all publications in this year
                pubs_html = '\n'.join([generate_publication_html(pub) 
                                      for pub in pubs_by_year[year]])
                
                insertions.append((insert_pos, pubs_html))
                
            else:
                # Year section doesn't exist, create new section
                print(f"  Creating new {year} section with {len(pubs_by_year[year])} publications")
                
                # Find where to insert the new year section
                # It should be inserted in chronological order
                year_sections = re.finditer(r'<h2 class="year-header">(\d+)</h2>', content)
                insert_before_year = None
                insert_pos = -1
                
                for match in year_sections:
                    existing_year = int(match.group(1))
                    if year.isdigit() and int(year) > existing_year:
                        insert_before_year = existing_year
                        # Find the start of this year's section
                        insert_pos = content.rfind('<div class="year-section">', 0, match.start())
                        break
                
                if insert_pos == -1:
                    # Insert at the end, before the closing </div>
                    insert_pos = content.rfind('</div>\n\n</div>')
                
                # Generate the complete year section
                year_section = f'''<div class="year-section">
  <h2 class="year-header">{year}</h2>
  
'''
                year_section += '\n'.join([generate_publication_html(pub) 
                                          for pub in pubs_by_year[year]])
                year_section += '</div>\n\n'
                
                insertions.append((insert_pos, year_section))
        
        # Apply all insertions (in reverse order to maintain positions)
        insertions.sort(key=lambda x: x[0], reverse=True)
        for pos, html in insertions:
            content = content[:pos] + html + content[pos:]
        
        # Write back to file
        with open(publications_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✓ Successfully updated {publications_file}")
        
    except Exception as e:
        print(f"\n✗ Error updating publications file: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Main execution function."""
    print("=" * 70)
    print("Google Scholar Publication Fetcher")
    print("=" * 70)
    print()
    
    # Show configuration
    print(f"Configured profiles: {len(GOOGLE_SCHOLAR_PROFILES)}")
    print(f"Team members to highlight: {len(TEAM_MEMBERS)}")
    print()
    
    # Step 1: Fetch publications from all profiles
    print("Step 1: Fetching publications from Google Scholar profiles...")
    print("-" * 70)
    all_publications = []
    
    for profile_url in GOOGLE_SCHOLAR_PROFILES:
        pubs = fetch_scholar_profile(profile_url, max_papers=100)
        all_publications.extend(pubs)
        time.sleep(3)  # Rate limiting between profiles
    
    print(f"Total publications fetched: {len(all_publications)}\n")
    
    # Step 2: Remove duplicates
    print("Step 2: Removing duplicate publications...")
    print("-" * 70)
    unique_publications = remove_duplicates(all_publications)
    print(f"Unique publications: {len(unique_publications)}\n")
    
    # Step 3: Check existing publications
    print("Step 3: Checking existing publications in publications.md...")
    print("-" * 70)
    existing_titles = extract_existing_titles(PUBLICATIONS_FILE)
    
    # Filter out publications that already exist
    new_publications = []
    for pub in unique_publications:
        normalized = normalize_title(pub['title'])
        if normalized not in existing_titles:
            new_publications.append(pub)
        else:
            print(f"  Skipping existing: {pub['title']}")
    
    print(f"\nNew publications to add: {len(new_publications)}\n")
    
    # Step 4: Sort and insert publications
    if new_publications:
        print("Step 4: Inserting new publications into publications.md...")
        print("-" * 70)
        
        # Sort by year (descending) and maintain Google Scholar order within each year
        new_publications.sort(key=lambda x: (
            -int(x['year']) if x['year'].isdigit() else 0,
            all_publications.index(x)  # Maintain original order from Scholar
        ))
        
        insert_publications(PUBLICATIONS_FILE, new_publications)
    else:
        print("No new publications to add.")
    
    print("\n" + "=" * 70)
    print("✓ Done!")
    print("=" * 70)


if __name__ == "__main__":
    main()
