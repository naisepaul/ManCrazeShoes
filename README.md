# ManCrazeShoes

# Introduction

Welcome to the [ManCrazeShoes](https://mancrazeshoes-4c1185db9ef9.herokuapp.com/). This is the documentation for my e-commerce web application: Mancrazeshoes. It has been built using Django, Python, JavaScript, CSS3 & HTML5 for educational purposes as part of Code Institute’s Diploma in Web Application Development Course.

[You can see the live project here](https://mancrazeshoes-4c1185db9ef9.herokuapp.com/)

![Responsive view](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715724756/mock-up_of7llk.png)

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

## User Experience

### Website goal

- To provide users with a place to purchase shoes for men of their interest.
- To provide the users the ability to search and browse shoes of different categories.
- To provide the users with the ability to check their order history.
- To provide the users with the most recents shoes from the company.

### Scope

This project seeks to create an e-commerce platform dedicated to providing customers with a wide selection of shoes for men. 

- Create an account and log in securely.
- Reset their password if necessary.
- Browse, search, and filter through available shoes.
- Add desired shoes to their shopping cart.
- Adjust quantities within their shopping cart.
- Remove items from their shopping cart as needed.
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
16. As an administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders made on this site.
17. As an administrator, I want to be able to add new products to the website so that I can expand the product catalog
18. As an administrator, I want to be able to edit existing products on the website so that I can update and manage the product catalog.
19. As an administrator, I want to be able to remove products from the website so that I can manage the product catalog.
20. As a User I want to be able to complete the checkout process for my shopping cart so that I can purchase the items I've added to my cart.

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
</details><br> 

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