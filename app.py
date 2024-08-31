from operator import index
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import time

def ops1():
    DATA_STORAGE_DIR = "data_store"
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/jobs/search?position=1&pageNum=0")

    jobs = driver.find_elements(By.CLASS_NAME,"base-card")
    print(jobs)
    for idx, job in enumerate(jobs):
        data = job.get_attribute("outerHTML")
        file_path = os.path.join(DATA_STORAGE_DIR, f"job_{idx + 1}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data)
    time.sleep(5)
    driver.close()

def collector1():

    folder = os.listdir("data_storage")
    jobs_dict = {"Title":[],
                "Company":[],
                "Location":[],
                "Link":[]}

    for file in folder:
        try:
            with open(f"data_storage/{file}") as f:
                html_doc = f.read()
            soup = BeautifulSoup(html_doc,"html.parser")
            title =soup.find("h3",attrs={'class':'base-search-card__title'}).get_text()
            Company = soup.find('a',attrs={'class':"hidden-nested-link"}).get_text()
            location =soup.find("span",attrs={'class':'job-search-card__location'}).get_text()
            Link =soup.find("a",attrs={'class':'base-card__full-link'})['href']

            jobs_dict["Title"].append(title.strip())
            jobs_dict["Company"].append(Company.strip())
            jobs_dict["Location"].append(location.strip())
            jobs_dict["Link"].append(Link)

            df= pd.DataFrame(jobs_dict)
            df.to_csv("Data.csv")
        except Exception as e:
            print(e)

def ops2():
    # Load the CSV file
    df = pd.read_csv('Data.csv')

    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Create directory for saving job descriptions if it doesn't exist
    if not os.path.exists("jd"):
        os.makedirs("jd")

    # Iterate over the links in the DataFrame
    for i, link in enumerate(df["Link"]):
        driver.get(link)
        time.sleep(2)  # Give the page time to load
        
        try:
            # Try to find and click the "Show More" button to expand the job description
            button = driver.find_element(By.CLASS_NAME, "show-more-less-html__button")
            button.click()
            time.sleep(1)  # Wait for the content to expand

            # Extract the job description
            data = driver.find_element(By.CLASS_NAME, "details")
            jd = data.get_attribute("outerHTML")

            # Save the job description to an HTML file
            with open(f"jd/{i}.html", 'w', encoding='utf-8') as f:
                f.write(jd)

        except Exception as e:
            print(f"Error processing link {i}: {e}")

        time.sleep(1)  # Small delay before processing the next link

    # Close the WebDriver
    driver.quit()

def collector2():

    # Define CSS class names as constants
    POST_TIME_CLASS = "posted-time-ago__text posted-time-ago__text--new topcard__flavor--metadata"
    JD_CLASS = "show-more-less-html__markup"
    SALARY_RANGE_CLASS = "salary compensation__salary"

    # Initialize dictionary to store extracted data
    job_details = {
        "title": [],
        "company_name": [],
        "company_location": [],
        "posted_duration": [],
        "jd": [],
        "salary": []
    }

    folder= os.listdir("jd")
    for file in folder:
        try:
            # Open and read the HTML file
            with open(f"jd/{file}", 'r', encoding='utf-8') as f:
                html_doc = f.read()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_doc, "html.parser")

            # Extract job details
            title = soup.find("h1", class_="top-card-layout__title").get_text(strip=True)
            company_name = soup.find("a", class_="topcard__org-name-link").get_text(strip=True)
            company_location = soup.find("span", class_="topcard__flavor topcard__flavor--bullet").get_text(strip=True)
            posted_duration = soup.find('span', class_=POST_TIME_CLASS).get_text(strip=True)
            jd_text = soup.find('div', class_=JD_CLASS).get_text(strip=True)
            salary = soup.find('div', class_=SALARY_RANGE_CLASS)
            salary_text = salary.get_text(strip=True) if salary else "Not provided"

            # Append the extracted data to the dictionary
            job_details["title"].append(title)
            job_details["company_name"].append(company_name)
            job_details["company_location"].append(company_location)
            job_details["posted_duration"].append(posted_duration)
            job_details["jd"].append(jd_text)
            job_details["salary"].append(salary_text)

        except Exception as e:
            print(f"An error occurred: {e}")

    # If needed, convert the dictionary to a DataFrame
    job_df = pd.DataFrame(job_details)

    # Output the DataFrame (for example, saving to CSV)
    job_df.to_csv('extracted_job_details.csv', index=False)
