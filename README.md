# LinkedIn Job Scraper

This project is a web scraping application designed to extract job listings and detailed job descriptions from LinkedIn using Python, Selenium, and BeautifulSoup. The data is saved in HTML files and CSV format for further analysis.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Data Storage](#data-storage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Scrapes job listings from LinkedIn and stores them as HTML files.
- Extracts relevant job data such as title, company, location, and job description.
- Stores the extracted data in CSV format for easy access and analysis.
- Handles pagination and "Show More" buttons to capture complete job descriptions.

## Project Structure

```

LinkedIn-Job-Scraper/
│
├── app.py # Main scraping logic for jobs and descriptions
├── pipeline.py # Pipeline that integrates all scraping steps
├── requirements.txt # Python dependencies
├── README.md # Project overview and usage guide
├── data_store/ # Directory to store scraped job HTML files
│ ├── job_1.html
│ ├── job_2.html
│ └── ...
├── jd/ # Directory to store job description HTML files
│ ├── 0.html
│ ├── 1.html
│ └── ...
└── Data.csv # CSV file containing summarized job data
└── extracted_job_details.csv # CSV file containing detailed job descriptions

```

## Setup and Installation

### Prerequisites

- Python 3.7+
- Chrome WebDriver (Ensure it matches your Chrome browser version)
- Git (optional, for cloning the repository)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/LinkedIn-Job-Scraper.git
   cd LinkedIn-Job-Scraper
   ```

````

2. **Install Dependencies:**
   Make sure you have `pip` installed. Run the following command to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Chrome WebDriver:**
   - Download the Chrome WebDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/).
   - Ensure the WebDriver executable is in your PATH or place it in the project directory.

## Usage

1. **Run the Scraper:**

   ```bash
   python pipeline.py
   ```

2. The scraper will perform the following steps:
   - Scrape job listings and save them in `data_store/`.
   - Extract basic job details and save them in `Data.csv`.
   - Scrape detailed job descriptions and save them in `jd/`.
   - Extract job description data and save it in `extracted_job_details.csv`.

## Data Storage

- **data_store/**: Contains HTML files of job listings.
- **jd/**: Contains HTML files of job descriptions.
- **Data.csv**: Stores basic job details extracted from the listings.
- **extracted_job_details.csv**: Stores detailed job descriptions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

---

Replace `https://github.com/your-username/LinkedIn-Job-Scraper.git` with your actual GitHub repository link. You can also modify the descriptions, project structure, and setup instructions according to your project's specific details.
```
````
