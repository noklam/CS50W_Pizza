# Project 3
[![Build Status](https://dev.azure.com/lrcnok0929/lrcnok0929/_apis/build/status/noklam.CS50W_Pizza)](https://dev.azure.com/lrcnok0929/lrcnok0929/_build/latest?definitionId=3)
[![Build Status](https://travis-ci.org/noklam/CS50W_Pizza.svg?branch=master)](https://travis-ci.org/noklam/CS50W_Pizza)

## Web Programming with Python and JavaScript

Pizza Ordering System with Django

# Objectives

* Experimenting with Test Driven Development approach, try to write test first. Follow this book. (Good to have)
Test-Driven Development with Python, 2nd Edition
* Add CI into practice together with TDD (Good to have)
* Become more comfortable with Django.(Must)
* Gain experience with relational database design.(Must)
* Develop the registration features and order features in different branch, and merge them at later, to simulate real-life working env. (Must)

# Tools

* Django, Selenium, Travis CI

# Installation

A webdriver is needed in order to run selenium
https://github.com/mozilla/geckodriver/releases

# Milestones

## Done:


## To-be Done:

* Complete the Menu, Adding Items, and Registration/Login/Logout steps.
* Complete the Shopping Cart and Placing an Order steps.
* Complete the Viewing Orders and Personal Touch steps.

## Progress

 08/05/2018:

* Create functional_test for user story
* Create unittest


# Requirements

* Menu: Your web application should support all of the available menu items for Pinnochio�s Pizza & Subs (a popular pizza place in Cambridge). It�s up to you, based on analyzing the menu and the various types of possible ordered items (small vs. large, toppings, additions, etc.) to decide how to construct your models to best represent the information. Add your models to orders/models.py, make the necessary migration files, and apply those migrations.
  
* Adding Items: Using Django Admin, site administrators (restaurant owners) should be able to add, update, and remove items on the menu. Add all of the items from the Pinnochio�s menu into your database using either the Admin UI or by running Python commands in Django�s shell.
  
* Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.
  
* Shopping Cart: Once logged in, users should see a representation of the restaurant�s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual �shopping cart.� The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again.
  
* Placing an Order: Once there is at least one item in a user�s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.
  
* Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.
  
* Personal Touch: Add at least one additional feature of your choosing to the web application. Possibilities include: allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders, integrating with the Stripe API to allow users to actually use a credit card to make a purchase during checkout, or supporting sending users a confirmation email once their purchase is complete. If you need to use any credentials (like passwords or API credentials) for your personal touch, be sure not to store any credentials in your source code, better to use environment variables!
* In README.md, include a short writeup describing your project, what�s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project.

* Additional package in requirements.txt
* Goal: Clone it in other computer, run requirements and able to start app immediately without configuration.
