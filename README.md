# ManCrazeShoes

# Introduction

Welcome to the [ManCrazeShoes](https://mancrazeshoes-4c1185db9ef9.herokuapp.com/). This is the documentation for my e-commerce web application: Mancrazeshoes. It has been built using Django, Python, JavaScript, CSS3 & HTML5 for educational purposes as part of Code Institute’s Diploma in Web Application Development Course.

[You can see the live project here](https://mancrazeshoes-4c1185db9ef9.herokuapp.com/)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720508580/mock-up_aav1d8.png)

## [Table of Contents](#table-of-contents)

- [User Experience](#user-experience)
  - [Website goal](#website-goal)
  - [Scope](#scope)
  - [User Stories](#user-stories)
   
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Database Schema](#database-schema)
  - [Fonts](#fonts)
  - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
    - [Overview](#overview)
    - [EPICS(Milestones)](#epics(milestones))
    - [User Stories issues](#user-stories-issues)
    - [MoSCoW prioritization](#moscow-prioritization)
    - [GitHub Projects](#github-projects)
- [Features](#features)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Home](#home)
        - [Hero Section](#hero-section)
        - [Recent Items](#recent-items)
    - [Product Page](#product-page)
        - [Product Card](#product-card)
        - [Single Product Page](#single-product-page)
    - [My Profile Page](#my-profile-page)
    - [Product Management](#product-management)
    - [Shopping bag](#shopping-bag)
    - [Checkout](#checkout)
        - [Order Confirmation Page](#order-confirmation-page)
    - [User Authentication](#user-authentication)
- [Future Features](#future-features)
- [Marketing](#marketing)
- [Search Engine Optimization SEO](#search-engine-optimization-seo-and-marketing)
- [Testing](#testing)
- [Technologies And Languages](#technologies-and-languages)
    - [Languages Used](#languages-used)
    - [Python Modules](#python-modules)
    - [Technologies and programs](#technologies-and-programs)
- [Deployment](#deployment)
    - [Deploy on Heroku](#deploy-on-heroku)
    - [Fork the repository](#fork-the-repository)
    - [Clone the repository](#clone-the-repository)
- [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    - [Comments](#comments)
            

## User Experience

### Website goal

- To provide users with a place to purchase shoes for men of their interest.
- To provide the users the ability to search and browse shoes of different categories.
- To provide the users with the ability to save shoes to their wishlist
- To provide the users with the ability to check their order history.
- To provide the users with the most recents shoes from the company.

### Scope

This project seeks to create an e-commerce platform dedicated to providing customers with a wide selection of shoes for men. 

- Create an account and log in securely.
- Reset their password if necessary.
- Browse, search, and filter through available shoes.
- View product stock levels
- Add desired shoes to their shopping cart.
- Adjust quantities within their shopping cart.
- Remove items from their shopping cart as needed.
- Save products to wishlist
- Update personal information
- View past orders
- Safely complete transactions using the integrated Stripe payment system.
- Access a comprehensive overview of past orders for reference and tracking purposes.

Key Features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design: -The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:

- Users can register an account, providing access to all functionality of ManCrazeShoes.
- Registered users can log in to view their profile and orders.

4. Order Management and Checkout:

- Users can add items to their shopping cart.
- The shopping cart allows users to update item quantities or remove products.
- Secure checkout process ensures safe payment transactions..

5. Admin Features:
- Admin dashboard provides a product overview and order summary.
- Admins can add, delete, or modify products.
- Stock levels and product details can be edited by admins.
- Order status can be updated by admins.

6. Notification Messages:

- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

#### Benefits:

- User-Centric Approach: The platform prioritizes user needs, facilitating efficient browsing and purchasing.
- Streamlined Navigation: Users can effortlessly navigate between website sections for enhanced accessibility.
- Enhanced Communication: Email and notification features improve user engagement.

### User Stories

1. As a developer I can set up a new Django project so that I can create the project's structure
2. As a developer I can connect database and media storage so that the user's stored data is stored successfully
3. As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development
4. As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile
5. As a user I want the website to be responsive so I can view it on my mobile
6. As a user I want to be able to register an account so that I can have access to all functionality of the website.
7. As a registered user I want to be able to log in to my account so I can view my profile page and my orders.
8. As a registered user I want to be able to see my profile page so that I can update my information
9. As a User I want to be able to view detailed information about a product's description,price and size.
10. As a User I want to be able to search for product categories in the website by entering keywords so that I can quickly find specific items or topics of interest.
11. As a registered user I want to be able to reset my password so that I can regain access to my account in case I forget my password.
12. As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase.
13. As a registered user I want to be able to edit the cart so that I can control the quantity of items I want to purchase.
14. As a registered user I want to be able to remove the items from the cart so that it is not available for other users.
15. As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases on Mencrazeshoes with confidence..
16. As a authenticated user, I want to be able to save shoes to my wishlist so that I can revisit and consider purchasing them later on.
17. As an administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders made on this site.
18. As an administrator, I want to be able to add new products to the website so that I can expand the product catalog
19. As an administrator, I want to be able to edit existing products on the website so that I can update and manage the product catalog.
20. As an administrator, I want to be able to remove products from the website so that I can manage the product catalog.
21. As a User I want to be able to complete the checkout process for my shopping cart so that I can purchase the items I've added to my cart.

[Back to Table of contents](#table-of-contents)

## Design

### Colour Scheme
In this website mainly used black and white combinations. For login,sign up forms and buttons used light blue colors. For product container used grey color and yellow color for selected shoe size.

The below colours are the main colours.
-  #fff
-  #333
-  #f2f2f2
-  #ffd700;
- aquamarine

### Database Schema

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715736668/database-schema_svcmsn.png)

1. User: The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the UserProfile model with one to one relationship.

2. UserProfile: The UserProfile model is a custom custom-created model to handle the user profile details. Signals are used to reflect the changes between the User and UserProfile models.

3. Category: This model was created for the purpose of defining categories for the products

4. Product: This is a custom product model. It is connected to Genre.

5. Order: This model holds all the information of the user's order. It is connected to the UserProfile as a ForeignKey.

6. OrderLineItem This model is connected to the Order and Product as a ForeignKey. It is created for each item in the order
7. ProductVariant: This model is connected with shoe size and stock for each size.
8. Wishlist: This model stores the products to a wishlist for authenticated users. It is connected to UserProfile as a ForeignKeyand Products models as a manytomanyfield

### Fonts

In addition to Bootstrap 4 built in font family the below two fonts were used throughout the application

Poppins
Indie Flower

[Back to Table of contents](#table-of-contents)

### Wireframes

- Home
<details>
  <summary>Home</summary> 
    <img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715766033/wireframe-home_jirs0t.png">   
</details>

- Product
<details>
  <summary>Product</summary> 
  <img src ="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715766033/wireframe-product_po4b1y.png">
</details>

### Agile Methodology

#### Overview

This project was created using agile principles. As this is my second full-stack project, using agile, it was easier to identify the relevant milestones. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### Epics(Milestones)

The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715769834/epic-milestone_qjbw1o.png)

#### User Stories Issues

The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. During development where possible, the commit messages are connected to their corresponding issues.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715770270/user-stories1_jfo3yf.png)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715770270/user-stories2_vfusbh.png)

#### MoSCoW prioritization

This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715770543/mosco_itcuti.png)

#### GitHub Projects

The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715770719/github-project_lrpvxe.png)

## Features

### Navbar

The navbar was built using bootstrap 4 and it is fully responsive. The search bar allows the users to search for products by keywords from any page of the website. The My Account drop down gives the user the option to log in or sign up. If the user is authenticated additional menu options are displayed like my profile and Product Management (if the user is a superuser). The shopping bag icon is a link to the shopping bag and it also displays the total of the items in the bag. The nav links allow the user to refine the products by category, price and new arrivals. There is a dropdown for shoes which allows the user to see the formal and casual shoes.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715772856/navbar-desktop_wvjktt.png)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720509064/navbar-mobile_obwnl9.png)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720509064/navbar-mobile1_hsmu4f.png)

### Toasts

Toasts from Bootstrap were implemented to provide customers with feedback regarding their actions on the website.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715773676/toast_spon3d.png)

### Footer

The footer consist of links to social media links, help and shop by.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720509349/footer-desktop_oozwa4.png)

- mobile view

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720509349/footer-mobile_p1ntxx.png)

### Home

#### Hero Section

The hero section is the beginning of the whole customer's journey. That is why I made it a priority to create appealing hero section. The text on the left side communicates about the new collections and right side I used carousel with 3 shoe photos.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720509503/hero-section_kfpkzp.png)

#### Recent Items

The products displayed on the home page are the most recently added 6 products.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715774753/recent-items_hr5m56.png)

[Back to Table of contents](#table-of-contents)

### Product Page

The all product page renders all products to the user. They have the option to sort the products by category and price. If we want we can select by category like formal, casual and sandals. And there is small button on the right bottom to go to the top.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643939/product-page_ieex1y.png)

#### Product Card

The product card consist of an image of the shoe, price, name and heart button for wishlist. When we click on the image it goes to the product details page.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643565/product-card_ab3vec.png)

#### Single Products Page

On the page's left side, a product image is displayed. On the right side, the most important information about the product is displayed. This includes the name, price, description, shoe size, stock details display on the right side of the size, if there is no stock customer cant click on that size and add to cart button with quantity dropdown. 
Implementing stock levels in the product model, allowed for adding custom logic when it comes to adding items to the shopping bag. The user should not be able to add to their cart a higher quantity(5 maximum).

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727642252/single-product-page_nhcwbe.png)

### My Profile Page

This section is accessible only to registered users. This section contains two sections. left side- my profile and right side - my orders

- Profile

This page renders a form for the user's address and phone number. If the user has any details saved, it renders prefilled.

- Order History

This page displays the past orders of this user.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715778176/profile-order_pkxlme.png)

- Wishlist

This page displays the wishlist items added

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643056/wishlist_cgdquj.png)


### Product Management

This section can be accessed only by admin or superuser. This section allows admins to add, edit and delete shoes without the need of the built in Django admin.

- Products view for super user

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643056/admin-product-view_xre3wy.png)

- single product view for super user

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643056/admin-product-view1_erg4np.png)

#### Add Products

This page renders the product creation form and all required fields to add an item to the database. 

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643300/add-product_x6zppo.png)

#### Edit Product

This page renders the product form prefilled with the existing data in the database. It allows the admin to modify the details of the products.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643300/edit-product_etw0q0.png)

#### Delete review confirmation

It allows the admin to delete the details of the products.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1727643056/delete-product_wbgiib.png)

[Back to Table of contents](#table-of-contents)

#### Shopping bag

The shopping bag can be accessed from the main nav menu. The shopping bag table section provides a clear and organized representation of the items added to the shopping bag. Each item has a small image, name, size, price, quantity, and subtotal. The users can upgrade the quantity or delete items from the cart with the help of the buttons provided. On the bottom right side displays the bag total, delivery charges, and grand total.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715791580/shopping-bag_ucginn.png)

#### Checkout

This page contains a form for the user's delivery and payment information and a summary of the user's order. If the user has an account, they can save their delivery information on their profile to automatically be filled in the checkout.

The checkout Form In the checkout the user can add their details and if they're logged in, can check the box to save their details for future transactions. Users must enter their payment information before completing the checkout and all payments are handled via Stripe.

Order summary A final summary of the user's order is shown containing all the user's basket items, quantity and subtotal for each item. The user can also see their bag total, delivery costs and the grand total in the summary.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715792268/checkout_hvysl3.png)

#### Order confirmation page

After the order has been completed, the user is redirected to a confirmation page containing a final rundown of the order and what the user purchased. This page can be accessed again from the user's profile if they have an account on the site by clicking the order number from the list of past orders.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715792504/checkout-confirmation_tljixh.png)

### User Authentication

The website uses django allauth's built in functionality which allows the users to register and log in securely. There is also a reset password functionality which allows the user to input their email address and recieve a link where they can securely reset their password.

- login form

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715793054/login_k0g7oi.png)

- Sign up form

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715793054/signup_aai1gy.png)

[Back to Table of contents](#table-of-contents)

## Future Features

- Add stock details which can be updated by the admin.
- Add reviews, customer can add, edit and delete their reviews.
- Add wishlist, so user can see their wishlist when they login next time.
- Add send email to confirmation to customers when they order confirmed.

## Marketing

### Search Engine Optimization SEO and Marketing

#### Business Model

The B2C (Business-to-Consumer) ecommerce model for this online shoeshop operates as a platform catering to individual consumers looking to purchase a wide variety of shoes conveniently from their place. This model revolves around offering a selection of styles, ranging from casual, formal and sandals providing an accessible and user-friendly interface for browsing, selecting, purchasing, and receiving shoes.

The target customers for this online shoeshop encompass diverse demographics, including fashion-conscious individuals, athletes, professionals, and anyone in need of quality footwear for various occasions. The business aims to attract shoe enthusiasts seeking convenience, variety, competitive pricing, and an engaging shopping experience.

### SEO

- Enhancements have been implemented for the main template, including the addition of descriptive meta tags such as title, description, and keywords. 
- An XML sitemap was generated using a sitemap generator based on the deployed website, and this file is included at the root level of the project. 
- Additionally, a robots.txt file was created at the root level of the project to guide search engine crawlers on which URLs they can access on the website.

### Marketing

- Newsletter is included in the home page. This section facilitates user engagement and promotes the e-commerce store through effective email marketing and social media presence.

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720510743/newsletter_dewcjn.png)

- Facebook Page

[ManCrazeshoes](https://www.facebook.com/profile.php?id=61562444031840)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720510790/facebook-page_m6mtt3.png)


## Testing
Testing documentation can be found [here](TESTING.md).

## Technologies And Languages

### Languages Used
  - HTML
  - CSS
  - JavaScript
  - jQuery
  - Bootstrap
  - Python
  - Django
### Python Modules
  - dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

  - django-storages - Django Storages is a collection of custom storage backends for Django, including support for storing files on remote services like Cloudinary.

  - django-widget-tweaks - Django Widget Tweaks is a package that simplifies working with form widgets and templates in Django

  - gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

  - Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

  - psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

### Technologies and programs

  - Favicon Generator was used to generate Favicon
  - GitHub is the hosting site used to store the code for the website.
  - Git was used as a version control software to commit and push the code to the GitHub repository.
  - Heroku - used for deploying the project
  - Font Awesome - for creating atractive UX with icons
  - Bootstrap4 - for adding predifined styled elements and creating responsiveness
  - LightHouse - for testing performance
  - Photoshop was used for creating the mockup images of the website during planning stage.
  - Google Fonts was used to import fonts.
  - Google Chrome Lighthouse was used during the testing of the website.
  - Google Chrome Developer Tools was used during testing, debugging and making the website responsive.
  - Cloudinary was used to store media files.
  - Stripe was integrated to handle payment processing in a secure and convenient way.
  - W3C HTML Validator was used to check for errors in the HTML code.
  - W3C CSS Validator was used to check for errors in the CSS code
  - Js Hint was used to validate the JavaScript code.
  - CI Python Linter was used to validate the Python code.

### python Packages

<details>
  <summary>Python Packages</summary> 
    <img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715794819/python-packages_cjvwpl.png">   
</details>

## Deployment

  ### Deploy on Heroku

1. Create Pipfile

  - In the terminal enter the command  pip3 freeze > requirements.txt, and a file with all requirements will be created.

2. Setting up Heroku

  - Go to the Heroku website (https://www.heroku.com/)
  - Login to Heroku and choose Create App
  - Click New and Create a new app
  - Choose a name and select your location
  - Go to the Resources tab
  - From the Resources list select Heroku Postgres
  - Navigate to the Deploy tab
  - Click on Connect to Github and search for your repository
  - Navigate to the Settings tab
  - Reveal Config Vars and add your aws, Database URL and Secret key.

3. Deployment on Heroku

  - Go to the Deploy tab.
  - Choose the main branch for deploying and enable automatic deployment
  - Select manual deploy for building the App

### Fork the repository

For creating a copy of the repository on your account and change it without affecting the original project, useFork directly from GitHub:

  - On My Repository Page, press Fork in the top right of the page.
  - A forked version of my project will appear in your repository.

### Clone the repository

For creating a clone of the repository on your local machine, useClone:

  - On My Repository Page, click the Code green button, right above the code window
  - Chose from HTTPS, SSH and GitClub CLI format and copy (preferably HTTPS)
  - In your IDE open Git Bash
  - Enter the command git clone followed by the copied URL
  - Your clone was created

## Credits

### Media
  - Downloaded the shoe pictures from [Doc & Mark](https://docandmark.com/) and [freepik](https://www.freepik.com/)

### Code
  - Boutique Ado Walkthrough was used for the base of this project
  - [island-bees](https://github.com/emmahewson/island-bees)
  - [bookheaven](https://github.com/Dayana-N/Book-Heaven-PP5/)
### Acknowledgements
  - To complete this project I used Code institue student template: Gitpod full template
  - [Stackoverflow](https://stackoverflow.com/)
### Mockup
  - [Mockup screenshot generator](https://ui.dev/amiresponsive)
### Comments
   I really enjoyed working on this project. My idea was to develop a real world application with user friendly design. I wish I had more time to add automated testing and to describe in detail the manual testing performed as I usually do. That will be added on a later stage.
