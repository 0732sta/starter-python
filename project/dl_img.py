import urllib.request

def dl_jpg(url,file_path,file_name):
    full_path=file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)

url=input('Enter ing URL to dowload: ')
file_name =input('Enter file name to save as:')

dl_jpg(url, 'images/',file_name)