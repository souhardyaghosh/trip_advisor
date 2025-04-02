# trip_advisor
Currently a offline flask based script to give you Trip Plans with the help of Scrapping

# Trip Itinerary Generator

This project is a web application that generates travel itineraries based on user input. It scrapes itinerary details from an external website using Selenium and presents them in a structured format.

## Features
- Users can input their destination, number of days, and trip type.
- The application scrapes travel plans and structures them into a day-wise itinerary.
- Built with Flask for the backend and Selenium for web scraping.
- The frontend is a simple HTML form that displays the fetched itinerary.

## Screenshots

### Home Page
![Screenshot 1](https://raw.githubusercontent.com/souhardyaghosh/trip_advisor/main/ss1.png)

### Destination Page
![Screenshot 2](https://raw.githubusercontent.com/souhardyaghosh/trip_advisor/main/ss2.png)

### Booking Page
![Screenshot 3](https://raw.githubusercontent.com/souhardyaghosh/trip_advisor/main/ss3.png)


## Installation and Setup

### Prerequisites
Make sure you have Python installed (preferably Python 3.7+).

### Install Required Dependencies
Run the following command to install all necessary dependencies:
```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, install these manually:
```bash
pip install flask selenium webdriver-manager
```

### WebDriver Setup
Ensure you have Google Chrome installed. Selenium will manage the Chrome WebDriver automatically via `webdriver-manager`.

## Running the Application
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/trip-itinerary.git
   cd trip-itinerary
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
```
trip-itinerary/
│── app.py               # Main Flask application that handles routing and rendering
│── trip_scraper.py      # Web scraping logic using Selenium to fetch itinerary data
│── templates/
│   └── index.html       # HTML template for the frontend
│── static/              # Contains CSS, JS, images (if needed)
│── requirements.txt     # List of required Python dependencies
│── README.md            # Project documentation
```

### File Descriptions
- **app.py**: This is the main application file. It runs a Flask web server, accepts user input, calls the scraping function, and renders the HTML template.
- **trip_scraper.py**: This file contains the Selenium-based web scraping logic that extracts itinerary details from an external travel planning website.
- **templates/index.html**: This is the frontend template where users enter their trip details and view the generated itinerary.
- **static/**: This directory is reserved for static files like CSS, JavaScript, or images if needed.
- **requirements.txt**: Lists all required Python libraries to be installed for running the project.
- **README.md**: Contains documentation for installation, usage, and project details.

## Troubleshooting
- If you face an error related to ChromeDriver, ensure that Chrome is installed and up to date.
- If running on Linux, you may need to install additional dependencies for Selenium:
  ```bash
  sudo apt-get install -y chromium-chromedriver
  ```

## Author
**Made by Souhardya**

## License
This project is licensed under the MIT License.

