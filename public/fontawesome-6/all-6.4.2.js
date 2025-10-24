/* FontAwesome 6 Free Icons - Basic Implementation */
/* This is a minimal implementation. For full FontAwesome, use the official CDN */

@font-face {
  font-family: 'Font Awesome 6 Free';
  font-style: normal;
  font-weight: 900;
  font-display: block;
  src: url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-solid-900.woff2") format("woff2"),
       url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-solid-900.ttf") format("truetype");
}

@font-face {
  font-family: 'Font Awesome 6 Brands';
  font-style: normal;
  font-weight: 400;
  font-display: block;
  src: url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-brands-400.woff2") format("woff2"),
       url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-brands-400.ttf") format("truetype");
}

.fab, .fa-brands {
  font-family: 'Font Awesome 6 Brands';
  font-weight: 400;
}

.fas, .fa-solid {
  font-family: 'Font Awesome 6 Free';
  font-weight: 900;
}

.fa:before {
  display: inline-block;
  font-style: normal;
  font-variant: normal;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
}

/* Social Media Icons */
.fa-linkedin:before { content: "\f08c"; }
.fa-twitter:before { content: "\f099"; }
.fa-whatsapp:before { content: "\f232"; }
.fa-envelope:before { content: "\f0e0"; }

/* Other icons */
.fa-angle-up:before { content: "\f106"; }