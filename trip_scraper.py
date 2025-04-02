from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def parse_itinerary_by_am_pm(itinerary_text, day_titles_text):
    day_places = []
    for title in day_titles_text.split('\n'):
        if ':' in title:
            place = title.split(':')[1].strip()
            day_places.append(place)

    days = []
    current_day = {
        'day_number': 1,
        'place': day_places[0] if day_places else "Day 1",
        'activities': []
    }
    previous_time_period = None

    for line in itinerary_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if 'AM' in line or 'PM' in line:
            current_time_period = 'AM' if 'AM' in line else 'PM'
            if previous_time_period == 'PM' and current_time_period == 'AM':
                days.append(current_day)
                current_day = {
                    'day_number': len(days) + 1,
                    'place': day_places[len(days)] if len(days) < len(day_places) else f"Day {len(days)+1}",
                    'activities': []
                }
            previous_time_period = current_time_period
            current_day['activities'].append(line)
        elif current_day['activities'] and not line.startswith('USD') and not line.startswith('FREE'):
            current_day['activities'][-1] += "\n" + line

    if current_day['activities']:
        days.append(current_day)

    return days

def scrape_itinerary(destination):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://plantrip.io/")
        wait = WebDriverWait(driver, 60)
        textbox = wait.until(EC.presence_of_element_located((By.ID, "destination")))
        textbox.send_keys(destination)
        button = driver.find_element(By.ID, "generate-itinerary")
        button.click()
        itinerary_container = wait.until(EC.visibility_of_element_located((By.ID, "itinerary-container")))
        time.sleep(10)

        day_titles = driver.find_elements(By.CLASS_NAME, "day-title")
        day_titles_text = "\n".join([title.text for title in day_titles])
        card_bodies = driver.find_elements(By.CLASS_NAME, "card-body")
        itinerary_details_text = "\n".join([card.text for card in card_bodies])

        parsed_days = parse_itinerary_by_am_pm(itinerary_details_text, day_titles_text)
        return {"itinerary": parsed_days}
    finally:
        driver.quit()
