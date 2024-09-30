[back to main Readme](README.md)

## Code Validation

### HTML Validation

HTML Validation was done with the W3 HTML Validator (https://validator.w3.org/nu/)

Page | URL | Logged In Status | Result | info
--- | --- | --- | --- | ---
Landing Page | / | Guest | pass | 
Products | products/?sort=price&direction=asc | Guest | Pass |
Training equipment | products/?category=freeweights,kettlebells,spinning,yogamats | Guest | Pass |
Courses | products/?category=workoutprograms | Guest | Pass |
Special Offers | products/?category=new_arrivals,clearance | Guest | Pass |
trainers view all trainers | trainers/alltrainers/ | Guest | Pass |
trainer details | trainers/trainerdetails/1 | Guest | Pass |
about | about/ | Guest | Pass |
Product details | products/3/ | Guest | Pass |
Shopping bag | bag/ | Guest | Pass |
Checkout | checkout/ | Guest | Pass | 
Landing Page | / | Admin | Pass | 
Products | products/?sort=price&direction=asc | Admin | Pass |
Training equipment | products/?category=freeweights,kettlebells,spinning,yogamats | Admin | Pass |
Courses | products/?category=workoutprograms | Admin | Pass |
Special Offers | products/?category=new_arrivals,clearance | Admin | Pass |
trainer details | trainers/trainerdetails/1 | Admin | Pass |
about | about/ | Admin | Pass |
Product details | products/3/ | Admin | Pass |
Shopping bag | bag/ | Admin | Pass |
Checkout | checkout/ | Admin | Pass | 
trainers add trainer | trainers/ | Admin | Pass |
trainers view all trainers | trainers/alltrainers/ | Admin | Pass |
trainers add workout program | products/add/ | Admin | Pass |
trainer view workout programs | trainers/trainercourses/ | Admin | Pass |
trainer class attendance | trainers/classAttendance/1/ | Admin | Pass |
My Account Product Management | products/add/ | Admin | Pass
My Account My Profile | profile/ | Admin | Pass |

### CSS Validation

    The CSS was validated using the W3 CSS Validator (https://jigsaw.w3.org/css-validator/)

File | Result | issues
--- | --- | ---
checkout.css | Pass | 1 Warning
profile.css |  Pass | 
base.css | Pass |

### Python Validation

The following files were tested with the CI Python Linter(https://pep8ci.herokuapp.com/)

App | File | Result
--- | --- | ---
about | admin.py | Pass
about | apps.py | Pass
about | forms.py | Pass
about | views.py | Pass
bag | apps.py | Pass
bag | contexts.py | Pass
bag | views.py | Pass
checkout | admin.py | Pass
checkout | apps.py | Pass
checkout | forms.py | Pass
checkout | signals.py | Pass
checkout | views.py | Pass
checkout | webhook_handler.py | Pass
checkout | webhooks.py | Pass
home | apps.py | Pass
home | views.py | Pass
products | admin.py | Pass
products | apps.py | Pass
products | forms.py | Pass
products | views.py | Pass
products | widgets.py | Pass
profiles | apps.py | Pass
profiles | forms.py | Pass
profiles | views.py | Pass
trainers | admin.py | Pass
trainers | apps.py | Pass
trainers | forms.py | Pass
trainers | views.py | Pass
trainers | widgets.py | Pass
trainers | checkif_student_already_checked.py | Pass

### JavaScript Validation
JavaScript linting was done with JSHint (https://jshint.com/)

App | File | Result
--- | --- | ---
checkout | stripe_elements.js | Pass
profiles | countryfield.js | Pass

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


## User Story Testing

### EPIC User
I can administer my User account and contact the site if need be

User Story | deskop | mobile | notes
--- | --- | --- | ---
As a User I can Register with the site so I can Login | 30/924 | 30/9/24 |
As a User I can Login to the site so I can use and administer my account | 30/924 | 30/9/24 |
As a User I can view Trainers and their courses and see their Bio's | 30/9/24 | 30/9/24 |
As a User I can order a product so that I can get it delivered to me | 30/9/24 | 30/9/24 |
As a User I can add a product to the Bag and administer the shopping bag | 30/9/24 | 30/9/24 |
As a User I can edit my profile so that I can have an up to date profile | 30/9/24 | 30/9/24 |
As a User I can enroll on a course so that I can partake in a workout program | 30/9/24 | 30/9/24 |
As a User I can contact site admin for any site issues that I may have |
As a User I can contact a Trainer for any queries or concerns I may have in relation to workouts |




