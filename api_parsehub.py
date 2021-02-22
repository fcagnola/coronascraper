# For this project I used Parsehub's API for automating and retrieving parsed information
# ParseHub is completely free, and provides a project-oriented approach which allows you
# to have a single project token to retrieve the most recent scraped version through APIs.

# These are the URLs for API requests
# GET https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data
# POST https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run

#If you decide to use Parsehub as well fill in your tokens and keys below:

API_KEY = ""
PROJ_TOKEN = ""
RUN_TOKEN = ""
TARGET_URL = "https://www.worldometers.info/coronavirus/"
API_GET_URL = f"https://www.parsehub.com/api/v2/projects/{PROJ_TOKEN}/last_ready_run/data"
API_UPDATE_URL = f"https://www.parsehub.com/api/v2/projects/{PROJ_TOKEN}/run"
