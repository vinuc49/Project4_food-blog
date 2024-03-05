<h1 align="center">Namaste</h1>
<div align="center"><img src="docs/img/responsive image.png"></div>

Food Blog is a web application built using the Django framework, designed to create an engaging and user-friendly platform for food enthusiasts to share, discover, and interact with a diverse range of recipes. Whether you're a food enthusiast sharing recipes or a home cook looking for new ideas, food blog is the perfect platform to connect and explore the world of flavors. 


You can view the live site here - <a href="https://project4-food-blog-5db6aef86fa9.herokuapp.com/" target="_blank" rel="noopener">Food Blog</a>

## **[Repository](https://github.com/vinuc49/Project4_food-blog)**

# User Experience

### **User Stories**

#### **Site User**
- As a user I can view a paginated list of recipes so that I can pick one to read
- As a user I can view a selection of random recipes so that I can pick and read the one I like
- As a user I can click on a recipe so that I can read the whole recipe
- As a user I can view the comments on individual recipes so that I can read other user's opinions on recipes
- As a user I can register for an account so that I can interact with content and post recipes
- As a user I can view and select a category of recipes so that I can view recipes in category
- As a user I can search the recipes by keyword so that find relative recipes
- As a user I can view the number of likes so that I can see which recipe is most popular
- As a user I can view other people cookbooks so that I can get ideas

#### **Registered User**
- As a registered user I can post a comment on a recipe so that I can be involved in the conversation
- As a registered user I can like/unlike the recipes so that I can interact with the content
- As a registered user I can login so that I can access my content
- As a registered user I can logout so that other users cannot access my account
- As a registered user I can access my profile so that I can edit my details and upload a profile image
- As a registered user I can delete my comments so that the comments are no longer visible
- As a registered user I can edit my comments so that I can update my comments


#### **Site Admin**
- As a site admin I can approve/disapprove the comments so that I can decide if the content is relevant
- As a site admin I can create, read, update, and delete recipes so that I can manage my content
- As a site admin I can delete or update user's comments so that I can manage my content
- As a site admin I can delete or update user's cookbooks so that I can manage my content
- As a site admin I can create draft recipes so that I can finish writing the content later
- As a site admin I can create, update and delete categories so that I can manage my blog content


#### **Testing User Stories**



### Agile Methodology

- GitHub Projects were uset to create kanban board, and Issues were used to create User Stories and Epics which helped me move through the project and organize tasks. 

- Using GitHub Issues, I was also documenting bugs in order to make sure that they are not forgotten. 

- User Stories were organized in Epics which helped me to build the project section by section. 

- Agile Methodology and GitHub Projects helped me a lot in organizing my own work on this project, but I still very often found myself adjusting and adding User stories.  

