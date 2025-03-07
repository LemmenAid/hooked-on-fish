# Testing

Return back to the [README.md](README.md) file.

## Index – Table of Contents
* [HTML](#html)
* [CSS](#css)
* [JavaScript](#javascript)
* [Python](#python)
* [Responsiveness](#responsiveness)
* [Browser Compatibility](#browser-compatibility)
* [Lighthouse Audit](#lighthouse-audit)
* [Defensive Programming](#defensive-programming)
* [User Story Testing](#user-story-testing)
* [Automated Testing](#automated-testing)
* [Solved Bugs](#solved-bugs)



## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2F) | ![screenshot](TESTING-files/html-home.png) | Pass: No Errors |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Fabout%2F) | ![screenshot](TESTING-files/html-about.png) | Pass: No Errors |
| About - Grounds | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Fabout%2F) | ![screenshot](TESTING-files/html-about-grounds.png) | Pass: No Errors |
| Zone - map | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Fabout%2Fzone-map%2F) | ![screenshot](TESTING-files/html-zone.png) | Pass: No Errors |
| Contact Us | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Fcontact%2F) | ![screenshot](TESTING-files/html-contact.png) | Pass: No Errors |
| Features | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Ffeatures%2F) | ![screenshot](TESTING-files/html-features.png) | Pass: No Errors |
| Feature Story | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Fthe-enchanting-irish-green-bells-moluccella-laevis%2F) | ![screenshot](TESTING-files/html-feature-story.png) | Pass: No Errors |
| Dashboard | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Faccounts%2Flogin%2F#textarea) | ![screenshot](TESTING-files/html-dashboard.png) | Pass: No Errors |
| Member Story | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Faccounts%2Flogin%2F#textarea) | ![screenshot](TESTING-files/html-memeber-stories.png) | Pass: No Errors |
| Create Story | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Faccounts%2Flogin%2F#textarea) | ![screenshot](TESTING-files/html-create.png) | Pass: No Errors |
| Custom Error 400 | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2F8000-lemmenaid-coastalgarden-1k1wefnkeaf.ws.codeinstitute-ide.net%2Ftest-error%2F#textarea) | ![screenshot](TESTING-files/html-400.png) | Pass: No Errors |
| Custom Error 403 | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2F8000-lemmenaid-coastalgarden-1k1wefnkeaf.ws.codeinstitute-ide.net%2Ftest-error%2F#textarea) | ![screenshot](TESTING-files/html-403.png) | Pass: No Errors |
| Custom Error 404 | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2F8000-lemmenaid-coastalgarden-1k1wefnkeaf.ws.codeinstitute-ide.net%2Ftest-error%2F#textarea) | ![screenshot](TESTING-files/html-404.png) | Pass: No Errors |
| Custom Error 500 | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2F8000-lemmenaid-coastalgarden-1k1wefnkeaf.ws.codeinstitute-ide.net%2Ftest-error%2F#textarea) | ![screenshot](TESTING-files/html-500.png) | Pass: No Errors |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](TESTING-files/html-login.png) | Pass: No Errors |
| Logout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Faccounts%2Flogin%2F#textarea) | ![screenshot](TESTING-files/html-logout.png) | Pass: No Errors |
| Signup | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](TESTING-files/html-signup.png) | Errors explained below. |

<br>
The following validation errors appear on the signup page when using Django allauth: 
<br>
<br>

1. "End tag p implied, but there were open elements" 
- This occurs because the default form rendering does not close < p > or < span > tags properly when rendering help text.

2. "Unclosed element span" and "Stray end tag span" 
- These errors are due to the way Django allauth handles help text within form fields. It wraps help text in < span > tags but does not ensure strict compliance with HTML validation rules.

3. "No p element in scope but a p end tag seen" 
- Django allauth uses < p > tags inconsistently, which causes this error when rendering form errors or help texts.
<br>

These errors are caused by the default Django form rendering engine used by allauth, which generates the HTML automatically. While these issues do not affect functionality, fixing them would require overriding the templates or form rendering logic entirely.

*** 

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcoastal-gardens-e950c82335fb.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](TESTING-files/css-style.png) | Pass: No Errors |

***

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files (the comments.js file, the contact-zone-map.js file and the javascript in the base.html file). After inserting /*jshint esversion: 6 */ at the top of the file no errors were returned apart from one undefined variable - bootstrap.

| File | Screenshot | Notes |
| --- | --- | --- |
| comments.js | ![screenshot](TESTING-files/js-comments.png) | One undefined variable "bootstrap" see below. |
| contact-zone-map.js | ![screenshot](TESTING-files/js-contact-zone-map.png) | Pass: No Errors |
| JavaScript in the base.html | ![screenshot](TESTING-files/js-base.png) | One undefined variable "bootstrap" see below. |


One undefined variable "bootstrap".

This appears when using Bootstrap's JavaScript components (like new bootstrap.Modal in the comments.js file.) because JSHint doesn't recognize the bootstrap object as a global variable, even though it is defined globally by the included Bootstrap JS file.
This is a common issue with external libraries that define global variables. JSHint doesn't automatically detect these variables unless they are declared in the configuration.

***

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. No errors were returned:


#### Validation For coastalgardens App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| asgi.py | ![screenshot](TESTING-files/python-cg-asgi.png) | Pass: No Errors |
| settings.py | ![screenshot](TESTING-files/python-cg-settings.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-cg-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-cg-views.png) | Pass: No Errors |
| wsgi.py | ![screenshot](TESTING-files/python-cg-wsgi.png) | Pass: No Errors |

***

#### Validation For about App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-about-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-about-apps.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-about-models.png) | Pass: No Errors |
| tests.py | ![screenshot](TESTING-files/python-about-tests.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-about-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-about-views.png) | Pass: No Errors |

***

#### Validation For blog App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-blog-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-blog-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](TESTING-files/python-blog-forms.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-blog-models.png) | Pass: No Errors |
| tests.py | ![screenshot](TESTING-files/python-blog-tests.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-blog-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-blog-views.png) | Pass: No Errors |

***

#### Validation For contact App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-contact-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-contact-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](TESTING-files/python-contact-forms.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-contact-models.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-contact-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-contact-views.png) | Pass: No Errors |

***

#### Validation For dashboard App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-db-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-db-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](TESTING-files/python-db-forms.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-db-models.png) | Pass: No Errors |
| tests.py | ![screenshot](TESTING-files/python-dashboard-tests.png) | Pass: No Errors |
| signals.py | ![screenshot](TESTING-files/python-db-signals.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-db-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-db-views.png) | Pass: No Errors |


***

### Testing Error Pages

To ensure that custom error pages (e.g., 400, 403, 404, and 500 errors) display correctly, the following setup was implemented during development for testing purposes.

1. A temporary route was added in urls.py to trigger various error responses manually.
2. The temporary test_error view raises specific exceptions or returns error status codes to simulate different error scenarios.<br>

![Screenshot](TESTING-files/testing%20error%20pages..png)

<br>

Testing Procedure<br>
1. Visit the /test-error/ URL in your browser. 
2. Uncomment one of the lines in the test_error function at a time to simulate the desired error.
3. Reload the page and verify the correct error template is displayed.
4. Check that the page matches your custom design for error pages.

For the 404 test, a non-existent URL was accessed directly instead of using the /test-error route.



***

### Browser Compatibility

Coastal Gardens was tested through the Heroku app website on the following browsers without issues:  
- Google Chrome (Version 132.0.6834.6) | Works as expected
- Mozilla Firefox (Version 132.0) | Works as expected
- Safari (Version 20619.2.8) | Works as expected
- Microsoft Edge (Version 131.0.2903.51) | Works as expected

***

### Responsiveness
* The website has been tested on different devices(under which; iPhone SE / iPhone 12 / Samsung Galaxy S9 / MacBook Air / MacBook Pro / HP laptop).
* The website was responsive on all screens from mobile phones to desktops.
* Chrome DEV Tools have been used to check the responsivness throughout the development of the website.

***

### Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.
Overall I am happy with the outcome. However, the Best Practices is significantly influenced by Cloudinary images.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](TESTING-files/lh-home.png) | Some minor performance and accessibility warnings |
| About | Desktop | ![screenshot](TESTING-files/lh-about.png) | Some minor accessibility warnings |
| Features | Desktop | ![screenshot](TESTING-files/lh-features.png) | Some minor performance and accessibility  warnings |
| Contact Us | Desktop | ![screenshot](TESTING-files/lh-contact.png) | Some minor performance and accessibility warnings |
| Dashboard | Desktop | ![screenshot](TESTING-files/lh-dashboard.png) | Some minor performance and accessibility warnings |
| Create Story | Desktop | ![screenshot](TESTING-files/lh-create-story.png) | Some minor accessibility warnings |
| Member Stories | Desktop | ![screenshot](TESTING-files/lh-member-stories.png) | Some minor performance and accessibility warnings |
| Sign Up | Desktop | ![screenshot](TESTING-files/lh-signup.png) | Some minor performance and accessibility warnings |
| Custom Error Pages | Desktop | ![screenshot](TESTING-files/lh-error-pages.png) | Some minor SEO and accessibility warnings |

***

### Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Features link in navbar | Redirection to Features page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact Us page | Pass | |
| | Click on Signup link in navbar | Redirection to Signup page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Logout link in navbar | Log out & Redirection to Home page | Pass | |
| | Click on Dashboard link in navbar | Redirection to Dashboard | Pass | |
| | Click on Member Stories link in navbar | Redirection to Member Stories page | Pass | |
| Features Page | | | | |
| | Click on post container | Redirection to that post details page | Pass | |
| | Click on post title | Redirection to that post details page | Pass | |
| | Click on Pagination right arrow | Redirection to next pagination page | Pass | |
| | Click on Pagination left arrow | Redirection to previous pagination page | Pass | |
| Signup Page | | | | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Redirects user to personal dashboard | Pass |
| Log In | | | | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to dashboard page | Pass | |
| Log Out | | | | |
| | Click Logout button | Logs out user, Redirects user to home page | Pass |
| Dashboard | | | | |
| | Click on the saved posts | Redirects to that post | Pass | |
| | Click on the create story button | Redirects to create story page | Pass | |
| Create Story | | | | |
| | upload photo - choose file button | able to upload photo from device | Pass | |
| | add text to title field | add text | Pass | |
| | add text to content field | add text | Pass | |
| | add text to excerpt field | add text | Pass | |
| | click publish story button | gives notification that story is waiting for approval (admin needs to approve to publish) | Pass | |
| Member Stories Page | | | | |
| | Click on post container | Redirection to that post details page | Pass | |
| | Click on post title | Redirection to that post details page | Pass | |
| | Click on Pagination right arrow | Redirection to next pagination page | Pass | |
| | Click on Pagination left arrow | Redirection to previous pagination page | Pass | |
| Story Delete Confirm | | | | |
| | delete story button | button only visible to author of story | Pass | |
| | Click on delete story button | Delete story, display confirmation modal with definite delete button | Pass | |
| Comment section | | | | |
| | Click on delete comment button | Delete comment, display confirmation modal with definite delete button | Pass | |
| | Click on edit comment button | puts comment in add comment textfield to update | Pass | |
| | Click update comment button | gives feedback message that comment is waiting for approval | Pass | |
| | Add comment button | when not logged in add comment section not available | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Redirect to login page | Pass | |
| Site buttons | | | | |
| | Hover effect buttons | hover effect for buttons across the site the background colour change | Pass |
| | feedback messages | After updating or deleting a comment as a user you get a feedback message. | Pass |
| | messages disappear automatically | after 5 sec message appears it will automatically disappear. | Pass |

***

### User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a Visitor, I want to browse feature articles on coastal gardening, so that I can learn more about gardening by the sea. | ![screenshot](TESTING-files/user-story-features.png) |
| As a Visitor, I want to be able to view the plant zone map, so I can determine in which zone I live. | ![screenshot](TESTING-files/user-story-zone.png) |
| As a Visitor, I want to read an About page to understand the purpose and mission of the site. | ![screenshot](TESTING-files/user-story-about.png) |
| As a Visitor, I want to easily navigate to different sections of the site, so I can find relevant information quickly. | ![screenshot](TESTING-files/user-story-navigation.png) |
| As a Visitor, I can see a paginated list of site feature posts so that I see only the most up-to-date posts and can navigate to older posts if I wish | ![screenshot](TESTING-files/user-story-pagination.png)|
| As a Potential Member, I want to view a sign-up page that explains the benefits of joining, so I know why I should become a member. | ![screenshot](TESTING-files/user-story-signup.png) |
| As a Potential Member, I want a simple registration process, so I can quickly join the community. | ![screenshot](TESTING-files/user-story-signup2.png) |
| As a Member, I want a personalised dashboard where I can save and view my favourite articles, so I can easily revisit them. | ![screenshot](TESTING-files/user-story-dashboard.png) |
| As a Member, I want to see a list of all my comments in one place, so I can keep track of my participation. | ![screenshot](TESTING-files/user-story-comments.png) |
| As a Member, I can see a paginated list of site Member Stories so that I see only the most up-to-date posts and can navigate to older posts if I wish | ![screenshot](TESTING-files/user-story-member-stories.png)|
| As a Member, I want the ability to write and publish my own gardening stories, so I can share my experiences with other members. | ![screenshot](TESTING-files/user-story-create.png) |
| As a Member, I want access to member-only stories, so I can learn from the experiences of other coastal gardeners. | ![screenshot](TESTING-files/user-story-member-story.png) |
| As a Member, I can delete a story that I have written. | ![screenshot](TESTING-files/user-story-delete-story.png) |
| As a Member, I can comment on stories and edit / delete these comments. | ![screenshot](TESTING-files/user-story-delete-edit-comments.png) |
| As a Member, I can logout so that access to my account is stopped and my information is kept secure | ![screenshot](TESTING-files/user-story-logout.png) |
| As an Member, I can login to the site so that I can access account-based functionalities and information | ![screenshot](TESTING-files/user-story-login.png) |
| As an Admin, I can update select site content via a back-end interface so that I can add and remove content from the site, without engaging with the site's code. | ![screenshot](TESTING-files/user-story-admin1.png) |
| As an Admin, I want to moderate comments, so I can ensure a respectful and constructive environment. | ![screenshot](TESTING-files/user-story-admin2.png) |
| As an Admin, I want to manage user accounts, so I can assist with membership issues and maintain site quality. | ![screenshot](TESTING-files/user-story-admin3.png) |

***

### Automated Testing

#### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Blog | tests.py | 93% | ![screenshot](TESTING-files/automated-blog.png) |
| About | tests.py | 100% | ![screenshot](TESTING-files/automated-about.png) |
| Dashboard | tests.py | 99% | ![screenshot](TESTING-files/automated-dashboard.png) |

***

### Solved Bugs

* During testing I replaced the Post.objects.get() line with get_object_or_404 in my save_post view. This ensures that if the Post with the given post_id does not exist, Django will return a 404 response instead of raising an exception.

* Added the 'status=1' filter in the user_dashboard view, to only include stories that are published in "Your Stories".

* During testing of my error pages, I realized that the order of URL paths in urls.py is crucial. Specifically, the empty ("") path must always be the last entry. Initially, my error page tests weren’t working because I had added the test paths at the end, which caused the empty path to interfere. Once I corrected the order, everything worked as expected.

* The else block of my create_stories_view was being executed every time the request method was GET, which ment that the error message from the view was added even when the user first visits the page (without having submitted the form/published the story). To fix this, I moved the error message handling to the part of the code where the form is checked for validity.

***