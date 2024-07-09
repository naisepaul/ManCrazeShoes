# ManCrazeShoes - E-Commerce Site - Testing

![Mock-up](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720508580/mock-up_aav1d8.png)

[Click here to view the live web application](https://mancrazeshoes-4c1185db9ef9.herokuapp.com/)

This is the testing documentation for my e-commerce web application: ManCrazeShoes


Back to [README.MD](README.md)

# Testing

- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)

- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [User Story Testing](#user-story-testing)
- [Stripe](#stripe)

## Code Validation

### HTML

I ran the code for all the pages through the [W3C HTML Validator](https://validator.w3.org/nu/) using the textarea input by generating the source code from the deployed site (right click and select 'View Page Source' in Chrome) and pasting it in to allow me to check all pages whether requiring log in or not. All code passed the validation tests. Results below.


<details><summary>HTML Validation Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **HOME** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | closing tag error- resolved | PASS |
| **PRODUCTS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Page passes validation with no errors | PASS |
| **PRODUCT DETAIL** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ |No p element in scope but a p end tag seen- resolved | PASS |
| **ADD PRODUCT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ |  No errors | PASS |
| **EDIT PRODUCT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ |  Page passes validation no errors | PASS |
| **BAG** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Duplicate ID error - resolved | PASS |
| **CHECKOUT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Page passes validation no errors | PASS |
| **CHECKOUT SUCCESS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PROFILE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **ALLAUTH TEMPLATES** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | contact_us tag error - resolved | PASS |
| **403** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **404** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **500** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |

</details>

---

### CSS Validation

I ran the CSS code through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). All code passed the validation tests. Results below.


<details><summary>CSS Validation Results Table</summary>

| **Feature**    | **Expected Outcome**                  | **Test Performed**                                   | **Result**                                                                                                              | **Pass / Fail** |
|----------------|---------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| CSS Validation | Page passes validation with no errors | Ran CSS through https://jigsaw.w3.org/css-validator/ | no errors | PASS            |

</details>

<details><summary>Validation Final Results Screenshot</summary>

<img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715839095/css-validation_meb0b0.png">

</details>

---

### JavaScript

I ran the JavaScript code through [JSHint](https://jshint.com/). For full results see the dropdowns below.

<details><summary>JavaScript Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **quantity_input.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |
| **stripe_elements.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. | PASS |
| **message_toggle.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **update-remove** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | No Errors | PASS |
| **sort_box.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **countryfield.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ |  No errors remaining | PASS |
| **rating_select.js** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **quantity-input** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |
| **Size-selector** | Page passes validation with no errors | Ran JavaScript through https://jshint.com/ | Missing semi-colons. All fixed. No errors remaining | PASS |

</details>

<details><summary>JavaScript Results Images</summary>

<details><summary>quantity_input.js</summary>
<img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715840620/quantity-input-script_ooiiwh.png">
</details>

<details><summary>stripe_element.js</summary>
<img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715840621/strip-elements_fgccgg.png">
</details>

<details><summary>size-selector</summary>
<img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715840620/size-script_bovn5a.png">
</details>

<details><summary>update-remove</summary>
<img src="https://res.cloudinary.com/dmhdrvehj/image/upload/v1715840621/update-remove-script_msruwh.png">
</details>
</details>

### Python

I ran the app.py code through [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/) to check the Syntax. GitPod also has a built in Python Linter which was used throughout the development process (see below). All code passed the validation tests. For full results see the dropdowns below.

<details><summary>Python Results Table</summary>

| **App** | **File** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|---|
| mancrazeshoes | settings | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| mancrazeshoes | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| bag | contexts | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | signals | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | webhook_handler | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| checkout | webhooks | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| home | test_views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| products | widgets | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | admin | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | forms | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | models | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | urls | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |
| profiles | views | Code passes with no errors | Ran app.py through https://extendsclass.com/python-tester.html | Code passes with no errors | PASS |

</details>

## Responsiveness

The manual testing was done on the following devices

- Dell laptop 14 inch
- Apple iPhone 13 pro max
- Oneplus 10

### Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | ---|

## Manual Testing

- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on the links in Navbar|Redirect to correct page |Pass|Navbar present on all pages |
||Click on the links in My Account|All redirect to correct page |Pass|Navbar present on all pages |
||Click on the cart icon| Redirect to shopping cart |Pass|Navbar present on all pages |
|Searchbar|type keywords|returns correct results |Pass|searchabar present on all pages |
|Hero section|Open Home page. Ensure the carousel section loads as it should|Hero section loads as it should |Pass| |
|Hero section|Click on the shop now button, ensure it leads to products page|It leads to products page |Pass| |
|Listing Card| Click on the listing card image. Ensure it redirects to the correct single product page |When clicked each card redirects to the correct product details listing page |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each external link opens the correct page in a new tab |All external links open the correct page in a new tab |Pass| |

- Products Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Product Home link| Click on all of the links in product home. Ensure they redirect to the home page. |All links redirect to the correct page. |Pass| |
|Sorting| Click on the select element and ensure that each sorting method returns the correct results |Each sorting method returns the correct results |Pass| |
|Button on bottom right | Click on the button it redirect to top of the page.||Button redirect to the top of the page |Pass| |

- Single Product Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Product details|Open the product page. Ensure all the relevant information is correct for the specific product|All the relevant information is correct for the specific product|Pass||
||Click add to cart button and ensure the product is added to cart|When clicked the product is added to cart |Pass||
|Description|Select description tag and ensure description is displayed| description is displayed |Pass||
|size|Display the size and selected size. And default size is given| details is displayed |Pass||

- Shopping Cart 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Shopping cart|Add product to cart and ensure it appears correctly in the cart|The product appears correctly in the cart|Pass||
|Update quantity|From the quantity button select new quantity and update. Ensure the total is calculated correctly|The product updates correctly in the cart|Pass||
|remove product|Click on the remove button and ensure the product is removed from cart|The product is removed from the cart|Pass||

- Checkout

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Checkout|Fill in the form and click on save details. Use stripe test card and confirm the order is successfull by checking stripe. Confirm the address is saved to profile|The address is saved to my profile. The purchase is successfull. Stripe logs show success.|Pass||
|Checkout|Visit the page as unauthenticated user. Ensure the form is not prefilled and does not allow to save details|The form is not prefilled and does not allow to save details.|Pass||
|Checkout|Click on back button and ensure it takes the user to the previous page|The back button work as it should.|Pass||

- My Profile

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Profile|Fill in the form and click on update. Ensure the details are updated|The details are updated|Pass||

- My Orders

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Orders|Open the orders page and ensure the orders showing are correct. |The orders are correct|Pass||
|Orders |Click on the order link and ensure it leads to the order page|The link leads to the order page|Pass||

- Product Management

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Admin dashboard|Visit admin page. Ensure the refine drop down works by selecting all available options |The refine drop down works as expected|Pass||
|Admin dashboard|Click on the edit product button, ensure it redirects to the edit product page |it redirects to the edit product page|Pass||
|Admin dashboard|Click on the delete product button, it delete the product |it delete the product |Pass||
|Admin dashboard|Click on the add product button, ensure it redirects to the add product page |it redirects to the add product page|Pass||

## Automated testing

Due to time limits there was no scope to expand.

## User Story Testing

|User Story|Screenshot|Result|
| --- | --- | --- |
| As a developer I can set up a new Django project so that I can create the project's structure | The project was set up successfully| <mark>PASS<mark>  |
| As a developer I can connect database and media storage(Cloudinary) so that the user's stored data is stored successfully | Database and media storage were connected successfully| <mark>PASS<mark> |
| As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development | The application was deployed after the initial set up to confirm everything is working as expected| <mark>PASS<mark> |
| As a User I can navigate through the website so that I can access different sections efficiently |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715772856/navbar-desktop_wvjktt.png)| <mark>PASS<mark> |
| As a user I can visit the home page so that I can identify the purpose of the website |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715848660/front-page_bqoxhf.png)| <mark>PASS<mark> |
| As a user I want to be able to view a list of all available products in the bookshop so that I can browse and choose books to purchase |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715775695/product-page_autnwo.png)| <mark>PASS<mark> |
| As a user I want to be able to view detailed information about a single product so that I can make an informed decision before purchasing |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715777126/single-product-page_zv5ifj.png)| <mark>PASS<mark> |
|As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find shoes that match my interests |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715849055/category-selection_slidbv.png)| <mark>PASS<mark> |
|As a User I want to be able to browse through a large list of products in the shop so that I can view all categories in an organised way |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715849299/category-product_h3lqqi.png)| <mark>PASS<mark> |
|As a user I want to be able to register an account so that I can have access to all functionality of Mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715793054/signup_aai1gy.png)| <mark>PASS<mark> |
|As a user, I want to be able to log in to my account so that I can access my personalized features and make purchases on Mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715793054/login_k0g7oi.png)| <mark>PASS<mark> |
|As a registered user I want to be able to see my profile page so that I can update my information |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715778176/profile-order_pkxlme.png)| <mark>PASS<mark> |
|As a user, I want to be able to add products to my shopping bag so that I can purchase multiple items at once on Mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715791580/shopping-bag_ucginn.png)| <mark>PASS<mark> |
|As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase on mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715849847/shopping-bag-update_y7ndou.png)| <mark>PASS<mark> |
|As a user, I want to be able to adjust the quantity of products in my shopping cart so that I can control the quantity of items I want to purchase on Mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715849847/shopping-bag-update_y7ndou.png)| <mark>PASS<mark> |
|As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases on Mancrazeshoes with confidence. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715850024/payment-stripe_oaby3e.png)| <mark>PASS<mark> |
|As an administrator, I want to be able to add new products to the website so that I can expand the product catalog on Mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715787400/add-product_emn0en.png)| <mark>PASS<mark> |
|As an administrator, I want to be able to edit existing products on the website so that I can update and manage the product catalog on Mancrazeshoes. |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715787400/edit-product_myityq.png)| <mark>PASS<mark> |
|As a website owner, I want to improve the website's search engine optimization (SEO) so that the website can rank higher in search engine results and attract more organic traffic.  |Descriptive meta tags were added to the main template, including title, description and keywords. | <mark>PASS<mark> |
|As a User I want to be able to complete the checkout process for my shopping cart so that I can purchase the items I've added to my cart |![feature](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715792268/checkout_hvysl3.png)| <mark>PASS<mark> |

## Stripe
- Order created successfully

![order](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715792504/checkout-confirmation_tljixh.png)

- Stripe webhooks

![order](https://res.cloudinary.com/dmhdrvehj/image/upload/v1720393587/Stripe-webhook_fo4vox.png)

- Stripe Events
![order](https://res.cloudinary.com/dmhdrvehj/image/upload/v1715851906/stipe_hrlszq.png)
