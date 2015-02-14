#!/usr/bin/python
#lets import the dropbox module
import dropbox
from Crypto.Cipher import AES
import hashlib
import sys ,getpass
import os ,random ,struct

leng=len(sys.argv)-1

if leng == 0:
    print("No files for encryption.")
    print("Try './encbox /path/to/file'\nQuiting!")
    sys.exit(1)


def encrypt_file(key,in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            Encrypted file
        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """

   
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
   

#taking the app key and secret 
key=raw_input('Enter your app key :')
print
secret=raw_input('Enter your app secret :')
print
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
print
print "Give a srong password to generate the key for AES encryption"
password=getpass.getpass()
key = hashlib.sha256(password).digest()
# encrypt the file(s)

for i in range(leng):
	encrypt_file(key,sys.argv[i+1])
	#and we upload it
	encrypted_file=''.join([sys.argv[i+1],'.enc'])
	f = open(encrypted_file, 'rb')
	response = client.put_file(encrypted_file, f)
	#remove the local encryption file
	os.remove(encrypted_file)
	print 'uploaded: ', response
