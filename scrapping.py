import requests
from bs4 import BeautifulSoup

# URL of the JoSAA opening and closing ranks page
url = "https://josaa.admissions.nic.in/applicant/SeatAllotmentResult/CurrentORCR.aspx"

# Start a session
session = requests.Session()

# Get the initial page
response = session.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the form data
viewstate = soup.find(id="__VIEWSTATE")["value"]
eventvalidation = soup.find(id="__EVENTVALIDATION")["value"]

# Define the form data payload
payload = {
    "__VIEWSTATE": viewstate,
    "__EVENTVALIDATION": eventvalidation,
    "ctl00$ContentPlaceHolder1$ddlRound": "1",  # Example Round
    "ctl00$ContentPlaceHolder1$ddlInstituteType": "IIT",  # Example Institute Type
    "ctl00$ContentPlaceHolder1$ddlInstitute": "IITKGP",  # Example Institute
    "ctl00$ContentPlaceHolder1$ddlBranch": "AEROSPACE ENGINEERING",  # Example Program
    "ctl00$ContentPlaceHolder1$ddlSeattype": "OPEN",  # Example Seat Type
    "ctl00$ContentPlaceHolder1$btnSubmit": "Submit"
}

# Submit the form with the payload
response = session.post(url, data=payload)
soup = BeautifulSoup(response.content, 'html.parser')

# Scrape the data from the resulting table
table = soup.find("table", {"class": "table-responsive"})
rows = table.find_all("tr")

# Extract the table data
data = []
for row in rows[1:]:  # Skip the header row
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

# Print the extracted data
for item in data:
    print(item)
