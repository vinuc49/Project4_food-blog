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
