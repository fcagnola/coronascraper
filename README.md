# coronascraper
CLI for querying coronavirus world and local cases. ParseHub for scraping content

This is an afternoon project: it is not considered "complete" or "the best version possible". 
Maybe I'll update in the future with more features and perfect the shell calls.

 **USAGE**

Download or clone the repo, download [ParseHub](https://parsehub.com) for scraping (it's free).
Create a new project in ParseHub, the basic tutorial should suffice: the website I used is this: https://www.worldometers.info/coronavirus/
Once you've created the project in Parsehub, simply take not of the relevant keys and tokens and 
insert them in the file "api_parsehub.py".

A shell call from there would look like this:
- World cases:
```
cd <folder where you downloaded coronascraper>
python3 corona.py "world"
```
- National cases and tests:
```
cd <folder where you downloaded coronascraper>
python3 corona.py "italy"
```
- Update Parsehub's scraped page:
```
cd <folder where you downloaded coronascraper>
python3 corona.py "update"
```


