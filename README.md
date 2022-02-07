<h1 align="center">Eduzita Creations</h1>

[View the live project here.](https://eduzita-creations.herokuapp.com/)

This is the main marketing website for Eduzita Creations. It is designed to be responsibe and accessible on a range of devices, making it easy to navigate for potential students and partners.

<h2 align="center"><img src="https://i.imgur.com/jJ0AC0f.jpg"></h2>

## User Experience (UX)

-   ### User stories

    -   ####

        1. As a shopper I want to view a list of products so I can select some to purchase.
        2. As a shopper I want to view a specific category of products to quickly find products I'm interested in withouth having to search through all products.
        3. As a shopper I want to view individual product details to identify the price, description, product rating, product image and available sizes.
        4. As a shopper I want to quickly identify deals, clearance items and special offers to take advantage of special savings on products I'd like to purchase.
        5. As a shopper I want to easily view the total of my purchases at any time to avoid spending too much.
        6. As a shopper I want to sort the list of available products so I can easily identify the best rated, best priced and categorically sorted produtcs.
        7. As a shopper I want to sort a specific category of product so I can find the best-priced or best-rated products across broad categories such as minerals, fossils and gemstone beads.
        8. As a shopper I want to search for a product by name or description so I can find a specific product I'd like to purchase.
        9. As a shopper I want to easily see what I've searched for and the number of results to quickly decide whether the product I want is available.
        10. As a shopper I want to easily select the quantity of a product when purchasing it to ensure I don't accidentally select the wrong product or quantity.
        11. As a shopper I want to view items in my bag to be purchased to identify the total cost of my purchase before checkout.
        12. As a shopper I want to adjust the quantity of individual items in my bag to easily make changes to my purchase before checkout.
        13. As a shopper I want to easily enter my payment information to check out quickly and without hassle.
        14. As a site user I want to easily register for an account so I can have a personal account and be able to view my profile.
        15. As a site user I want to easily login or logout so I can access my personal account information.
        16. As a site user I want to easily recover my password in case I forget it.
        17. As a site user I want to receive an email confirmation after registering so I can verify that my account registraion was successful.
        18. As a site user I want to have a personalized user profile so I can view my personal order history and order confirmations, and save my payment information.

-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are white and salmon pink.
    -   #### Typography
        -   The Lato font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Montserrat is a clean font used frequently in programming, so it is both attractive and appropriate.

*   ### Wireframes

    -   Shopping cart - [View](media/wireframes/cartpng.png)
    -   Desktop - [View](media/wireframes/desktoppng.png)
    -   Login page - [View](media/wireframes/loginpng.png)
    -   Sign up page - [View](media/wireframes/signuppng.png)
    -   Mobile - [View](media/wireframes/mobilepng.png)

## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [Django:](https://www.djangoproject.com/)
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.


### Testing User Stories from User Experience (UX) Section

-   #### 

    1. As a shopper I want to view a list of products so I can select some to purchase.
        1. As the user enters the page they have a "shop now" button that displays all available products.
    2. As a shopper I want to view a specific category of products to quickly find products I'm interested in withouth having to search through all products.
        1. On the main navigation bar users have the option to filter different categories.
    3. As a shopper I want to view individual product details to identify the price, description, product rating, product image and available sizes.
        1. Users can click on the product image and will be redirected to the product page where all information can be found.
    4. As a shopper I want to quickly identify deals, clearance items and special offers to take advantage of special savings on products I'd like to purchase.
        1. On the main navigation bar there's a specific tab for special offers.
    5. As a shopper I want to easily view the total of my purchases at any time to avoid spending too much.
        1. On the top right of the page at all times will be displayed the value of the shopping cart.
    6. As a shopper I want to sort the list of available products so I can easily identify the best rated, best priced and categorically sorted produtcs.
        1. On the various product pages there's a product filtering list.
    7. As a shopper I want to sort a specific category of product so I can find the best-priced or best-rated products across broad categories such as minerals, fossils and gemstone beads.
        1. On the various product pages there's a product filtering list.
    8. As a shopper I want to search for a product by name or description so I can find a specific product I'd like to purchase.
        1. Users can search for products using key words or specific names to find desired products.
    9. As a shopper I want to easily see what I've searched for and the number of results to quickly decide whether the product I want is available.
        1. After entering a key word or name all matching items will show up as a list.
    10. As a shopper I want to easily select the quantity of a product when purchasing it to ensure I don't accidentally select the wrong product or quantity.
        1. There is a quantity selector on each product page, including checkout bag.
    11. As a shopper I want to view items in my bag to be purchased to identify the total cost of my purchase before checkout.
        1. Before final purchase users will have the chance to verify and complete payment.
    12. As a shopper I want to adjust the quantity of individual items in my bag to easily make changes to my purchase before checkout.
        1. Before final purchase users will have the chance to verify and complete payment.
    13. As a shopper I want to easily enter my payment information to check out quickly and without hassle.
        1. To even more simplify this users can complete payment and delivery information in the profile tab.
    14. As a site user I want to easily register for an account so I can have a personal account and be able to view my profile.
        1. Any user can register for a new account and personalize profile in the profile tab.
    15. As a site user I want to easily login or logout so I can access my personal account information.
        1. Any user can register for a new account and personalize profile in the profile tab.
    16. As a site user I want to easily recover my password in case I forget it.
        1. User can recover password and will be prompted with a recovery email address.
    17. As a site user I want to receive an email confirmation after registering so I can verify that my account registraion was successful.
        1. Users will receive an email confirmation link right after registering a new account.
    18. As a site user I want to have a personalized user profile so I can view my personal order history and order confirmations, and save my payment information.
        1. In the profile tab all users will be able to view past and present orders as well as saving delivery and payment information.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Deployment
###	Forking the GitHub Repository

Forking a repository enables us to make a copy of the original repository on our GitHub account so we can view it and make changes without affecting the original work.
This is done using the following steps:
 1. Log in to [GitHub](https://github.com/shaff600) account and select the relevant repository.
 2. To the top right of the page there are three buttons, the furthest right says **Fork.** Click on this button.
 3. A copy of the original repository will now be in your account.
###	Making a Clone
To make a clone of my project use the following steps:
 1. Go to my [account](https://github.com/shaff600) and locate the relevant repository.
 2. Next to the green **Gitpod** button, click on **CODE.**
 3. Click on **Download Zip.**
 4. Once downloaded, you can extract the zip file's contents and save it to a desktop and run the website locally.

 ### Setting up the app
 - Within you work inviroment terminal:
    - Install requirements file, enter. 'pip install -r requirements.txt' in the terminal 
    - Import data
	    - "python3 manage.py loaddata categories.json"
		    - ensure this import is loaded first as brands and product rely on the relationship 
		- "python3 manage.py loaddata brands.json"
		- "python3 manage.py loaddata products.json"
		- Create a Super User to gain Admin access
			- "python3 manage.py createsuperuser
			- Enter credentials 
			- Navigate to "/admin/ URL on local host
  
**Create Heroku application:**

1.  Signed into Heroku
2.  Created a new app by clicking the "new" button.
3.  Select the new app
4.  Created the app project name
5.  In the resources tab, provision a new Postgres database.
7.  To use Postgres, in the gitpod terminal install dj_database_url (pip3 install dj_database_url) and psycopg2 (pip3 install psycopg2-binary)

**Setup AWS S3 Bucket:**

1.  Created an AWS account
2.  Went into the management console
3.  Selected S3
4.  Named a bucked related to the project
5.  Selected the closest region
6.  Allowed public access to the bucket, config changes required 
7.  Within the properties tab switched on static website hosting
8.  Within the permissions ta, pasted the CORS configuration which allows access between the Heroku app and the S3 bucket.
9.  Created a security policy for the S3 bucket using the built-in policy generator
10.  Set Action as "GetObject", copy and paste the unique ARN
11.  Copied the generated policy into the bucket policy editor
12.  Went onto the access control tab and sekected the public access item

## Credits

### Code
-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.