#!/usr/bin/env python3
import zlib,base64

''' This module will compress the file provided '''

def compress(inputfile,outputfile):

    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, 'UTF-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    compressed_file = open(outputfile,'w')
    compressed_file.write(compressed_data.decode('UTF-8'))

def decompress(inputfile,outputfile):
    compressed_data = open(inputfile,'r').read()
    decompress_data = zlib.decompress(base64.b64decode(compressed_data))
    decoded_data = decompress_data.decode('UTF-8')
    decompress_file = open(outputfile,'w')
    decompress_file.write(decoded_data)
    decompress_file.close()

#compress('file_to_be_compressed.txt','compressed_file')
decompress('compressed_file','file_to_be_compressed.txt')
