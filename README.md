# Concert Management System
This project is a web-based Concert Management System, inspired by platforms like Ticketmaster, allowing users to dynamically manage concerts and artists. Users can create, edit, delete, and view concert details such as dates, times, venues, and associated artists. The system leverages Django for backend development and its ORM to interact with a relational database.

## Features
- ### Artist Management:
  - Add, view, and delete artists.
- ### Concert Management:
  - Create, view, edit, and delete concert entries.
- ### Dynamic Dropdown Menus:
  - Artist dropdown menus dynamically update based on database changes.
- ### Relational Database Support:
  - One-to-many relationship between artists and concerts.
- ### Cascade Deletions:
  - Deleting an artist automatically removes all associated concerts.

## Project Structure

The primary application logic for this project is located in the myApp folder. This includes the following key files:
- models.py: Defines the database models for artists and concerts.
- views.py: Contains the view functions to handle user input and process database interactions.
- forms.py: Handles form definitions for adding artists and concerts.
- templates/: Contains HTML files, including dynamic elements for dropdown menus.
- admin.py: Registers models to appear in the Django admin interface.
### 1. Models (models.py)
- #### Artist Model:
  - Fields: name (artist name) and description.
  - Represents artists and is displayed in the Django admin interface.
- #### AddConcert Model:
  - Fields: date, time, venue, and artist.
  - Uses a ForeignKey to establish a one-to-many relationship with the Artist model.
  - Includes cascade deletion—removing an artist deletes all their associated concerts.    

### 2. Views (views.py)
- #### Add Artist:
  - Processes user input from the "Add Artist" form to insert new artist records.
  - Uses Django ORM:

    ```
    artists = Artist.objects.all()
    ```
  - This retrieves all artist records from the database.
- #### Create Concert:
  - Processes data from the "Create Concert" form, linking concerts to artists via a dropdown menu.
  - Demonstrates relational database operations with Django ORM.
 
### 3. Templates (```home.html```)
- #### Dynamic Dropdown Menu:
  - Uses a Django template loop to populate the artist dropdown:
    
    ```html
    {% for artist in artists %}
      <option value="{{ artist.id }}">{{ artist.name }}</option>
    {% endfor %}
    ```
  
  - Updates dynamically as new artists are added to the database.

## Demo Walkthrough
1. Adding Artists:
  - Use the "Add Artist" form to input artist details.
  - Save the entry, and the dropdown menu is dynamically updated with the new artist.
2. Creating Concerts:
  - Enter concert details, including the associated artist (selected from the dropdown menu).
  - Save the entry, and the concert details are inserted into the database and displayed in the table.
3. Editing and Deleting Entries:
  - Modify concert or artist details, and updates are saved to the database.
  - Delete entries directly, with cascade deletions ensuring database consistency.

## Installation & Setup
### Prerequisites
- Python 3.8 or higher
- Django 5.1.5
- Virtual Environment (recommended)

### Steps
1. Clone the Repository:

```bash
git clone https://github.com/chandleryang6/CS348-Project.git
cd project_directory
```

2. Set Up a Virtual Environment:

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

3. Install Dependencies:

``` bash
pip install django
```

4. Apply Migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the Development Server:

```bash
python manage.py runserver
```

6. Access the Application: Open your browser and go to:

http://127.0.0.1:8000

## Technologies Used
- Backend: Django (Python), Django ORM
- Frontend: HTML, CSS
- Database: SQLite (default Django database)






