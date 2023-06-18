import pytube
url = input("enter video url: ")

path = ""

pytube.Youtube(url).stream.get_higest_resolution().downloead(path)
