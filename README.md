![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome

# Project Research and Preparation

## Fitness Fanatic

Fitness Fanatic is a fictional website designed specifically for Code Institute for Project number 5 which is an e-commerce website. This site is all about training where you can buy fitness programs which go on for several weeks at several days a week. Or you can purchase basic fitness equipment for home use. The fictional workout programs are given in a fictional training location in person at say Fitness Fanatic Bridgewater Arklow. I chose the location Arklow as its where I live and for this type of business there is a lot of local competition in the local area.

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

![Home Landing Page of site](/readme_images/home_landing_page.png)

### Categories

1. name: freeweights, friendly_name: Free Weights
2. name: kettlebells, friendly_name: Kettlebells
3. name: spinning, friendly_name: Spinning
4. name: yogamats, friendly_name: Yoga Mats
5. name: clearance, friendly_name: Clearance
6. name: new_arrivals, friendly_name: New Arrivals
7. name: workoutprograms, friendly_name: Workout Programs

## Site Testing

A sererate README_TESTING.md file was used for testing and can be found [testing readme here](README_TESTING.md) . In this file I explain testing workflows.

## E-Commerce Business Model

Fitness Fanatic is a B2C type application. The site is focused at local employment. Where the classes are held in a local training center at about 15 people per class.

## Marketing Strategies

Fitness Fanatic is a local training center offering the purchase of various small type training equipment for home use. But the site also allows the customers to enroll on courses held at the local center where class sizes are small (typically 15). The site also allows the site administrator to manage trainers where a trainer could be a per workout program given hire (type kinda freelance). The trainer would register with admin and via a form setup their profile and then once registered, they can begin creating workout programs for several weeks at a time.

The offering for workout programs vary from the Body Beast program to the RKS Kettlebell System to the Skogg Kettlebell system to Spinning to Scientific Stretching. These are small offerings but are varied and interesting courses which would typically go on for an hour.

Marketing is done on customer satisfaction where they would use word of mouth to spread the word about a cool training program. At Fitness Fanatic a Facebook webpage was also setup to spread the word about the training programs on offer ![Facebook Page]()


## Entity Relationship Diagram

![Fitness Fanatic ERD](/readme_images/fitness_fanatic_erd.png)

## Wireframes

### About

![About](/readme_images/about.png)

### Bag

![bag](/readme_images/bag.png)

### Checkout

![Checkout](/readme_images/checkout.png)

### Contact Trainers

![Contact Trainers](/readme_images/contact_trainers.png)

### Home Page/ Landing Page

![Home Page](/readme_images/home_page.png)

### Product new arrivals

![Product new arrivals](/readme_images/products_category_new_arrivals.png)

### Product workout programs

![Product workout programs](/readme_images/Products_category_workoutprograms.png)

### Products

![Products](/readme_images/products.png)

### Trainer Class Admin

![Trainer Class Admin](/readme_images/trainer_class_admin.png)

### Trainer Profile

![Trainer Profile](/readme_images/trainer_profile.png)

### Trainers Add Workout Program

![Trainers Add Workout Program](/readme_images/trainers_add_workout_program.png)

### Trainers

![Trainers](/readme_images/trainers.png)

### User Profile

![User Profile](/readme_images/user_profile.png)

### Admin Add Trainer

![Admin Add Trainer](/readme_images/add_trainer.png)

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


## UX Colour Palette

## Images

This is the initial plan for images. I may need to edit and resize the images, but lets get MVP working and see!!.

- The background image for the Home Landing page

![Home page background](/readme_images/website_images/young-fitness-man-studio.jpg)

<a href="https://www.freepik.com/free-photo/young-fitness-man-studio_8990574.htm#fromView=search&page=1&position=3&uuid=edf2a89b-a38c-4ecb-88c4-7aff10e1119e">Image by serhii_bobyk on Freepik</a>

- Weights

  ![York Weight set 55Kg](/readme_images/website_images/weights.webp) has size = false

  price 160 Euro

  ![York Wight set 70Kg](/readme_images/website_images/weights_70kg.webp) has size = false

  clearance

  price 180 Euro

- Kettlebells

  ![York Kettlebell](/readme_images/website_images/Kettlebell.webp) has size = true

  price 45 Euro

  ![York plastic handle Kettlebell](/readme_images/website_images/new_arrivals_kettlebell.webp) has size = true

  new_arrivals

  price 20 Euro

- Spinning

  ![York Spin Bike](/readme_images/website_images/Sping_bike.webp) has size = false

  price 600 Euro

- Yoga

  ![York Yoga Mat](/readme_images/website_images/Yoga_mat.webp) has size = false

  price 30 Euro

- Trainers

  - Trainer 1 Image

    ![Trainer 1 image](/readme_images/website_images/Trainer_1.jpg)

    <a href="https://www.freepik.com/free-photo/person-sport-gym-using-kettlebells_22271433.htm#fromView=search&page=1&position=52&uuid=288aaa53-0f86-46f9-a8f4-1f291ba28be3">Image by freepik</a>

  - Trainer 2

    ![Trainer 2 image](/readme_images/website_images/Trainer_2.jpg)

    <a href="https://www.freepik.com/free-ai-image/athletic-person-exercising-working-out_94957668.htm#fromView=search&page=1&position=21&uuid=34773477-4b25-4b4d-b8d4-a5758dbec8db">Image by freepik</a>

  - Trainer 3

    ![Trainer 3 image](/readme_images/website_images/Trainer_3.jpg)

    <a href="https://www.freepik.com/free-photo/person-doing-indoor-cycling_22632032.htm#fromView=search&page=1&position=2&uuid=cad0d75b-332c-4fc4-aa68-5225cc5aba13">Image by freepik</a>

- Workout Programs

  - Skogg Kettlebells System

    ![Skogg Kettlebell System](/readme_images/website_images/skogg_kettlebell_system.jpg)

    <a href="https://www.freepik.com/free-photo/sportive-guy-training-with-kettlebell-photo-handsome-man-with-good-physique-strength-motivation_16179732.htm#fromView=search&page=1&position=18&uuid=5150ab8d-0760-4e19-be73-da257224826d">Image by teksomolika on Freepik</a>


  - RKS Kettlebell System

    ![RKS Kettlebell System](/readme_images/website_images/rks_kettlebell_workout.jpg)

    <a href="https://www.freepik.com/free-photo/person-sport-gym-using-kettlebells_22271411.htm#fromView=search&page=2&position=48&uuid=c71a9934-d41e-45d2-a141-99ca8215e10a">Image by freepik</a>

  - Body Beast Program

    ![Body Beast](/readme_images/website_images/Trainer_2.jpg)

    <a href="https://www.freepik.com/free-ai-image/athletic-person-exercising-working-out_94957668.htm#fromView=search&page=1&position=21&uuid=34773477-4b25-4b4d-b8d4-a5758dbec8db">Image by freepik</a>

  - Suspension Training Program

    ![Suspension Training Program](/readme_images/website_images/suspension_training.jpg)

    <a href="https://www.freepik.com/free-photo/young-woman-training-gym_10445545.htm#fromView=search&page=1&position=30&uuid=fcbf134b-85ab-4c96-8214-c56df3bd5271">Image by Racool_studio on Freepik</a>

  - Scientific Stretching Program

    ![Scientific Stretching](/readme_images/website_images/scientific_stretching.jpg)

    <a href="https://www.freepik.com/free-photo/female-athlete-doing-relaxation-exercises-while-practicing-home_26265868.htm#fromView=search&page=1&position=1&uuid=8f94638c-f232-4656-8ccb-e064bc50daa0">Image by Drazen Zigic on Freepik</a>

## Credits

I would like to thank Code Institute and the Tutoring team aswell as the mentors for their support throughout this course.

I would also like to thank freepik.com (https://www.freepik.com/) for the images used. I would also like to thank York Fitness (https://yorkfitness.com/) as being the supplier for the equipment and the images are got from their website for this!!

