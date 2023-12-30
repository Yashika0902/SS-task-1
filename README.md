**Import Libraries:**
Import the requests library for fetching web data.
Import the pandas library for data manipulation and display.

**Define the JSON Data URL:**
Set the URL of the JSON data as a string variable.

**Fetch the JSON Data:**
Use requests to send a GET request to the URL.
Parse the response to JSON format.

**Extract Product Information:**
Access the product data within the JSON structure.

**Process and Sort Data:**
Transform the product data into a list, including attributes like title, price, and popularity.
Sort this list by popularity in descending order.

**Create a DataFrame for Display:**
Use pandas to convert the sorted list into a DataFrame.
Define column names corresponding to product attributes.

**Display the Top Products:**
Show the top entries (like the top 10) from the DataFrame.

**Run the Script:**
Execute the script to see the output.
The script displays the top 10 products from the fetched JSON data, sorted by their popularity in descending order.
