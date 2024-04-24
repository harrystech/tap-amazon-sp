
import requests
import zlib

def test_download_stream():
    character_code = 'iso-8859-1'
    url = ""
    document = requests.get(url).content
    print(f"document: {document}")
    document = zlib.decompress(bytearray(document), 15 + 32)
    document = document.decode(character_code)
    
    print(document)
    
    with open("test_doc.txt", "w+", encoding=character_code) as text_file:
        text_file.write(document)
    
    