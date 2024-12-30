# Content Expiry Notifier

Managing content with expiration dates can be challenging, especially when deadlines are crucial. Forgetting about an upcoming expiration can lead to missed opportunities, financial losses, or unnecessary stress. The Content Expiry Notifier is a MicroSaaS application designed to tackle this problem by providing a simple, intuitive platform to track and manage expiring content.

# Setup Instructions
  1. Before starting, ensure you have the following installed:
      Python (version 3.7 or higher)
      pip (Python's package manager)
  
  2. Set Up a Virtual Environment (Optional but Recommended)
      Create a virtual environment
     Activate the virtual environment
     
  4. Install Dependencies
     
     
         pip install -r requirements.txt
  6. Initialize the Database
      This will create a content.db file in your project directory
      
         python -c "from app import init_db; init_db()"

  7. Run the Application

           python app.py
  8. Access the Application
     
           http://127.0.0.1:5000


# Features overview

    ## Features
    **Add Content**: Enter title, description, and expiry date for any content.
    **Manage Content**: View all content in a list and delete unwanted items.
    **Expiry Alerts**: Automatically identify and highlight content expiring within 3 days.
    **Detail View**: View comprehensive details of individual content items.

# Screenshots
![VScode environment](https://github.com/user-attachments/assets/278bfd92-5039-4e71-9e4b-3036214cf9dc)
![HomePage](https://github.com/user-attachments/assets/cada2c02-7188-4d08-bbf7-932b20ed4779)
![Adding-Content](https://github.com/user-attachments/assets/40e13028-4bac-4888-817f-1b18d4415d64)
![ListOfContent](https://github.com/user-attachments/assets/10cc3396-7fc9-4d41-98fe-147dd2e1dd45)
![AboutContent](https://github.com/user-attachments/assets/8acee386-cc3b-41c8-9170-78656898b17c)

# Technologies Used
    Backend: Flask
    Frontend: HTML, CSS (Bootstrap optional)
    Database: SQLite

# Add Your Code

Include app.py, templates/ (for HTML files), static/ (for CSS/JS if any), and a requirements.txt file for Python dependencies.



