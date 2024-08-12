# Flask Data Processing Application

## Overview
This Flask application simulates a simplified data retrieval and processing system. It provides API endpoints to fetch, process, and store data in-memory, simulating interactions with an external service.

## Features
- **/fetch-data**: Simulates fetching data from an external service and processes it.
- **/get-processed-data**: Returns the processed data stored in memory.

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone <repository-url>
cd flask_app
```

### 2. Create and Activate a Virtual Environment
Set up a virtual environment to manage dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the necessary dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application
Start the Flask application by running:
```bash
python run.py
```

### 5. Access the API Endpoints
You can now interact with the API using the following endpoints:
- **Fetch and process data**: `GET http://127.0.0.1:5000/fetch-data`
- **Retrieve processed data**: `GET http://127.0.0.1:5000/get-processed-data`

## Project Structure

```
flask_app/
│
├── app/
│   ├── __init__.py        # Flask application factory
│   ├── routes.py          # API routes and data processing logic
│   └── data_store.py      # In-memory data storage management
│
├── requirements.txt       # Python dependencies
├── run.py                 # Entry point to run the Flask application
└── README.md              # Setup and usage instructions
```

## Notes
- The application uses mock data to simulate fetching from an external service.
- In-memory storage is used to store the processed data temporarily.
- This is a simple demonstration application and is not intended for production use.

## Deployment
To deploy the application on a local machine:
1. Follow the setup instructions above.
2. Ensure Flask is running on `localhost` and the appropriate port (default is 5000).
3. Use tools like Postman or curl to test the API endpoints.
