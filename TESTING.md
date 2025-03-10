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
| Home | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2F) | ![screenshot](TESTING-files/html-home.png) | Pass: No Errors |
| About | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fabout%2F) | ![screenshot](TESTING-files/html-about.png) | Pass: No Errors |
| About - Grounds | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fabout%2Fgrounds%2F) | ![screenshot](TESTING-files/html-about-grounds.png) | Pass: No Errors |
| All products | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fproducts%2F) | ![screenshot](TESTING-files/html-products.png) | Pass: No Errors |
| Product detail | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fproducts%2F3%2F) | ![screenshot](TESTING-files/html-product-detail.png) | Pass: No Errors |
| Buy Online | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fbuy%2Fonline%2F) | ![screenshot](TESTING-files/html-online.png) | Pass: No Errors |
| Buy in Person | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fbuy%2Fin-person%2F) | ![screenshot](TESTING-files/html-inperson.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fcontact%2F) | ![screenshot](TESTING-files/html-contact.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fcontact%2F) | ![screenshot](TESTING-files/html-bag.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fcheckout%2Fcheckout_success%2FEAE37899F5244847AD8FEDE43A9AC043) | ![screenshot](TESTING-files/html-checkout.png) | Pass: No Errors |
| Checkout Success | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Fproducts%2F) | ![screenshot](TESTING-files/html-checkout-success.png) | Pass: No Errors |
| Product Management | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-management.png) | These errors appear to originate from code that was emplate-generated or framework-based code. As this code is part of a pre-existing structure and functions as intended, I have opted not to modify it. |
| Profile | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-profile.png) | Pass: No Errors |
| Custom Error 400 | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-400.png) | Pass: No Errors |
| Custom Error 403 | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-403.png) | Pass: No Errors |
| Custom Error 404 | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-404.png) | Pass: No Errors |
| Custom Error 500 | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-500.png) | Pass: No Errors |
| Login | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](TESTING-files/html-login.png) | Pass: No Errors |
| Logout | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](TESTING-files/html-logout.png) | Pass: No Errors |
| Signup | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2Faccounts%2Fsignup%2F#l219c299) | ![screenshot](TESTING-files/html-signup.png) | Errors explained below. |

<br>
The following validation error appeared on the signup page when using Django allauth: 
<br>
<br>

"Element ul not allowed as child of element small in this context." 
- This error was occured because a < ul > element was nested inside a < small > tag. This issue originates from how Django's crispy-forms library renders form errors by default. Since this is not code I have written manually but part of the third-party package’s default behavior, I have chosen to leave it as is, as it does not impact the website’s functionality.
<br>


*** 

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files (base.css / profile.css / checkout.css).

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fhooked-on-fish-85d55f56e378.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](TESTING-files/css-style.png) | Pass: No Errors |

***

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files and js scripts on html pages. After inserting /*jshint esversion: 6 */ and /* global $ */  at the top of the validator file no errors were returned.

| File | Screenshot | Notes |
| --- | --- | --- |
| script in bag.html | ![screenshot](TESTING-files/js-bag.png) | PASS |
| stripe-elements.js | ![screenshot](TESTING-files/js-stripe-elements.png) | PASS  after inserting /* global Stripe */ |
| Quantity input script in products app. | ![screenshot](TESTING-files/js-products-quantity-script.png) | PASS |
| new image script in product html pages. | ![screenshot](TESTING-files/js-products-img-script.png) | PASS |
| countryfield.js in profiles app | ![screenshot](TESTING-files/js-countryfield.png) | PASS |
| toast script in base.html | ![screenshot](TESTING-files/js-base.png) | PASS |

***

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. No errors were returned:


#### Validation For hooked_on_fish App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| asgi.py | ![screenshot](TESTING-files/python-hof-asgi.png) | Pass: No Errors |
| settings.py | ![screenshot](TESTING-files/python-hof-settings.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-hof-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-hof-views.png) | Pass: No Errors |
| wsgi.py | ![screenshot](TESTING-files/python-hof-wsgi.png) | Pass: No Errors |

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

#### Validation For bag App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | ![screenshot](TESTING-files/python-bag-apps.png) | Pass: No Errors |
| contexts.py | ![screenshot](TESTING-files/python-bag-contexts.png) | Pass: No Errors |
| tests.py | ![screenshot](TESTING-files/python-bag-tests.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-bag-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-bag-views.png) | Pass: No Errors |

***

#### Validation For buy App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-buy-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-buy-apps.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-buy-models.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-buy-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-buy-views.png) | Pass: No Errors |

***

#### Validation For checkout App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-checkout-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-checkout-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](TESTING-files/python-checkout-forms.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-checkout-models.png) | Pass: No Errors |
| signals.py | ![screenshot](TESTING-files/python-checkout-signals.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-checkout-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-checkout-views.png) | Pass: No Errors |
| webhook_handler.py | ![screenshot](TESTING-files/python-checkout-wb-handler.png) | Pass: No Errors |
| webhooks.py | ![screenshot](TESTING-files/python-checkout-webhooks.png) | Pass: No Errors |

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

