# ReceiptTracker

## Setup and Run Instructions

### Prerequisites
- Python 3.x
- Django (install via `pip install django`)

### Installation
1. Clone the repository:
   
    git clone https://github.com/azizhmd74/ReceiptTracker.git
    cd Test


2. Create a virtual environment (optional but recommended):
( all after installing it - but in my case its already installed)
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'


3. Install dependencies:

    pip install -r requirements.txt
 

4. Apply database migrations:

    python manage.py migrate
 

### Run the Application
1. Start the development server:
 
    python manage.py runserver


2. Open your browser and navigate to (http://127.0.0.1:8000/)

### Additional Steps
- Create a superuser account for admin access:

    python manage.py createsuperuser
- Access the Django admin panel at (http://127.0.0.1:8000/admin/) using the superuser credentials.

  
  ### here u cansee all links possible in this application besides the admin :
User Authentication URLs:
---------------------------

User Registration: http://127.0.0.1:8000/Test/signup
User Login: http://127.0.0.1:8000/Test/login
User Logout: http://127.0.0.1:8000/Test/logout #this one is handled automatically u dont type it 

Receipt-related URLs:
------------------------
Receipt List: http://127.0.0.1:8000/Test/receipt_list
Receipt Detail: http://127.0.0.1:8000/Test/receipt_detail/<receipt_id>/
Receipt Form: http://127.0.0.1:8000/Test/receipt_form/add/

and after deploying the project in render
