import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from app import ops1, ops2,collector1, collector2

def main():
    # Step 1: Scrape job listings and save them as HTML files
    ops1()
    
    # Step 2: Store the collected data 
    collector1()
    
    # Step 3: Scrape job details from the stored data 
    # and save them as HTML files
    ops2()

    # Step 4: Store the collected data into csv format
    collector2()

if __name__ == "__main__":
    main()
