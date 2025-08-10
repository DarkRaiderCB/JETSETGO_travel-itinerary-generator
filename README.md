# **JetSetGo** - Personalized Travel Itinerary Generator

### **Live Link**
Click <a href='https://sanyogmishra.pythonanywhere.com/'>here</a> to access the website. [NO LONGER AVAILABLE; 3 MONTH DURATION EXHAUSTED]

### **Overview**
This Django-based web application generates personalized travel itineraries based on user preferences such as destination, budget, and activities. It integrates Google Gemini API for itinerary generation and scrapes images from Wikimedia to visually enhance the itineraries.

### **Features**
- **Personalized Itineraries**: Tailored travel plans based on user inputs like budget, trip duration, and preferred activities.
- **AI-Powered Recommendations**: Uses Google Gemini API to generate detailed itineraries, including hotel, transport options, and must-visit places.
- **Wikimedia Image Scraping**: Automatically retrieves images of destinations from Wikimedia to provide a richer experience.
- **Admin Dashboard**: Allows admins to manage users and monitor application activities.
- **User Authentication**: Users can register and log in to save their travel itineraries and retrieve them later.
- **Guest Mode**: New users can try the platform without signing up for up to two times.
- **Responsive Frontend**: The application offers a modern user interface built with HTML, CSS, and JavaScript.

### **Tech Stack**
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **APIs**:
  - **Google Gemini API**: For generating AI-driven travel itineraries.
  - **Wikimedia API**: To scrape destination images.
- **Database**: SQLite3 (Django default)
- **Web Scraping**: BeautifulSoup and requests for scraping images.

### **Project Structure**
- **db.sqlite3**
- **itinerary/**
  - **admin.py**
  - **forms.py**
  - **models.py**
  - **views.py**
  - **utils.py**
  - **static/**
  - **templates/**
  - **urls.py**
  - **tests.py**
- **travel_itinerary/**
  - **asgi.py**
  - **settings.py**
  - **urls.py**
  - **wsgi.py**

### **Setup and Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DarkRaiderCB/Random-Stuff.git
   cd travel_itinerary
   ```

2. **Install dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the `itinerary` folder and add the following:
     - `API_KEY`: Your API key for Google Gemini.

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000` to use the application.

### **Usage**
- **Generate an Itinerary**: Users can generate a personalized travel itinerary by entering preferences such as destination, travel dates, budget, and activities. The system will provide a day-by-day plan, with links to hotel and transport options.
- **Guest Mode**: First-time users can try generating itineraries up to two times without creating an account.
- **Wikimedia Image Integration**: The application automatically fetches images of the destination using Wikimedia's API and embeds them into the itinerary.
- **Admin Dashboard**: Admins can access a dashboard for managing users and overseeing the application’s data.

### **Environment Variables**
To run this project, you will need to set up the following environment variable in your `.env` file:
- `API_KEY`: Your Google Gemini API key for generating itineraries.

### **API Integrations**
- **Google Gemini API**: The primary API for generating personalized travel itineraries based on user input.
- **Wikimedia API**: Scrapes images relevant to the destination to enhance the itinerary visually.


## Thankyou for visiting!