Link to GitHub Project can be found [here](https://github.com/vinuc49/Project4_food-blog)


# Features

## Existing Features


### Nav-bar and Logo

- this feature is present throughout entire project except on a page where user is prompt to define his profile role for using the app, and since the incentive is to pick the role as its vital part of a user functionality of the web app I decided to not incude this feature in this part of the project.

- page logo is also a link to home page. Other than that, navbar consists of links to: Home and Register/Login.

- authenticated user has his username visible on the navbar which is a link to profile page.

- unauthenticated user can see links to Register/Login instead of username.


![Nav-bar](/docs/img/nav-bar.png)

### Home Page

- this feature contains the carousel for aesthetis, and top recipes. The Carousel is present throughout the whole project.

- Top recipes are listed based on number of likes. This way users are able to see few best recipes straight away. 

- Users are also able to see recipe card that contains number of likes and comments. 

![Home Page](/docs/img/home-page.png)

### Footer 

- This feature contains Contact information and copyright.

- This feature present throughout the whole project

![Footer](/docs/img/footer.png)


## Full Blog Post Page

![full-post-img](/docs/img/full-post.png)

When a user clicks on a link to open a post fully, they are greeted with a fully formatted, traditonal blog post layout. The blog title is displayed in a large header tag at the top of the page, with further information stating the author and when the post was created/last updated.

As blogs have to be approved by the admin before publication, this helps to ensure the content being shared is relevant to the sites purpose and that the quality of the posts are up to the standard that the site admin would like. Adding to that, it is a much easier way to monitor posts rather than having to manually scroll through every published blog and pick out any for editing or deletion incase of a error or misuse of the platform.

Directly under the blog content, is a like button and a section containing the comments. Here it once again shows the number of likes the post, but this time also with the ability to like the post yourself. You can click the like button only if you are signed in. If not, there is a comment explaining this and a link that will take you to the 'Register for an account' page.

The same applies as above for the comments section. Any comments the post has received already are displayed here, along with the name of the user and the date it was made. If you are a signed in user, you can click the 'Add comment' button and be taken to the page where you can leave comments.

![full-post-comments-img](/docs/img/comment.png)

# Languages/Libraries Used

- Django
- Python
- HTML/CSS
- Bootstrap
- Cloudinary
- AllAuth Authentication
- Summernote Text Editor

This project was built primarily using Django and Python languages. HTML was also used throughout to implement numerous different webpages. The majority of styling throughout the site was done using Bootstrap classes, but to customise these further I implemented my own custom CSS styling to overwrite some of the more standard bootstrap style classes.

I used Cloudinary for some of the image file storage. This is because Django uses an ephemeral file system, so Cloudinary was a good choice to prevent my image files from being deleted after a certain amount of time has passed. For other image files, I used standard static file storage in my Gitpod workspace.

As stated earlier in this read-me, Django's own AllAuth authentication system was used in this project for signing in, signing out and registering an account. In order to customise the already created HTML files I had to input the following command into my terminal to copy the files and save them in my own workspace - 
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates

 Deployment

## Local Deployment

The points below outline the steps that I took to deploy my project to a local server - 

* Create a new GitHub repository 
* Select the Code-Institute-Full-Template and name your repository
* Press the Gitpod button to open a new Gitpod workspace
* Download all the required dependencies. Django, Psycopg2, gunicorn etc
* Create a requirements.txt file using command pip3 freeze --local > requirements.txt
* Create a new Django project using command django-admin startproject "project-name-here" .
* Create a new app using command python3 manage.py startapp "app-name-here"
* Add the above app name to list of installed apps in settings.py file
* Migrate these changes using command python3 manage.py migrate
* Run the project using command python3 manage.py runserver
* The project should now be running locally on port 8000

## Live Deployment

The steps outlined below, document the steps taken to deploy my live project to Heroku

* On GitHub, I forked my repository so it is not deleted after inactivity
* Navigate to Heroku.com, sign into your account and create a new app 
* I named my app PROJECT4_food-blog and picked the European region
* Go to the Resources tab, search for PostGres and confirm 
* Submit the order to confirm you want to use the PostGres database
* Create an env.py file on top level of your file system
* Import os to env.py file and copy your database-url from heroku config vars
* Create your variables in the env.py file - os.environ.get['DATABASE_URL'] = 'copied url from heroku'
* Create your own secret_key variable and add to env.py as outlined above
* Add secret_key value to config vars on heroku
* Navigate to settings.py file
* import os & dj_database_url
* Also add - if os.path.isfile(env.py): import env
* Replace secret variable on settings.py with os.environ.get('secret_key')
* Comment out databases section on settings.py and replace with 
DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL))}
* You're now using Postgres database on the backend
* Migrate changes the same way as outlined above
* Add PORT and value 8000 to heroku config vars
* In settings.py file, add code TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* In TEMPLATES - DIRS add the value [TEMPLATES_DIR]
* In ALLOWED_HOSTS add ["'app-name-here'.herokuapp.com", 'localhost']
* Create a procfile on top level of your file system
* Add code to procfile - web:gunicorn 'app-name-here'.wsgi
* Commit and push changes to Github
* Navigate to Deploy tab on heroku
* Connect to your GitHub account and type your repository name 
* Click deploy and your project should now be live

The link to my live website can be found at - https://project4-food-blog-5db6aef86fa9.herokuapp.com/

# Testing

## Manual Testing

Throughout the development, manual testing has been carried out by myself and also by my friends and family to document any bugs in the code. 

* All the code has been put through the appropriate validators
* Tested using Safari, Chrome and Firefox
* Blog posts have been created on multiple different devices
* Editing and deletions of blog posts have also been tested on different devices
* Comments have been posted by myself and others throughout development 
* Commenting has been tested on different devices to ensure it works as expected 
* The ability to like/unlike a post has been tried and tested on different devices and screen sizes

If statements were used quite extensively throughout the project, to ensure only the correct user can perform certain actions. These are outlined in more detail below - 
- The statement that ensures only logged in users can like and comment on posts is working as expected
- The if statement that checks to see if you are signed in before you can create a post has been tested and works as expected.
- Only the author of the post and the site admin can make any edits or deletions pertaining to that specific blog post works as expected.
- If an unauthorised user stumbles upon a webpage they should not have access to, an erro page displays as expected linking them back to the appropriate section of the website.

The authentication system has been tested appropriately to ensure - 
- You can sign in and out without any errors
- When you register for an account, it works as expected and doesn't throw any errors
- The same username cannot be used more than once


## **Acknowledgments**

- I would like to thank my Code Institute mentor for his support and feedback throughout this project.
- I would like to thank my spouse for her understanding, patience, and support while I developed this project.
- I would like to thank to Code Institute tutors. Developing this project I used tutors support a lot. Thanks a million, guys, for your patience, attention, help, and support. 