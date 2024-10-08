![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome
- [Welcome](#welcome)
- [Project Research and Preparation](#project-research-and-preparation)
  * [Fitness Fanatic](#fitness-fanatic)
    + [Landing page on desktop](#landing-page-on-desktop)
    + [Landing page on mobile](#landing-page-on-mobile)
    + [Categories](#categories)
  * [Site Testing](#site-testing)
  * [E-Commerce Business Model](#e-commerce-business-model)
  * [Marketing Strategies](#marketing-strategies)
  * [Planning](#planning)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Wireframes](#wireframes)
    + [About](#about)
    + [Bag](#bag)
    + [Checkout](#checkout)
    + [Contact Trainers](#contact-trainers)
    + [Home Page/ Landing Page](#home-page--landing-page)
    + [Product new arrivals](#product-new-arrivals)
    + [Product workout programs](#product-workout-programs)
    + [Products](#products)
    + [Trainer Class Admin](#trainer-class-admin)
    + [Trainer Profile](#trainer-profile)
    + [Trainers Add Workout Program](#trainers-add-workout-program)
    + [Trainers](#trainers)
    + [User Profile](#user-profile)
    + [Admin Add Trainer](#admin-add-trainer)
  * [EPICS](#epics)
    + [Admin](#admin)
    + [Trainer](#trainer)
    + [User](#user)
  * [User Stories](#user-stories)
    + [Admin](#admin-1)
    + [Trainer](#trainer-1)
    + [User](#user-1)
  * [UX Colour Palette](#ux-colour-palette)
  * [Images](#images)
  * [Website Design](#website-design)
    + [Header](#header)
    + [Footer](#footer)
    + [Homepage](#homepage)
      - [Products](#products-1)
      - [Add Product](#add-product)
    + [Courses](#courses)
    + [Trainers](#trainers-1)
      - [Admin Add Trainer](#admin-add-trainer-1)
      - [View All Trainers](#view-all-trainers)
        * [View Trainer Detail](#view-trainer-detail)
        * [View Trainer Email](#view-trainer-email)
      - [Add Workout Program](#add-workout-program)
      - [View Workout Programs](#view-workout-programs)
        * [Class Attendance](#class-attendance)
    + [About](#about-1)
    + [Profile](#profile)
    + [Bag](#bag-1)
  * [Future Features](#future-features)
  * [Technologies Used](#technologies-used)
  * [Deployment](#deployment)
    + [Clone GitHub Repository](#clone-github-repository)
    + [Deployment on Heroku](#deployment-on-heroku)
    + [Amazon AWS S3](#amazon-aws-s3)
    + [IAM](#iam)
    + [Final Setup](#final-setup)
  * [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Project Research and Preparation

## Fitness Fanatic

Fitness Fanatic is a fictional website designed specifically for Code Institute for Project number 5 which is an e-commerce website. [link](https://fitness-fanatic-8422c1e8a4c9.herokuapp.com/) This site is all about training where you can buy fitness programs which go on for several weeks at several days a week. Or you can purchase basic fitness equipment for home use. The fictional workout programs are given in a fictional training location in person at say Fitness Fanatic Bridgewater Arklow. I chose the location Arklow as its where I live and for this type of business there is a lot of local competition in the local area.

On the site you can purchase equipment.

On the site you can purchase a training workout program which is several days a week for several weeks.

On the site you can edit your profile once logged in.

On the site the administrator can add trainers, delete trainers and edit trainers.

On the site the trainers can edit their profile (It should be noted that the trainer profile is different from the user profile as it allows a trainer if they want to purchase items from the center through the normal purchase workflow).

On the site a trainer can create, edit and delete workout programs given by them once logged in as a trainer.

On the site a trainer once logged in can view their mail where a user can contact them through a trainer contact form. This is done through a database table and the trainer contact template shows the trainer their email/(entries in the database table) where the new email is shown and once marked as read it will no longer display. This is just a text based dump of the table info with a mark as read button. Once marked as read the read BooleanField in the table is marked as True. In this template it is hoped that it can be viewed by not read and year. For this project the entries wont be deleted as a paper trail would be needed for management.

On the site web admin can be contacted through a contact form which can be viewed via site admins in the Django site admin interface.

On the site a user can view trainer profiles and workout programmes given by each trainer.

On the site a trainer can administer their classes via an attendance form where it shows a list of students which purchased the course and a checkbox to say they attended at the date the form is opened and a button to submit the form.

If time permits I will have typical training workout programmes like the Skogg kettlebell system, RKS kettlebell system, for weight training the Body Beast workout program, Suspension training program, Scientific stretching program. These programs will be broken down into what is covered over the duration of the course. This information will be a template link on the trainers profile template page. Where if a user is interested in a program they can read about it here.

[Link To Live Site](https://fitness-fanatic-8422c1e8a4c9.herokuapp.com/)

[Goto Top](#welcome)

### Landing page on desktop 

![Home Landing Page of site](/readme_images/home_landing_page.png)

### Landing page on mobile

![Home Landing page mobile](/readme_images/home_landing_page_mobile.png)

### Categories

1. name: freeweights, friendly_name: Free Weights
2. name: kettlebells, friendly_name: Kettlebells
3. name: spinning, friendly_name: Spinning
4. name: yogamats, friendly_name: Yoga Mats
5. name: clearance, friendly_name: Clearance
6. name: new_arrivals, friendly_name: New Arrivals
7. name: workoutprograms, friendly_name: Workout Programs

[Goto Top](#welcome)

## Site Testing

A sererate README_TESTING.md file was used for testing and can be found [testing readme here](README_TESTING.md) . In this file I explain testing workflows.

[Goto Top](#welcome)

## E-Commerce Business Model

Fitness Fanatic is a B2C type application. The site is focused at local employment. Where the classes are held in a local training center at about 15 people per class.

## Marketing Strategies

Fitness Fanatic is a local training center offering the purchase of various small type training equipment for home use. But the site also allows the customers to enroll on courses held at the local center where class sizes are small (typically 15). The site also allows the site administrator to manage trainers where a trainer could be a per workout program given hire (type kinda freelance). The trainer would register with admin and via a form setup their profile and then once registered, they can begin creating workout programs for several weeks at a time.

The offering for workout programs vary from the Body Beast program to the RKS Kettlebell System to the Skogg Kettlebell system to Spinning to Scientific Stretching. These are small offerings but are varied and interesting courses which would typically go on for an hour.

Marketing is done on customer satisfaction where they would use word of mouth to spread the word about a cool training program. At Fitness Fanatic a Facebook webpage was also setup to spread the word about the training programs on offer [Facebook Page](/readme_images/facebook_fitness_fanatic_screengrab.png)

[Goto Top](#welcome)

## Planning 

## Entity Relationship Diagram

![Fitness Fanatic ERD](/readme_images/fitness_fanatic_erd.png)

[Goto Top](#welcome)

## Wireframes

### About

![About](/readme_images/about.png)

[Goto Top](#welcome)

### Bag

![bag](/readme_images/bag.png)

[Goto Top](#welcome)

### Checkout

![Checkout](/readme_images/checkout.png)

[Goto Top](#welcome)

### Contact Trainers

![Contact Trainers](/readme_images/contact_trainers.png)

[Goto Top](#welcome)

### Home Page/ Landing Page

![Home Page](/readme_images/home_page.png)

[Goto Top](#welcome)

### Product new arrivals

![Product new arrivals](/readme_images/products_category_new_arrivals.png)

[Goto Top](#welcome)

### Product workout programs

![Product workout programs](/readme_images/Products_category_workoutprograms.png)

[Goto Top](#welcome)

### Products

![Products](/readme_images/products.png)

[Goto Top](#welcome)

### Trainer Class Admin

![Trainer Class Admin](/readme_images/trainer_class_admin.png)

[Goto Top](#welcome)

### Trainer Profile

![Trainer Profile](/readme_images/trainer_profile.png)

[Goto Top](#welcome)

### Trainers Add Workout Program

![Trainers Add Workout Program](/readme_images/trainers_add_workout_program.png)

[Goto Top](#welcome)

### Trainers

![Trainers](/readme_images/trainers.png)

[Goto Top](#welcome)

### User Profile

![User Profile](/readme_images/user_profile.png)

[Goto Top](#welcome)

### Admin Add Trainer

![Admin Add Trainer](/readme_images/add_trainer.png)

[Goto Top](#welcome)

## EPICS

### Admin

- I can administer the site and Trainers <EPIC Admin>
  - I can read Site Admin emails through Django Admin
  - I can create, edit and delete (CRUD) trainers
  - I can create, edit and delete (CRUD) products

### Trainer

- I can administer my Trainer account <EPIC Trainer>
  - I can edit the trainer profile
  - I can create, edit and delete (CRUD) a workout program
  - I can view trainer email and mark it as read
  - I can set class attendance for enrolled students

### User

- I can administer my User account and contact the site if need be <EPIC User>
  - As a User I can Register with the site so I can Login
  - As a User I can Login to the site so I can use and administer my account
  - As a User I can view Trainers and their courses and see their Bio's
  - As a User I can order a product so that I can get it delivered to me
  - As a User I can add a product to the Bag and administer the shopping bag
  - As a User I can edit my profile so that I can have an up to date profile
  - As a User I can enroll on a course so that I can partake in a workout program
  - As a User I can contact site admin for any site issues that I may have
  - As a User I can contact a Trainer for any queries or concerns I may have in relation to workouts

[Goto Top](#welcome)

## User Stories

### Admin

- As an Admin User I can read Site Admin emails through the Django Admin interface <Admin View Site Email>
- As an Admin User I can create, edit and delete (CRUD) trainers so that I can administer trainers <Admin CRUD Trainers>
- As an Admin User I can create, edit and delete (CRUD) products so that I can administer products <Admin CRUD Products>

### Trainer

- As a Trainer I can edit my Trainer Profile so that I can have an update profile <Trainer edit Trainer Profile>
- As a Trainer I can create, edit and delete (CRUD) workout programs so that I can manage my workout programs <Trainer CRUD Workouts>
- As a Trainer I can view Trainer email so that I can manage my email <Trainer view Email>
- As a Trainer I can set class attendance for a class so that I can manage my workout program <Trainer Class Attendance>

### User

- As a User I can Register with the site so I can Login <User Register>
- As a User I can Login to the site so I can use and administer my account <User Login>
- As a User I can view Trainers and their courses and see their Bio's <User View Trainers>
- As a User I can order a product so that I can get it delivered to me <User Order Product>
- As a User I can add a product to the Bag and administer the shopping bag <User Administer Bag>
- As a User I can edit my profile so that I can have an up to date profile <User edit Profile>
- As a User I can enroll on a course so that I can partake in a workout program <User enroll Course>
- As a User I can contact site admin for any site issues that I may have <User email Site Admin>
- As a User I can contact a Trainer for any queries or concerns I may have in relation to workouts <User email Trainer>

[Goto Top](#welcome)

## UX Colour Palette

Colours used 

Value |
--- |
white |
#e6ebf1 |
#cfd7df |
#fefde5 |
#aab7c4 |
#000 |
rgba(23, 162, 184, .85) |
#3B4754 |
#222 |
#fff |
#007bff |
#6c757d |
#28a745 |
#dc3545 |
#ffc107 |
#17a2b8 |
#f8f9fa |
#343a40 |

[Goto Top](#welcome)

## Images

The images used for the site were researched and got from various sources. The planning and credits in raw format can be found [here](README_IMAGES.md)

[Goto Top](#welcome)

## Website Design
  For this site I kept things simple and strongly followed the walkthrough.

### Header
 
![Header Screengrab](/readme_images/header.png)

[Goto Top](#welcome)

### Footer

![Footer Screengrab](/readme_images/footer.png)

[Goto Top](#welcome)

### Homepage

  ![Home page desktop](/readme_images/home_landing_page.png)

  ![Home page mobile](/readme_images/home_landing_page_mobile.png)

[Goto Top](#welcome)

#### Products

  ![Products listing desktop](/readme_images/products_listing_desktop.png)

  ![Products listing mobile](/readme_images/products_listing_mobile.png)

[Goto Top](#welcome)

#### Add Product
  For the add product the logged in user has to be a site admin user or a registered trainer. Products can be of two types training equipment for sale or workout programs. I will deal with workout programs below under trainers as that case is more complex!.

  ![Add Product desktop](/readme_images/add_product_desktop.png)

  ![Add Product mobile](/readme_images/add_product_mobile.png)

[Goto Top](#welcome)

### Courses
  Courses or workout programs are given by registered trainers. 
### Trainers

#### Admin Add Trainer
  For a trainer to be registered on the system site admin has to add a trainer to the trainers list. This form has to be filled in and the password shown is auto generated on a per form basis and is shown in plain text so the admin and trainer can easily use it to log on to the system. Also once this form is submitted the trainer shows up on the system and is live on the View All Trainers link on the trainers nav-bar and can be contacted immediately via the online trainer contact form!.

  ![Add Trainer desktop](/readme_images/add_trainer_desktop.png)

  ![Add Trainer mobile](/readme_images/add_trainer_mobile.png)

[Goto Top](#welcome)

#### View All Trainers
  Once a trainer is registered their profile is put immediately on the view all trainers page.

  ![View All Trainers desktop](/readme_images/view_trainers_desktop.png)

  ![View all trainers mobile](/readme_images/view_trainers_mobile.png)

[Goto Top](#welcome)

##### View Trainer Detail
  The View trainer detail page is to show the trainer details and allow a customer to contact that trainer via an email. Also on this page its possible for a logged in trainer to view their email.

  ![view Trainer detail desktop](/readme_images/view_trainer_detail.png)

  ![View trainer detail mobile](/readme_images/view_trainer_detail_mobile.png)

[Goto Top](#welcome)

##### View Trainer Email
  This is a simple form to read open email tickets where if you check the checkbox and click on Update Email Status, the email is no longer visible to the trainer as the ticket is dealt with but can be viewed in admin by admin in the Django Admin App.

  ![View Trainer Email desktop](/readme_images/view_trainer_email_desktop.png)

  ![View Trainer Email mobile](/readme_images/view_trainer_email_mobile.png)

[Goto Top](#welcome)

#### Add Workout Program
  A Workout program is like a normal product but has extra information fo instance trainer name class size, start date, end date and number of weeks

  ![Add Workout desktop](/readme_images/add_workout_desktop.png)

  ![Add workout mobile](/readme_images/add_workout_mobile.png)

[Goto Top](#welcome)

#### View Workout Programs
  This navbar link is used to list workout programs where once clicked upon will bring up the class attendance form

  ![View Workout Programs](/readme_images/view_workout_programs.png)

[Goto Top](#welcome)

##### Class Attendance
    
  The class attendance is used to log attendance to a class

  ![The Class Attendance Form](/readme_images/class_attendance.png)

[Goto Top](#welcome)

### About

  The About page is to view some about information and a form to contact site admin

  ![About desktop](/readme_images/about_desktop.png)

  ![About mobile](/readme_images/about_mobile.png)

[Goto Top](#welcome)

### Profile
  The profile is used to store user information used by the system for ease of purchasing of products. On this page it also shows an order history.

  ![My profile desktop](/readme_images/my_profile_desktop.png)

  ![My profile mobile](/readme_images/my_profile_mobile.png)

[Goto Top](#welcome)

### Bag
  ![Shopping bag desktop](/readme_images/shopping_bag_desktop.png)

  ![Shopping bag mobile](/readme_images/shopping_bag_mobile.png)

[Goto Top](#welcome)

## Future Features

- 1. To have a stock management system. For the site as is the actual weights and gym equipment are to be supplied from the York Fitness warehouse and the workout programs are to be at 15 per class where for the initial startup the numbers of enrolled students would determine the number of classes of the same program. A stock management system would stop the numbers of enrolled students going too high and thus the center not being able to provide a reliable service.
- 2. Statistics. At the moment a trainer can log class attendance, but cant view stats on it. For instance a graphical chart showing attendance numbers on days or week numbers migh be useful.
- 3. If a customer chooses to purchase several workout programs. On the class attendance sheet it should show that the customer can have guests and you should be able to add a name to them on the attendance sheet.
- 4. Customer fitness sheets showing date and time class and maybe weight used. If applicable number of reps at weight (for weight trainer this is important)
- 5. Delete account. To allow a customer to delete their account. 
- 6. For this test database and system a change password capability isnt really needed but for a live system a change password would be needed. This is simple todo as allauth has the functionality in place. All that is required is on the navlink under profile you would just add a link to the change password allauth form and let allauth do the rest.

[Goto Top](#welcome)

## Technologies Used
  - HTML
  - Python
  - CSS
  - JavaScript
  - Django used as the Python framework for the site
  - AWS S3 used for online static and media file storage
  - PostgresSQL used as the relational database management
  - Heroku used for hosting the site
  - GitHub for storing repository of development
  - GitPod used for cloud IDE
  - Balsamiq used for wireframing
  - Bootstrap 4 used for frontend framework
  - favicon.io used to make favicon for the site

dependencies
app | version
--- | ---
asgiref | 3.8.1
boto3 | 1.34.159
botocore | 1.34.159
crispy-bootstrap4 | 2024.1
dj-database-url | 0.5.0
Django | 4.2.15
django-allauth | 0.57.2
django-countries | 7.2.1
django-crispy-forms | 2.3
django-storages | 1.14.4
django-summernote | 0.8.20.0
gunicorn | 23.0.0
jmespath | 1.0.1
oauthlib | 3.2.2
pillow | 10.4.0
psycopg2 | 2.9.9
PyJWT | 2.9.0
python3-openid | 3.2.0
requests-oauthlib | 2.0.0
s3transfer | 0.10.2
sqlparse | 0.5.1
stripe | 10.6.0

[Goto Top](#welcome)

## Deployment
  This project was developed using GitPod. The web application is deployed on Heroku. All Static and media files are stored via Amazon AWS S3. The repository is hosted on GitHub.

[Goto Top](#welcome)

### Clone GitHub Repository

  By Cloning a GitHub repository you can create a local copy of a GitHub remote repository.
  Cloning is done via the following steps

  - 1. Login to GitHub
  - 2. Navigate to the main GitHub repository that you want to clone
  - 3. Click on the green dropdown button Code
  - 4. To clone the repository using HTTPS under HTTPS copy the link
  - 5. Open command prompt
  - 6. Change to the directory you want to create the repository in
  - 7. Type git clone and paste the URL you copied in step 4.
    ``` $ git clone https://github.com/your-username/your-repository```
  - 8. Press enter. Your local copy of the repository will be created

For this project GitPod IDE was used so I just had to create a workspace and connect to GitHub by choosing the repository.
Once the workspace opened in GitPod 

To install the dependencies from the command line in GitPod
pip3 install -r requirements.txt

I setup an env.py file with the following constants
```
import os

os.environ.setdefault('STRIPE_PUBLIC_KEY', '<the key>')

os.environ.setdefault('STRIPE_SECRET_KEY', '<secret key>')

os.environ.setdefault('SECRET_KEY', '<secret key>')

os.environ.setdefault("STRIPE_WH_SECRET", "<stripe key>")

os.environ.setdefault("DEVELOPMENT", "True")
```

 Note: for the STRIP_WH_SECRET an endpoint had to be created https://<host_url>/checkout/wh/
 navigate to webhooks and click on you link and reveal signing secret and copy this into STRIP_WH_SECRET

Make migrations and setup initial database operations
on the CLI in GitPod enter python3 manage.py makemigrations
then
python3 manage.py migrate

To setup the categories and products copy over the media file and run
python3 manage.py loaddata categories
python3 manage.py loaddata products

Then I created a superuser by entering
python3 manage.py createsupreruser

[Goto Top](#welcome)

### Deployment on Heroku

This project uses Heroku for production and static and media files are stored via a bucket on Amazon AWS S3. To deploy on Heroku

  - 1. Naviage to heroku.com and login and create new app for your project and set the region and click on create app.
  - 2. Connect Heroku app to github repository 
  - 3. Configure variables on Heroku by navigating to settings and click on Revela Config Vars 

Variable | Key
--- | ---
AWS_ACCESS_KEY_ID | Access key for AWS 
AWS_SECRET_ACCESS_KEY | secret key for AWS 
DATABASE_URL | database url got from code institute 
EMAIL_HOST_PASS | password for email sender 
EMAIL_HOST_USER | email address used 
PORT | 8000 
SECRET_KEY | Django secrey key 
STRIPE_PUBLIC_KEY | stripe public key 
STRIPE_SECRET_KEY | stripe secret key 
STRIPE_WH_SECRET | stripe webhook secret key 
USE_AWS | True 

  - 4. Then create a Procfile with contents
  web: gunicorn fitness_fanatic.wsgi:application

  - 5. add hostname of heroku app to allowed hosts in settings.py

  I have setup the debug to be true if the DEVELOPMENT is found in the environment variables which will be true for localhost.

  - 6. on Heroku under deply for your app click Deploy Branch to deploy your app

[Goto Top](#welcome)

### Amazon AWS S3

This project uses Amazon Web Servies (AWS https://aws.amazon.com/) to store static and media files.

Once youve created an AWS account and logged in. You can follow the following steps to setup your static and media files storage.

From the AWS Management Console.

  - Search for S3
  - Create a new bucket, give it a name matching your Heroku app name and choose a region closest to you
  - Uncheck Block all public access and acknowledge that the bucket will be public.
  - From Object ownership make sure ACLs are enabled and Bucket owner preferred is selected
  - From the Permisssions tab paste in the following CORS configuration

  ```
    [
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
  ```

  - Copy your ARN string
  - From the Bucket Policy tab, select the Policy Generator link and set
    - Policy type: S3 Bucket Policy
    - Effect: Allow
    - Principal *
    - Actions: GetObject()
    - Amazon Resource Name (ARN): paste your ARN here
    - Click add Statement
    - Click Generate Policy
    - Copy entire Policy and paste it into the Bucket Policy editor

    ```
    {
    "Version": "2012-10-17",
    "Id": "Policy1726973504037",
    "Statement": [
        {
            "Sid": "Stmt1726973489892",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucket name/*"
        }
    ]
    }
    ```
    
    - Click save
    - From the Access Control List (ACL) section click edit and enable List for Everyone (public access) and accept the warning box.

### IAM
  Back on the AWS service menu, search for IAM (Identity and access management). Once on the IAM page

  - From User Groups click Create New Group
  - From User Groups, select newly created group and go to the permissions tab
  - Open the Add Permissions dropdown and click on Attach Policies
  - select the policy then click on Add Permissions at the bottom
  - From the JSON tab select Import Managed Policy link
    - Search for S3 select AmazonS3FullAccess policy and import
    
    ```
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::bucket name",
                "arn:aws:s3:::bucket name/*"
            ]
        }
    ]
    }
    ```

    - Click Review Policy
    - Provide a description a brief overview of what it for
    - Click Create Policy 

  - From User Groups click on group created
  - Click Attach Policy
  - Search for ther policy youve just created select it and click on Attach Policy
  - From User Groups click Add User
  - From Select AWS access type select Programmatic Access
  - Select the group to add to your user (created above)
  - Click Create User
  - under the User Summary on the right click on Create Access Key
    - set AWS_ACCESS_KEY_ID = Access Key ID
    - AWS_SECRET_ACCESS_KEY = Secret Access Key
  
### Final Setup
  - Back within S3 buckets create folder media
  - copy over existing media files to this folder
  - Under Manage Public Permisssions select Grant public read access to this object

[Goto Top](#welcome)

## Credits

I would like to thank Code Institute and the Tutoring team aswell as the mentors for their support throughout this course.

I would also like to thank freepik.com (https://www.freepik.com/) for the images used. I would also like to thank York Fitness (https://yorkfitness.com/) as being the supplier for the equipment and the images are got from their website for this!!

