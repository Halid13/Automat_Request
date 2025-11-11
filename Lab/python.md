# Provided context

The goal is to write a Python script that retrieves **user data** from a public API, processes it, and generates a report.  
This exercise simulates a basic automation or integration task an IT engineer might perform (e.g., collecting user information from an external service).
# Exercise

Write a Python script named **`fetch_users.py`** that:
	1. Makes a GET request to the public API: https://jsonplaceholder.typicode.com/  on **/users**
1. Parses the JSON response and extracts the following fields for each user:
    - `name`
    - `username`
    - `email`
    - `company.name`
2. Saves this data to a CSV file named `users_report.csv` with the following columns:
    `Name,Username,Email,Company`
3. Displays in the console a summary with:
    - the total number of users
    - the list of all company names (unique, sorted alphabetically)
    Example: `Total users: 10 Companies: [Deckow-Crist, Romaguera-Crona, ...]`
4. Add error handling for cases where:
    - the API request fails (network error or HTTP status not 200)
    - the JSON response is invalid
    - the CSV file cannot be written
