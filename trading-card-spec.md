# Trading Card Generator Project Specification (Tier 2)
Marketing Department

## Project Description
Create a dynamic trading card generation system that showcases fellow achievements in an engaging format.

[VIDEO EXAMPLE](https://drive.google.com/file/d/1991jY4Widl5cLsxN4_lNX9rIfePn6aAO/view?usp=sharing) - a possible example of what your program should do 

## Core Requirements
Your script needs to:
1. Scrape all student names and total points from https://pursuit.codetrack.dev/ site from the `Chrome Browser`
2. Store raw data in CSV format
3. Select 12 random fellows from the CSV file
4. Generate creative trading cards via Gemini API
5. Output both JSON data and responsive HTML

**GOTCHAS** 
- The site is dynamic and has pagination, you need to scrape all pages
- Study the Pursuit Codetrack site and understand how it works
- Not all cards in the Pursuit Codetrack have names, you should skip those cards without names without throwing an error. Your program should keep running



## Technical Specifications

### Suggested Libraries
```python
# Core libraries
import os
from dotenv import load_dotenv    # API key management
from selenium import webdriver    # Web automation
from bs4 import BeautifulSoup    # HTML parsing
import csv                       # Data storage
import json                      # JSON processing
from pathlib import Path         # File path handling
import random                    # Random selection
import time                      # Rate limiting
```

### Suggested Function Structure
- `setup_api()`: Configure AI service credentials
- `scrape_student_data(url)`: Comprehensive web scraping
- `save_to_csv(data, filename)`: Data storage
- `select_random_students(filename, num_students)`: Student selection
- `generate_trading_cards(students)`: AI card generation
- `save_json_cards(cards, filename)`: JSON output
- `generate_html(cards)`: HTML/CSS generation
- `validate_card_data(card)`: Data validation

### Card Data Structure
```json
{
  "name": "Student Name",
  "points": 2500,
  "power_rating": 85,
  "special_power": "Debug Master",
  "future_potential": "Future Tech Lead",
  "emoji": "🚀",
  "rarity": "Epic"
}
```

### Rarity Classifications
- Legendary: 4001+ points
- Epic: 2001-4000 points
- Diligent: 1001-2000 points
- Common: 0-1000 points

## Frontend Requirements
- Responsive design (1 card/mobile, 4 cards/desktop)
- Card styling with rarity indicators
- Visual hierarchy for card information
- Smooth hover effects
- Explanatory header section

## Deliverables
1. Complete Python script
2. CSV with raw data
3. JSON file with card details
4. Responsive HTML/CSS creation
5. Proper error handling using try..except blocks

## Technical Resources
- [Python Virtual Environment Setup](https://github.com/jdrichards-pursuit/python-virtual-environment-setup) - remember you do not need to select the ipykernel or select the shell using a .py file
- [Web Scraping In ClassTheory Training](https://github.com/jdrichards-pursuit/week-9.1-web-scraping-and-sentiment-analysis-theory)
- [BeautifulSoup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Python HTML Creation](https://www.geeksforgeeks.org/creating-and-viewing-html-files-with-python/)
- [Gemini API](https://cloud.google.com/vertex-ai/generative-ai/gemini/gemini-1.5-flash)
- [Chrome Browser](https://www.google.com/chrome/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [Python Documentation](https://docs.python.org/3/)
- [CSV Documentation](https://docs.python.org/3/library/csv.html)
- [JSON Documentation](https://docs.python.org/3/library/json.html)
- [Random Documentation](https://docs.python.org/3/library/random.html)
- [Time Documentation](https://docs.python.org/3/library/time.html)

## Technical Stretch Goals

- Rate limiting for web scraping
- Clean data validation
- Responsive design best practices


[Back to Assignment Brief](./readme.md)