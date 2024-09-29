[back to main Readme](README.md)

## Code Validation

### HTML Validation

HTML Validation was done with the W3 HTML Validator (https://validator.w3.org/nu/)

Page | URL | Logged In Status | Result | info
--- | --- | --- | --- | ---
Landing Page | / | Guest | pass | 1 warning
Products | products/?sort=price&direction=asc | Guest | Pass |
Training equipment | products/?category=freeweights,kettlebells,spinning,yogamats | Guest | Pass |
Courses | products/?category=workoutprograms | Guest | Pass |
Special Offers | products/?category=new_arrivals,clearance | Guest | Pass |
trainers view all trainers | trainers/alltrainers/ | Guest | Pass |
trainer details | trainers/trainerdetails/1 | Guest | 

### CSS Validation

    The CSS was validated using the W3 CSS Validator (https://jigsaw.w3.org/css-validator/)

File | Result | issues
--- | --- | ---
checkout.css | Pass | 1 Warning
profile.css |  Pass | 
base.css | Pass |

### Python Validation

### JavaScript Validation

## Wave Web AIM

Page | Errors | Alerts | Result
--- | --- | --- | ---
Home | 0 | skipped heading level | pass
Home search all products by price | 0 | skipped heading level, possible heading | pass
courses | 0 | skipped heading level, possible heading | pass
special offers | 0 | skipped heading level, possible heading | pass
view all trainers | 0 | skipped heading level | pass
trainer logged in add workout program | 0 | skipped heading level | pass
trainer logged in view workout programs | 0 | skipped heading level | pass
about page | 0 | skipped heading level | pass
class attendance | 0 | orphaned form label, missing fieldset, skipped heading level | pass
my profile | 0 | skipped heading level | pass
add trainer | 0 | skipped heading level | pass
view trainer details | 0 | skipped heading level | pass

## Lighthouse testing

It was noticed that for lighthouse testing that it was best to use incognito mode on Google Chrome. It was also noticed that i get different values if I have my VPN active or if I connect outside my dedicated firewall.

Page | Performance | Accessibility | Best Practice | SEO
--- | --- | --- | --- | ---
Home (landing page desktop) | 96 | 93 | 100 | 100
Home (mobile) | 87 | 92 | 100 | 100
all products listing by price (desktop) | 91 | 94 | 100 | 91
all products listing (mobile) | 72 | 95 | 100 | 91
all training equipment (desktop) | 92 | 94 | 100 | 91
all training equipment (mobile) | 73 | 95 | 100 | 91
courses | | | | todo
all specials (desktop) | 92 | 94 | 100 | 91
all specials (mobile) | 69 | 95 | 100 | 91
trainers view all trainers | | | | todo
trainers add workout program | | | | todo
trainers view workout programs | | | | todo
about (desktop) | 95 | 93 | 100 | 100
about (mobile) | 82 | 95 | 100 | 100
my account project management (desktop) | 90 | 94 | 100 | 100
my account project management (mobile) | 82 | 93 | 100 | 100
my account my profile (desktop) | 91 | 94 | 100 | 100
my account my profile (mobile) | 77 | 95 | 100 | 100






