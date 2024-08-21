![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
=============================================================================================================================================================================================

# Welcome

# Project Research and Preparation

## Fitness Fanatic

Fitness Fanatic is a fictional website designed specifically for Code Institute for Project number 5 which is an e-commerce website. This site is all about training where you can buy fitness programs which go on for several weeks at several days a week. Or you can purchase basic fitness equipment for home use. The fictional workout programs are given in a fictional training location in person at say Fitness Fanatic Bridgewater Arklow. I chose the location Arklow as its where I live and for this type of business there is a lot of local competition in the local area.

On the site you can purchase equipment.

On the site you can purchase a training workout program which is several days a week for several weeks.

On the site you can edit your profile once logged in.

On the site a user can update their password. This is in the admin dropdown once logged in you just click on a link and a allauth template is opened which updates the password.

On the site the administrator can add trainers, delete trainers and edit trainers.

On the site the trainers can edit their profile (It should be noted that the trainer profile is different from the user profile as it allows a trainer if they want to purchase items from the center through the normal purchase workflow).

On the site a trainer can create, edit and delete workout programs given by them once logged in as a trainer.

On the site a trainer once logged in can view their mail where a user can contact them through a trainer contact form. This is done through a database table and the trainer contact template shows the trainer their email/(entries in the database table) where the new email is shown in bold and once marked as read will display as normal text. This is just a text based dump of the table info with a mark as read button. Once marked as read the read BooleanField in the table is marked as True. In this template it is hoped that it can be viewed by not read and year. For this project the entries wont be deleted as a paper trail would be needed for management.

On the site web admin can be contacted through a contact form which can be viewed via site admins in the Django site admin interface.

On the site a user can view trainer profiles and workout programmes given by each trainer.

On the site a trainer can administer their classes via an attendance form where it shows a list of students which purchased the course and a checkbox to say they attended at the date the form is opened and a button to submit the form.

If time permits I will have typical training workout programmes like the Skogg kettlebell system, RKS kettlebell system, for weight training the Body Beast workout program, Suspension training program, Scientific stretching program. These programs will be broken down into what is covered over the duration of the course. This information will be a template link on the trainers profile template page. Where if a user is interested in a program they can read about it here.


### Categories

1. name: freeweights, friendly_name: Free Weights
2. name: kettlebells, friendly_name: Kettlebells
3. name: spinning, friendly_name: Spinning
4. name: yogamats, friendly_name: Yoga Mats
5. name: clearance, friendly_name: Clearance
6. name: new_arrivals, friendly_name: New Arrivals
7. name: workoutprograms, friendly_name: Workout Programs

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

