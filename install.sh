sudo pip install requests


# I am using CouchDB to install it:
sudo add-apt-repository ppa:couchdb/stable -y
sudo apt-get update -y
sudo apt-get remove couchdb couchdb-bin couchdb-common -yf
sudo apt-get install -V couchdb
sudo stop couchdb
sudo start couchdb
sudo pip install couchdbkit
#If you want email notifier for exceptions and Add it to Config filey
sudo pip install bugsnag