#### Validation For home App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | ![screenshot](TESTING-files/python-home-apps.png) | Pass: No Errors |
| tests.py | ![screenshot](TESTING-files/python-home-tests.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-home-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-home-views.png) | Pass: No Errors |

***

#### Validation For products App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | ![screenshot](TESTING-files/python-products-admin.png) | Pass: No Errors |
| apps.py | ![screenshot](TESTING-files/python-products-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](TESTING-files/python-products-forms.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-products-models.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-products-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-products-views.png) | Pass: No Errors |

***

#### Validation For profiles App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | ![screenshot](TESTING-files/python-profiles-apps.png) | Pass: No Errors |
| forms.py | ![screenshot](TESTING-files/python-profiles-forms.png) | Pass: No Errors |
| models.py | ![screenshot](TESTING-files/python-profiles-models.png) | Pass: No Errors |
| urls.py | ![screenshot](TESTING-files/python-profiles-urls.png) | Pass: No Errors |
| views.py | ![screenshot](TESTING-files/python-profiles-views.png) | Pass: No Errors |

***

### Testing Error Pages

To ensure that custom error pages (e.g., 400, 403, 404, and 500 errors) display correctly, the following setup was implemented during development for testing purposes.

1. A temporary route was added in urls.py to trigger various error responses manually.
2. The temporary test_error view raises specific exceptions or returns error status codes to simulate different error scenarios.<br>

![Screenshot](TESTING-files/testingerrorpages.png)

<br>

Testing Procedure<br>
1. Visit the /test-error/ URL in your browser. 
2. Uncomment one of the lines in the test_error function at a time to simulate the desired error.
3. Reload the page and verify the correct error template is displayed.
4. Check that the page matches your custom design for error pages.

For the 404 test, a non-existent URL was accessed directly instead of using the /test-error route.



***

### Browser Compatibility

Hooked on Fish was tested through the Heroku app website on the following browsers without issues:  
- Google Chrome (Version 132.0.6834.6) | Works as expected
- Mozilla Firefox (Version 132.0) | Works as expected
- Safari (Version 20619.2.8) | Works as expected
- Microsoft Edge (Version 131.0.2903.51) | Works as expected

***

### Responsiveness
* The website has been tested on different devices(under which; iPhone SE / iPhone 12 / Samsung Galaxy S20 / MacBook Air / MacBook Pro / HP laptop).
* The website was responsive on all screens from mobile phones to desktops.
* Chrome DEV Tools have been used to check the responsivness throughout the development of the website.

***

### Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.
Overall I am happy with the outcome. However, the Best Practices is significantly influenced by Cloudinary images.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](TESTING-files/lh-home.png) | Some minor performance and accessibility warnings |
| Who We Are | Desktop | ![screenshot](TESTING-files/lh-about.png) | Some minor accessibility warnings |
| Where We Fish | Desktop | ![screenshot](TESTING-files/lh-grounds.png) | Some minor performance and accessibility warnings |
| Buy Online | Desktop | ![screenshot](TESTING-files/lh-online.png) | Some minor performance and accessibility  warnings |
| Buy in Person | Desktop | ![screenshot](TESTING-files/lh-inperson.png) | Some minor performance and accessibility  warnings |
| All Products | Desktop | ![screenshot](TESTING-files/lh-products.png) | Some minor performance and accessibility  warnings |
| Product Detail | Desktop | ![screenshot](TESTING-files/lh-product-detail.png) | Some minor accessibility  warnings |
| Shopping Bag | Desktop | ![screenshot](TESTING-files/lh-bag.png) | Some minor performance and accessibility  warnings |
| Checkout | Desktop | ![screenshot](TESTING-files/lh-checkout.png) | Some minor accessibility  warnings |
| Contact Us | Desktop | ![screenshot](TESTING-files/lh-contact.png) | Some minor performance and accessibility warnings |
| Profile | Desktop | ![screenshot](TESTING-files/lh-profile.png) | Some minor performance and accessibility warnings |
| Sign Up | Desktop | ![screenshot](TESTING-files/lh-signup.png) | Some minor accessibility warnings |
| Custom Error Pages | Desktop | ![screenshot](TESTING-files/lh-error-pages.png) | Some minor SEO and accessibility warnings |

***

### Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About / Who we are link in navbar | Redirection to About page | Pass | |
| | Click on About / Where we Fish  link in navbar | Redirection to grounds page | Pass | |
| | Click on Where to Buy / online link in navbar | Redirection to where to buy page | Pass | |
| | Click on Where to Buy / in person link in navbar | Redirection to where to buy page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact Us page | Pass | |
| | Click on Signup link in navbar | Redirection to Signup page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on Logout link in navbar | Log out & Redirection to Home page | Pass | |
| | Click on Profile link in navbar | Redirection to Profile | Pass | |
| | Click on All Products link in navbar | Redirection to All Products page | Pass | |
| | Click on single Product link in navbar | Redirection to the Product page | Pass | |
| All Products Page | | | | |
| | Click on add to bag | adds product to bag | Pass | |
| | Click on increment button | increments quantity | Pass | |
| | Click on decrement button | decrements quantitiy | Pass | |
| | Click on Product | Redirection to product detail page| Pass | |
| Product detail Page | | | | |
| | Click on add to bag | adds product to bag | Pass | |
| | Click on keep shopping | Redirect back to products page | Pass | |
| | Click on increment button | increments quantity | Pass | |
| | Click on decrement button | decrements quantitiy | Pass | |
| | Click on Product | Redirection to product detail page| Pass | |
| Buy in Person Page | | | | |
| | Hover over Partner shops | color change | Pass | |
| | Click on Partner Shop | Redirects to Partner Shop website | Pass | |
| Log In | | | | |
| | Click Login button | Logs in user, Redirects user to home page | Pass |
| Log Out | | | | |
| | Click Logout button | Logs out user, Redirects user to home page | Pass |
| Profile | | | | |
| | Click on the previous order | Redirects to overview of that previous order | Pass | |
| | Click on update information button | Updates and saves new information | Pass | |
| Shopping Bag Page | | | | |
| | Click on keep shopping | Redirect back to products page | Pass | |
| | Click on secure checkout | Redirect to checkout page | Pass | |
| | Click on increment button | increments quantity | Pass | |
| | Click on decrement button | decrements quantitiy | Pass | |
| | Click on update button | updates quantitiy | Pass | |
| | Click on delete button | deletes product from bag | Pass | |
| Checkout Page | | | | |
| | Fill out checkout form - asks for required field | Only able to checkoout after filling out required fields | Pass | |
| | Click on checkout button | Redirection to checkout succes page | Pass | |
| | Click on Adjust bag | Redirection back to Shopping Bag Page | Pass | |
| Contact Us Page | | | | |
| | Submit contact form | Only able to submit after filling out all the required field. | Pass | |
| Site Navigations - Logged Out User | | | | |
| | Navigate to any login required URL | Redirect to login page | Pass | |
| Site buttons | | | | |
| | Hover effect buttons | hover effect for buttons across the site the background colour change | Pass |
| | feedback messages | After adding, updating or deleting a product as a user you get a feedback message. | Pass |
| | messages disappear automatically | after 5 sec message appears it will automatically disappear. | Pass |

***

### User Story Testing

| User Story | Screenshot |
| --- | --- |
| 1. As a visitor, I want to easily understand the purpose of the website, so I can decide if I want to explore further. | ![screenshot](TESTING-files/user-story-1.png) |
| 2. As a visitor, I want to see a clear and engaging homepage, so I feel drawn into the brand. | ![screenshot](TESTING-files/user-story-2.png) |
| 3. As a visitor, I want to browse the available seafood products, so I can see what’s on offer. | ![screenshot](TESTING-files/user-story-3.png) |
| 4. As a visitor, I want to know where the seafood is sourced from, so I can trust the authenticity of the product. | ![screenshot](TESTING-files/user-story-4.png) |
| 5. As a visitor, I want to find contact details, so I can get in touch with the business for any questions. | ![screenshot](TESTING-files/user-story-5.png)|
| 6. As a customer, I want to create an account, so I can save my details for future orders. | ![screenshot](TESTING-files/user-story-6.png) |
| 7. As a customer, I want to easily add products to a cart, so I can purchase multiple items in one order. | ![screenshot](TESTING-files/user-story-7.png) |
| 8. As a customer, I want to securely pay for my order online, so I can confidently complete my purchase. | ![screenshot](TESTING-files/user-story-8.png) |
| 9. As a customer, I want to receive an order confirmation email, so I know my purchase has been successful. | ![screenshot](TESTING-files/user-story-9.png) |
| 10. As an admin, I want to add, edit, or remove seafood products, so the inventory stays up to date. | ![screenshot](TESTING-files/user-story-10.png) ![screenshot](TESTING-files/user-story-10-2.png) |
| 11. As an admin, I want to manage customer orders, so I can ensure they are processed and delivered correctly. | ![screenshot](TESTING-files/user-story-11.png) |
| 12. As a visitor, I want to subscribe to a newsletter, so I can stay updated on news and special offers. | ![screenshot](TESTING-files/user-story-12.png) |

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

* During testing, I removed the type attribute from the < script > tags in the HTML files, as the HTML validator flagged it as unnecessary.

* I updated the name attribute for the extra meta tag block on the product detail page to resolve an HTML validation error caused by duplicate name attributes in the base.html file.

* I added a < ul > element to the mobile navigation in the HTML and removed the type attribute from JavaScript script tags in base.html to resolve validation errors.



* During testing of my error pages, I realized that the order of URL paths in urls.py is crucial. Specifically, the empty ("") path must always be the last entry. Initially, my error page tests weren’t working because I had added the test paths at the end, which caused the empty path to interfere. Once I corrected the order, everything worked as expected.

***