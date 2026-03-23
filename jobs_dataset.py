import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    data = []
    print(f"Found {len(job_cards)} jobs. Starting deep scraping...")

    for card in job_cards:
        # Extract basic info from the main page
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        
        # Get detail page URL
        links = card.find_all("a")
        detail_url = links[1]['href']

        # Request and parse the detail page for description
        detail_res = requests.get(detail_url)
        detail_soup = BeautifulSoup(detail_res.text, "html.parser")
        description = detail_soup.find("div", class_="content").find("p").text.strip()

        data.append([title, company, location, description, detail_url])
        print(f"Scraped: {title}")
        
        # Optional: short delay to prevent server overload
        # time.sleep(0.1)

    # Save data to a rich CSV file
    with open("detailed_jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "URL"])
        writer.writerows(data)

    print("\nDone! CSV saved successfully.")
else:
    print("Failed to retrieve the page")