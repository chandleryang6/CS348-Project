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










