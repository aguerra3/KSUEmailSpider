# KSUEmailSpider

This Scrapy-based web scraper is designed to navigate through the kennesaw.edu domain, extract email addresses, and analyze the text content of the pages. The main functionalities include:

Exploration: The scraper initiates from a specified starting URL within the kennesaw.edu domain and follows links to other pages within the same domain, ensuring comprehensive coverage.

Email Extraction: As the scraper processes each page, it uses regular expressions to identify and extract email addresses. These email addresses are stored in a list for further use or analysis.

Word Count and Frequency Analysis: The scraper collects the text content of each page, tokenizes it into individual words, and counts the frequency of each word. This data is stored in a dictionary where keys are words and values are their corresponding counts.

Data Storage: The extracted email addresses and word frequency data are stored in CSV files for easy access and further analysis.

Visualization: Using Matplotlib, the collected word frequency data is plotted in both linear and logarithmic scales to provide insights into the distribution and occurrence of words across the domain.
