# bitprop-real-estate
Introduction
    The Bitprop Rental Management System is a web-based application designed to streamline the process of     
    managing rental properties and connecting prospective tenants with available properties. The system allows 
    prospective tenants to view available properties, register their interest for specific properties, and 
    notifies the relevant agent when a tenant has indicated interest.

Table of Contents
    -Introduction
    -Features
    -Thought Process
    -Assumptions
    -Difficulties
    -Design Choices
    -Implementation
    -Nice-to-Have Features
    -Setup and Usage
    - Testing the code

Features
    Property Listings: Display available properties with details such as location and price.
    Registration Form: Allow prospective tenants to submit their interest in specific properties.
    Agent Login: Provide agents with a login to view tenant inquiries related to properties they manage.
    Email Notifications: Notify agents via email when a tenant registers interest in a property.

Thought Process
    Research Process:
        Researched existing rental management systems to understand common features and user requirements.
        Studied Flask and SQLite documentation for backend development.
        Explored various email sending APIs for sending notification emails.
    Design Process:
        Designed a user-friendly interface using HTML, CSS, and JavaScript.
        Created a simple SQLite database schema for storing property and tenant data.
        Implemented backend logic in Python using Flask to manage user interactions and database operations.

Assumptions
    The application is designed for a small-scale rental management operation, managing a limited number of properties and tenants.
    The application assumes a single-agent model, where each property is managed by a single agent.
    Authentication and user roles are not implemented in the initial version of the application.

Difficulties
    Integrating email sending functionality required researching and understanding SMTP protocols and configuring email servers.
    Ensuring data integrity and security in a multi-user environment was a challenge, especially regarding database operations.

Design Choices
    HTML/CSS/JavaScript: Chosen for front-end development due to familiarity and ease of implementation for basic user interface requirements.
    SQLite: Selected as the backend database solution for its simplicity and ease of setup, suitable for small-scale applications.
    Flask: Chosen as the web framework for its lightweight and flexible nature, suitable for developing RESTful APIs and handling HTTP requests.
    SMTP: Utilized for sending notification emails, leveraging Python's built-in smtplib library for email sending functionality.

Implementation
    HTML/CSS/JavaScript: Used to create user interface elements such as forms, tables, and navigation.
    SQLite: Employed for creating and querying databases to store property and tenant information.
    Flask: Utilized for routing HTTP requests, handling form submissions, and rendering dynamic HTML templates.
    SMTP: Integrated for sending notification emails to agents when tenants express interest in properties.

Nice-to-Have Features
    User Authentication: Implementing user authentication and authorization for agents and administrators to access specific functionalities.
    Property Management: Adding features for agents to manage property listings, including adding, editing, and removing properties.
    Enhanced Notification System: Implementing a more robust notification system with email templates and customization options.
    Responsive Design: Making the user interface responsive to different screen sizes and devices for a better user experience.
    Property Search Functionality: Introducing a feature that allows clients to search for properties according to price, location, size, etc., enhancing the user experience and providing more tailored property recommendations.

Setup and Usage

    Installation:
        1. Clone the repository:
            git clone https://github.com/your_username/bitprop-real-estate.git
        2. Install dependencies:
            pip install -r requirements.txt

    How to run:
        1. Navigate to the project directory:
            cd bitprop-real-estate
        2. Run the WebServerFlask.py Application:
            python3 WebServerFlask.py
        3. Open a web browser and go to http://localhost:5000 to access the application.

Testing the Code
    To test the functionality of the system:
    
        1. Ensure that the necessary email configuration is set up in WebServerFlask.py:
            EMAIL_ADDRESS = 'your_email@example.com'
            EMAIL_PASSWORD = 'your_email_password'
            SMTP_SERVER = 'smtp.example.com'
            SMTP_PORT = 587

        2. Update line 55 in WebServerFlask.py with the email address of the agent who should receive notification emails:
        recipient_email = 'agent_email@example.com'

Note: For a fully functional website, implement a method to retrieve the responsible agent's email based on the property of interest.
