from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/91950/Downloads/Project 127/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scrapped_data = []
stars_data = []
# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup=BeautifulSoup(browser.page_source)
        START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        table_body = bright_star_table.find('tbody')
        table_rows = table_body.find_all('tr')
          # Get data from <td>
        for row in table_rows:
            table_cols = row.find_all('td') # print(table_cols)
            temp_list = []
            for col_data in table_cols:
            # Print Only colums textual data using ".text" property # print(col_data.text)
            # Remove Extra white spaces using strip() method
                data = col_data.text.strip()
                # print(data)
                temp_list.append(data)
                # Append data to star data list scarped_data.append(temp_list)
                scrapped_data.append(temp_list)
        
            for i in range(0,len (scrapped_data)):
                Star_names =  scrapped_data[i][1] 
                Distance = scrapped_data[i][3] 
                Mass = scrapped_data[i][5]
                Radius = scrapped_data[i][6]
                Lum = scrapped_data[i][7]
                required_data = [Star_names, Distance, Mass, Radius, Lum]
                stars_data.append(required_data)
            
# Calling Method    
scrape()
# Define Header
headers = ['star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']
# Define pandas DataFrame
star_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
    

