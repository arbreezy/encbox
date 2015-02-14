encbox.py is a useful script for remote encryption data storage in Dropbox.  

encbox.py first connects to your Dropbox account , you must have a developer account to have access to Dropbox API, then you will need your app key and app secret.

After the succesful connection,script parse and encrypts the file(s),using the AES encryption.

*The files' names are inserted in a Bloom filter.*