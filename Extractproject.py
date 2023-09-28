import requests
from bs4 import BeautifulSoup
import pandas as pd

page_url = "https://www.bio.org/bio-member-directory" 

response = requests.get(page_url)                                                                                               # Send a GET request to the webpage

soup = BeautifulSoup(response.content, "html.parser")                                                                           # Create a BeautifulSoup object to parse the HTML content

table = soup.find("table", class_="table views-table views-view-table cols-6")                                                  # Find the table element

headers = [th.get_text(strip=True) for th in table.select("thead th a")]                                                        # Extract the table headers

rows = table.select("tbody tr")                                                                                                 # Extract the table rows

data = []                                                                                                                       
for row in rows:                                                                                                                # Iterate over the rows and extract the data
    row_data = [td.get_text(strip=True) for td in row.find_all("td")]
    data.append(row_data)


for i in range (0,80):

    current_page = f"?key=&page={i}”"                                                                                           # Using fstring to get page number because URL does not change for different pages 
    url = page_url + current_page

    response = requests.get(url)                                                                                                # Send a GET request to the webpage

    soup = BeautifulSoup(response.content, "html.parser")                                                                       # Create a BeautifulSoup object to parse the HTML content

    table = soup.find("table", class_="table views-table views-view-table cols-6")                                              # Find the table element

    headers = [th.get_text(strip=True) for th in table.select("thead th a")]                                                    # Extract the table headers

    rows = table.select("tbody tr")                                                                                             # Extract the table rows

    for row in rows:                                                                                                            # Iterate over the rows and extract the data
        row_data = [td.get_text(strip=True) for td in row.find_all("td")]
        data.append(row_data)

df = pd.DataFrame(data, columns=headers)                                                                                        # Create a pandas DataFrame from the extracted data

df.to_excel("data.xlsx", index=False)                                                                                           # Save the DataFrame to an Excel file

