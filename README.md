# HOOKED ON FISH

![Main Mockup](README-files/main-mockup.png)

[View Live Website here.](https://hooked-on-fish-85d55f56e378.herokuapp.com/)

[GitHub Repo](https://github.com/LemmenAid/hooked-on-fish)

***

## Index – Table of Contents
* [Features](#features)
* [Project Development](#project-development)
* [Layout](#layout)
* [Data Schema](#data-schema)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

***

### Project Description  

_Hooked on Fish is a website for my final portfolio project with [Code Institute](https://codeinstitute.net/ie/)._

Hooked on Fish is a website for a small-scale, sustainable seafood business based in Connemara, Galway, Ireland. The business is run by Thomas Flaherty, a local fisherman who catches fresh seafood daily—including mackerel, brown crab, lobster, scallops, and shrimp. The website serves as an online presence for the business, offering information about the catch, a direct way for customers to get in touch, and a place to stay updated on new products and market availability.

### Project Purpose

The purpose of Hooked on Fish is to create a digital storefront that reflects the business’s values—sustainability, transparency, and quality. The website connects local customers with fresh seafood while offering an inside look at the fishing process through blog updates and a newsletter called Fisherman’s Friends. It also serves as a foundation for expanding the business’s reach through local markets and direct sales.

***

## Features

### General Features on each page

#### Navigation Bar

* Displayed across all pages, the navigation bar provides links to Home, About, Products, Contact, and an Instagram page for social updates.


Navigation bar:<br>
![Nav Bar](README-files/navbar.png)

Navigation bar for members:<br>
![Nav Bar](README-files/navbar-member.png)

Dropdown navigation menu:<br>
![Nav Bar dropdown menu](README-files/navbar-drop.png)

***

#### The Footer

The footer appears on every page and includes the business logo, copyright information, and links to the business’s social media accounts. 
It's also possible to Sign Up for the FIsherman's Friends newsletter in the footer.


![Footer](README-files/footer.png)

***

### Features by page

#### Home Page
The homepage introduces Hooked on Fish with a striking hero image and a clear call-to-action, encouraging visitors to learn more about the business and its products.

![Home Page](README-files/home-page.png)

***

#### About Us Page
The About page tells the story of Hooked on Fish, focusing on Thomas's experience as a fisherman, the boat Fortibus, and the business’s commitment to sustainable fishing practices.

![About Us](README-files/about.png)

***

#### Products Page
This page showcases the available seafood, providing descriptions and sustainability notes for each type of catch. The page is designed for easy future expansion into an e-commerce platform.

![Features](README-files/products.png)

***

#### Profile
The personalized profile page provides logged-in members with an overview of their previous orders. It also allows them to save their delivery information or update that information. 

![Dashboard](README-files/profile.png)

***

#### Where to buy Pages
On these pages, visitors can read information on where and how to buy the Hooked on Fish products.

![Member Stories](README-files/buy.png)

***

#### CRUD for SuperUser
A super user has full CRUD functionality for the products on the website.
<br>
<br>
For users who are not logged in, the Save, Delete, and Comment options are not available.
<br>
<hr>

#### Products when logged in as a super user:
![Story](README-files/product-login.png)

#### Products and comments when logged out:
![Story](README-files/product-logout.png)

***

#### Contact Page
A contact form allows customers to reach out with inquiries, whether they’re looking for specific seafood, bulk orders, or general information. The form includes a dropdown menu for users to select their inquiry type.

![Create Story](README-files/create-story.png)

***

#### Custom Error Handler Page
Custom error pages to ensure user-friendly navigation, even in unexpected situations.

![Sign Up](README-files/error-page.png)

***

### Future Implementations

* A weekly catch update displaying available seafood in real-time.
* A recipe section featuring simple seafood recipes using the business’s  fresh products.
* A fishing report archive, giving insight into seasonal trends and sustainable practices.
* A gallery page of all images features on the website.

***

## Project Development

### Creating Process

Developing Hooked on Fish has been an exciting challenge, combining both backend and frontend skills. Since this project is a real-world business application, my goal was to create a professional, minimal, and user-friendly website that accurately represents the brand.

This project allowed me to further develop my knowledge of Django, Bootstrap, and database management. I focused on clean code, easy navigation, and practical business functionality. The process involved careful planning to ensure the website could scale in the future if the business expands.

### Project SetUp

The project follows an MVC framework using Django. The foundational pages were built first (Home, About, Products, and Contact), followed by dynamic elements like the where to buy and contact form.

I also incorporated user stories and an agile approach to ensure a structured development process.

Jump to Credits: [Credits](#credits)

***

### Agile Development

[GitHub Projects](https://github.com/users/LemmenAid/projects/5/views/1) served as an Agile tool for the development of this project. 

I started with creating the User Stories. Then these stories were broken down into tasks as steps to follow in the building process of the website. I added these steps to the Project Board on Github to keep track of the buidling process and to assist with better organisation and prioritisation of the tasks. I made sure that Should-have prioritised user stories were not more than 60% of the timebox user story points total.


<details>
<summary> User Story Template
</summary>

![User Story Template](README-files/user-story-temp.png)
</details>

<details>
<summary> User Story Issues
</summary>

![User Story Issues](README-files/issues.png)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](README-files/project-board.png)
</details>
<br>

***

### User Stories

VISITOR

1. As a visitor, I want to easily understand the purpose of the website, so I can decide if I want to explore further.
2. As a visitor, I want to see a clear and engaging homepage, so I feel drawn into the brand.
3. As a visitor, I want to browse the available seafood products, so I can see what’s on offer.
4. As a visitor, I want to know where the seafood is sourced from, so I can trust the authenticity of the product.
5. As a visitor, I want to find contact details, so I can get in touch with the business for any questions.

CUSTOMER

6. As a customer, I want to create an account, so I can save my details for future orders.
7. As a customer, I want to easily add products to a cart, so I can purchase multiple items in one order.
8. As a customer, I want to securely pay for my order online, so I can confidently complete my purchase.
9. As a customer, I want to receive an order confirmation email, so I know my purchase has been successful.
10. As a customer, I want to leave a review for the products I purchased, so I can share my experience.

ADMIN

11. As an admin, I want to add, edit, or remove seafood products, so the inventory stays up to date.
12. As an admin, I want to manage customer orders, so I can ensure they are processed and delivered correctly.

MARKETING

13. As a visitor, I want to subscribe to a newsletter, so I can stay updated on news and special offers.
14. As a visitor, I want to follow the business on social media, so I can see updates and connect with the brand.
15. As a visitor, I want to view recipes or cooking tips for seafood, so I can feel inspired to try new dishes.


***

## Layout

### Wireframes

The layout is clean and minimal. Navigation is streamlined through a clear menu bar, with links to key areas such as Products, Contact, and About.

Key interface elements include:

- Interactive buttons for saving and deleting products, visible only when applicable.
- Clear error pages that redirect users when something goes wrong.
- Responsiveness is a priority, ensuring smooth usability on mobile and desktop devices.

Wireframes were created using Balsamiq to plan the site’s structure.

<details>
<summary> Home Page
</summary>

![alt text](README-files/wireframe-main.png)<br>

</details>

<details>
<summary> Text Pages
</summary>

![alt text](README-files/wireframe-text-page.png)<br>

</details>

<details>
<summary> Products Page
</summary>

![alt text](README-files/wireframe-features.png)<br>

</details>

<details>
<summary> Mobile View
</summary>

![alt text](README-files/mb-all-wireframe.png)<br>

</details>
<br>

***

### Data Schema

The database structure follows a relational model with key entities for products, buy, and contact inquiries. Below is an Entity Relationship Diagram that shows the key models and their fields:

<details>
<summary> Entity Relationship Diagram (ERD)
</summary>

![Database Diagram](README-files/erd-diagram.png)

</details>

<br>

#### 1. Profile Model

Attributes:
- Primary Key: Auto-generated by Django.
- first_name (TextField)
- last_name (TextField)
- email (TextField, unique)<br>

Purpose: 
Stores basic user information and is extended by the User Profile model.


#### 2. Product Model

Attributes:
- user (OneToOneField linked to User model)
- saved_posts (ManyToManyField linked to Post model)

Purpose: 
User model for personalised dashboard, to include additional fields for saved posts.

#### 3. Contact Model

Attributes:
- name (CharField, max length: 200)
- email (EmailField)
- garden_experience (CharField, max length: 20)
- garden_zone (CharField, max length: 3)
- message (TextField)
- read (BooleanField)

Purpose: 
Captures contact form submissions, including garden-related queries.

#### 6. About Model

Attributes:
- title (CharField)
- profile_image (CloudinaryField)
- content (TextField)
- updated_on (DateTimeField)

Purpose: 
Represents content for the "About Us" page.

#### Relationships Overview:
- One-to-One: User Profile extends User.
- One-to-Many:
-- Product bought by users.
- Many-to-Many: Users save multiple orders through the User Profile model.

<br>

This schema efficiently organizes data to support Hooked on Fish' functionality, such as customer profiles, products and contact forms. It leverages Django's ORM to enforce relationships and constraints.

***

## Design

### Colour Scheme

![alt text](README-files/colour-palette.png)

The colour scheme is kept very simple and clean. The few colours used drawn inspiration from the Connemara coastal landscape, and give a Fishermens feel.

Wanting to keep the design clean and clear, I have used only a few hues of blue for adding colour. Making sure the attention of the reader is mostly drawn to the content. <br>
I have chosen a white neutral for the background and a deep charcoal for headers and accents to provide the necessary contrast, ensuring readability and accessible text elements without overwhelming the page.

### Typography

The typography on Hooked on Fish is a clean sans-serif font, to create a modern clean feel. 

The following code has been imported into the top of the base.html file:

    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">

Roboto:<br>
![alt text](README-files/roboto.png)<br>


### Imagery

Several image sources were used for the images throughout the website.<br>

<details>
<summary> The links to these sources are listed here:
</summary>

* [Hero Image, FIsherman]()

* Photo by : 
* Photo by : 
</details>

*** 

## Technologies Used

### Languages

* HTML
* CSS
* Javascript
* Python

### Frameworks, programs and libraries

* [Django](https://docs.djangoproject.com/en/5.0/) - Framework used to create website.
* [AllAuth](https://docs.allauth.org/en/latest/) - used to provide authentication framework for the project.
* [Django signals](https://docs.djangoproject.com/en/5.0/topics/signals/) - Using signals.py to automatically create a profile when a new member registers.
* [PostGreSQL database](https://www.postgresql.org/) - used as the relational database management for the website.
* [Github](https://github.com/) - Used for hosting the repository.
* [VS Code](https://code.visualstudio.com/) - Used for developing the application.
* [Am I Responsive?](https://ui.dev/amiresponsive) - Used to create an image of the website on various screen sizes.
* [Heroku](https://www.heroku.com/) - Used for deploying the live project.
* [Bootstrap](https://getbootstrap.com/) - Used to add style to the displayed pages
* [ChatGPT](https://chat.openai.com/) - Used to create the blogs, member stories and about page.
* [Code Beautify](https://codebeautify.org/) - Used to format HTML and CSS code.
* [Clouidnary](https://cloudinary.com/) - Used to host images and integrate with django and the admin portal.

### Design
* Fonts from [Google Fonts](https://fonts.google.com/) 
* Favicon [Favicon](https://favicon.io)
* Wireframes [Balsamiq wireframe](https://balsamiq.com/)
* Images from several sources, underwhich [Pexels](https://www.pexels.com/)
* Colour palette generator [Coolors](https://coolors.co/)

***

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

***

## Deployment 
_I have used several different READMEs to write the deployment section of this README.<br> 
All listed in the credit section below._<br>


The Live deployed application can be found deployed on [Heroku](https://hooked-on-fish-85d55f56e378.herokuapp.com/).<br>
This project was developed using [Visual Studio Code](https://code.visualstudio.com/) and committed to git and pushed to GitHub.

### Database
This project uses [Neon.tech](https://www.neon.tech) for the PostgreSQL Database. This was provided by Code Institute via a database-maker website for Code Institute Students.

### Cloudinary API

This project uses the Cloudinary API to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.<br>
On your Cloudinary Dashboard, you can copy your API Environment Variable.<br>
Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

### Heroku Deployment 

The application was deployed to Heroku. In order to deploy, the following steps were taken:

1. If you have an account, login to Heroku. Otherwise create a new account.
2. Once signed in, click the "New" button in the top right corner, below the header and choose "Create new app".
3. Choose a unique name for the application and select your region. When done, click "Create app".
4. This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars" and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy:
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

<hr>

### Local Deployment
This project can be cloned or forked in order to make a local copy on your own system.
For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Forking repo on GitHub

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

#### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

***

## Credits

* I would like to thank Brian Macharia for his great mentor support and guidance - helping me through the process of building my first ever e-commerce full stack website.
* My facilitator Lewis from Code Institute for supporting us through our final project and giving us great tips and resources for learning tools, and her feedback during the weekly stand-ups.
* At last I would like to give thanks to my friends and family for taking the time to test the website and giving me great feedback.

### Content

I have taken inspiration and information from the following websites for Hooked on Fish:

* [Garden Illustrated](https://www.gardensillustrated.com)
* [RHS](https://www.rhs.org.uk/garden-inspiration/garden-types/coastal-gardens)
* [Martha Stewart.com](https://www.marthastewart.com/)
* [Gardenista](https://www.gardenista.com/)
* [Gardening Know How](https://www.gardeningknowhow.com/garden-how-to/gardening-by-zone)

***

### Code

The walkthrough project "Boutique Ado" was a great way of understanding how to get started on an full stack Django framework website and it was therefor a good source of inspiration. I have also used my fourth portfolio project [Coastal Gardens](https://github.com/LemmenAid/coastal-gardens/) as inspiration for this website. 

I have used various resources to help me with figuring out how to create the Hooked on Fish Website:


* [Simple is better than Complex - for the dashboard](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)
* [Harabat - for the dashboard](https://harabat.github.io/django-htmx/07_users_and_profiles/)
* [Stackoverflow - create profile](https://stackoverflow.com/questions/61580144/django-create-profile-for-user-signal)
* [Django Waves - one to one](https://djangowaves.com/resources/django-one-to-one-field/)
* [Geeks for Geeks - add slug field inside model](https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/)
* [MdBootstrap - for the footer](https://mdbootstrap.com/docs/standard/navigation/footer/examples-and-customization/)
* [Stackoverflow - for the auto-dismiss alert](https://stackoverflow.com/questions/23101966/bootstrap-alert-auto-close)
* [Get Bootstrap - for the auto-dismiss alert](https://getbootstrap.com/docs/5.0/components/alerts/)
* [She Codes - for the auto-dismiss alert](https://www.shecodes.io/athena/8466-how-to-create-an-event-listener-to-alert-a-message)
* [GitHub/CMed01 - for the custom error pages](https://github.com/CMed01/portfolio-milestone-4/tree/main)
* [Learn Django - for the custom error pages](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)
* [Django Docs - for automated testing](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)
* [The Mozilla Developer Network (MDN) - for automated testing](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
* [YouTube - Mastering Django Unit Testing: An In-Depth Introduction and Tutorial](https://www.youtube.com/watch?v=N_HLNV2UQjg&t=1s)
* [YouTube - Automated Test Basics - Python & Django](https://www.youtube.com/watch?v=6I_haJimhPY)

* [Stack overflow](https://stackoverflow.com/)
* [Pep Style Guide](https://peps.python.org/pep-0008/)
* [W3Schools](https://www.w3schools.com/)
* [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/style/)
* [Real Python - for quick tutorials on several subjects](https://realpython.com/)
* [Tripleten - best practices](https://tripleten.com/blog/posts/python-best-practices)

* Code Institute Slack Channel

***

### Templates I have used for inspiration and creating my readme.md and my testing.md:

I have used my own ReadMe of [Coastal Gardens](https://github.com/LemmenAid/coastal-gardens/) as inspiration for this ReadMe. I used several other ReadMe files as inspiration as well:

* [Sample README Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md?plain=1) - Copied the Deployment section and used for general guideline.
* [Read Me Template Code Institute](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)
Used for general guideline.
* [Plant Factory - crypticCaroline](https://github.com/crypticCaroline/ms1-plantfactory/blob/master/README.md?plain=1) - Especially for the Technologies Used, Testing sections and design sections.
* [Visit Järbo - ClaudiaInSweden](https://github.com/ClaudiaInSweden/visit-jarbo/blob/main/README.md?plain=1) - General inspiration / guideline.
* [Bushy Park Tennis CLub - LewisMDillon](https://github.com/LewisMDillon/bushy-park-tennis-club-ld) - Deployment section and TESTING.md.
* [Oasis Hotels - Marchopkins96](https://github.com/Marchopkins96/oasis-hotels) - General inspiration / guideline.
* [GitHub Docs](https://docs.github.com/en)