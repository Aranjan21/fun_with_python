Code Description

This python script will compress the text file. We will be using module zlib and base64 encoder .

problem encounter *--

compressed_data = zlib.compress(data)
TypeError: a bytes-like object is required, not 'str'

In order to compress data we need to convert it to bytes first . Once the data is compressed again we need to encode it to make it useable/accessible

similarly  we need to decode the the while decompressing the file .

We will be using tkinter module to display .
OOPS feature is also used to import modules.
