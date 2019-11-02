# CFMS Readme

## Computerised Facility Management System

This project is a Web application powered by Django; a web development framework for python. The application is a system designed to suit the requirements of a company that needs to coordinate work activities across several assets.

The system is based around work orders; any user may order work (maintenance, repair, etc), from this request a user is assigned to do the work, an asset is linked to the work and parts associate with the work can be altered. A planned feature is a preventative maintenance schedule for each asset based on its requirements and work orders automatically generated for these scheduled tasks.

The system tracks 4 different elements that can all influence each-other; Assets, Parts, Work orders and Users.

### Assets

These are any piece of equipment which needs to be tracked by the users. They should have a preventative maintenance schedule which generates work orders (tasks) and can also be linked to manually generated work orders for emergency/misc work.

### Parts

These are the components of said assets, the quantity of each of these parts is tracked and maintained above a certain level in the inventory, purchase orders are generated when the stock is too low and needs replenishing. The parts are linked to the work orders where a specified quantity of them will be consumed for the job.

### Work Orders

The tasks that are assigned to users to perform, they can be routine or ad hoc maintenance work required for an asset, work orders are the core of the system as they drive the changes in all the other elements of the system.

### Users

They may be technical staff which can be assigned to fulfil work orders, the amount of hours each user has completed is tracked and their schedule is automatically filled up with tickets (work orders).

## Setup

1. Clone the repository

    `git clone https://github.com/MfonUdoh/CFMS.git`

2. Install the requirements

    `pip install -r requirements.txt`

3. Migrate database

    `python3 manage.py migrate`

4. Create an admin user

    `python3 manage.py createsuperuser`

5. Launch the server

    `python3 manage.py runserver`

6. Login with admin account

    go-to: http://127.0.0.1:8000/admin

7. View website

    go-to: http://127.0.0.1:8000/

To launch on network

1. /CFMS/settings.py ⇒ ALLOWED_HOSTS ⇒ add your host IP to the list
2. `python3 manage.py runserver 0.0.0.0:8000`
3. go to [hostIP]:8000

### Functionality

- Asset overview
- Parts tracking
- Work order posting

### Future Work

- Phone notifications
- User authentification levels
- Sort and search for lists
- Personalised user dashboards
