**War Thunder Camouflage Scraper**
=====================================

**Project Title**
-----------------

A Python web scraper designed to extract camouflage data from War Thunder's website.

**Description**
---------------

I built this to automate the process of collecting camouflage information from War Thunder, saving you time and effort in organizing your vehicle collection. This project utilizes a multi-tab approach for efficient scraping and provides options for downloading image and zip files for offline use.

**Features**
------------

*   **Multi-Tab Scraper**: Utilize up to `X` concurrent tabs to scrape camouflage data from War Thunder.
*   **Data Storage**: Store scraped data in a SQLite database for easy access.
*   **Image and Zip Downloads**: Toggle option to download images and zip files of camouflages directly to your computer.
*   **Headless Mode**: Run the browser in headless mode for silent execution.

**Installation**
---------------

To get started, ensure you have Python 3.7 or later installed on your system. Then, simply:

```bash
pip install -r requirements.txt
```

**Usage**
---------

1.  Clone this repository using `git clone`.
2.  Run the script using `python main.py` (or modify the `main()` function as per your preferences).
3.  Configure the number of concurrent tabs (`--num_tabs`) and output directory for database files (`--output_dir`) using command-line arguments.

**Contributing**
---------------

Feel free to contribute by:

*   Forking this repository.
*   Modifying the code to suit your needs (e.g., adding new features or fixing issues).
*   Submitting pull requests with detailed explanations of changes.

**License**
----------

Released under the [MIT License](LICENSE). Do as you like, but a credit would be nice!

**Tags/Keywords**
-----------------

war thunder, web scraper, camouflage data, multi-tab approach, image and zip downloads, headless mode, python project