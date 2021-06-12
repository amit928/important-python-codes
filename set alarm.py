# import datetime
# import playsound

# time=datetime.datetime.now().strftime('%H:%M:%S')
# while time>= str("22:43:00") and time< str("22:43:30"):
#     time=datetime.datetime.now().strftime('%H:%M:%S')
#     playsound.playsound('D:\\music\\alarm ringtone.mp3',True)



# import webbrowser

# x="Salman Khan"
# url="https://google.com/"+x
# webbrowser.open(url)

try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
  
# to search
query = "wikipedia"
  
for j in search(query, tld="co.in", num=20, stop=20, pause=2):
    print(j)