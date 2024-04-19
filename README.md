# Macmassage Website

Welcome to the Macmassage Website project! This Django-based web application allows users to schedule appointments, manage services, and more for a massage therapy business.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Screenshots](#screenshots)

## Introduction

The Macmassage Website project provides a convenient online platform for clients to book appointments, browse services, and manage their bookings. Built with Django, the application follows best practices for web development and provides a user-friendly experience.

## Features

- **User Authentication**: Secure user registration and login system.
- **Appointment Scheduling**: Easy scheduling with customizable time slots.
- **Service Management**: Browse and manage services, including descriptions and pricing.
- **Responsive Design**: Optimized for seamless viewing on various devices.
- **Integration**: Easily integrate with third-party APIs for additional functionality.

## Installation

To run the Macmassage Website project locally, follow these steps:

1. Clone the repository to your local machine:

  git clone https://github.com/peggle-me-this/macmassage.git

2. Navigate to the project directory:

  cd macmassage_site

3. Install the required dependencies:

  pip install -r requirements.txt

4. Apply database migrations:

  python manage.py migrate

5. Start the development server:

  python manage.py runserver

6. Access the application in your web browser at http://localhost:8000/

##Usage
Once the application is running locally, you can access its features through the web interface. Here are some common tasks you can perform:

User Account: Create a user account and log in to access the booking system.
Appointment Booking: Schedule appointments by selecting available time slots and providing necessary details.
Dashboard: View and manage upcoming appointments in the user dashboard.
Profile Management: Make changes to user profile information.

##Documentation
For detailed documentation on the project's codebase, including API references and usage guides, refer to the documentation.
[!Docs](https://github.com/peggle-me-this/macmassage/tree/main/docs)

##License

The Macmassage Website project is currently not licensed. Without a specific license, the default copyright laws apply, 
meaning others cannot reproduce, distribute, or create derivative works from this project without explicit permission.

## Screenshots

### Homepage
[![Homepage](index.htmlScreenshot.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/index.htmlScreenshot.png)
A screenshot of the home page with hyperlink to contact info 'reach out' and logo.

### Booking Page
[![Booking Page](bookAppointment.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/bookAppointment.png)
A screenshot of the book appointment page.

### Registration Page
[![Registration Page](registration.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/registration.png)
A screenshot of the registraton page.

### Successful Registration Page
[![Successful Registration Page](registrationSuccessful.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/registrationSuccessful.png)
A screenshot of the registration successful page.

### View Current Bookings Page
[![View Current Bookings Page](viewCurrentBookings.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/viewCurrentBookings.png)
A screenshot of the current bookings available page.

### Bookings Hyperlinks Special Page
[![Bookings Hyperlinks Special Page](bookingsHyperlinksSpecial.png)]([http://example.com](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/bookingsHyperlinksSpecial.png)
A screenshot of of the bookings hyperlinks and the specials image.

### About Macmassage Page
[![About Macmassage Page](about_macmassageHyperlinks.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/about_macmassageHyperlinks.png)
A screenshot of the about page with the hyperlinks for social media and contact details.

### Booking Redirect Without Login Page
[![Booking Redirect Without Login Page](bookingRedirectWithoutLogin.png)](https://github.com/peggle-me-this/macmassage/blob/main/screenshots/bookingRedirectWithoutLogin.png)
A screenshot of the redirect if you try to make a booking while not logged in.
