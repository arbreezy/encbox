#!/usr/bin/python
#lets import the dropbox module
import dropbox
from Crypto.Cipher import AES
import hashlib
import sys ,getpass

leng=len(sys.argv)-1

if leng == 0:
    print("No files for encryption.")
    print("Try './encbox /path/to/file'\nQuiting!")
    sys.exit(1)

#taking the app key and secret 
key=raw_input('Enter your app key : ')
secret=raw_input('Enter your app secret : ')
#initializing the flow 
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(key,secret)

#we are ready to start the connection, so we can generate our token
authorize_url = flow.start()

print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'

code = raw_input("Enter the authorization code here: ").strip()

#then we copy/paste the token from the website
# This will fail if the user enters an invalid authorization code

access_token,user_id= flow.finish(code)
client = dropbox.client.DropboxClient(access_token)
print 'The account has been linked successfully'
