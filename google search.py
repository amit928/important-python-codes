import pywhatkit
import wikipedia
import os

def googleSearch(search):
    command_search=str(search)
    command_search=search.replace("mark","")
    command_search=command_search.replace(" in google","")
    command_search=command_search.replace("hey","")
    command_search=command_search.replace("search","")
    command_search=command_search.replace("what is","")
    command_search=command_search.replace("who is","")
    command_search=command_search.replace("who are","")
    command_search=command_search.replace("how to","")
    command_search=command_search.replace("what do you mean by","")

    print(command_search)
    try:
        pywhatkit.search(command_search)
        # wikipedia.search(command_search)
        answer=wikipedia.summary(command_search,2)
        print(f"According to wikipidea : {answer}")
    except Exception as e:
        print("Your answer not found in wikipedia ,Please Search here")

googleSearch("hey mark search who is Amit Kumar Mallick ")

# import webbrowser

# command_search="Narendra Modi"
# url="https://en.wikipedia.org/wiki/"+str(command_search)
# webbrowser.open(url)