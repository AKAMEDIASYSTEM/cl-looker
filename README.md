# cl-looker
cron script that tweets me when stuff I'm looking for is on craigslist.  

it uses the excellent [python-craigslist](https://github.com/juliomalegria/python-craigslist) library: `pip install python-craigslist` Refer there for most of the documentation you will need.  

To use this, you should alter `terms.json` with the items you are looking for - each object (ie, `{"name": "sickle", "limit": 50}`) can contain keys from the craigslistForSale search params fields.  

You must also alter the `cl-looker.py` script with your own Twitter credentials. The script requires the [tweepy](http://docs.tweepy.org/en/latest/install.html) Twitter library: `pip install tweepy`  

Then either run the script manually, or set up a cronjob to run it, ie:  
`9 18 * * * python3 /home/pi/aka-crons/cl-looker/cl-lathe.py`
