encbox is a useful script for remote encryption data storage for Dropbox.  

encbox.py first connects to your Dropbox account , you must have a developer account to have access to Dropbox API, then you will need your API keys.

After the succesful connection,script parse and encrypts the file(s),using AES encryption.

*The files' names are inserted in a Bloom filter.*

decbox.py download an encrypted file(s) from your dropbox account and then decrypt it locally.

TIP: your passwords *must* be the same for encryption and decryption  