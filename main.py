import wikipedia
import webbrowser

def getPage():
  # 1 means number of random articles
  random_article = wikipedia.random(1)

  # print to the user the choice of random article
  print("The random generated wikipedia article is " + random_article)

  # User input to view the page or not
  choice = input("Continue Loading more info about "
                  + random_article + " (y/n/q)")

  if(choice == 'y' or choice == 'Y'):
    # Prints the summary of the random picked article
    print(wikipedia.summary(random_article, 10, 0
          , auto_suggest=True, redirect=True))
    # user choice to open in webbrowser
    web_browser = input("Do you want to open this in your web browser? (y/n)")
    if (web_browser == 'y' or web_browser == 'Y'):
      wiki_load = wikipedia.page(random_article)
      webbrowser.open(wiki_load.url)
    elif (web_browser == 'n' or web_browser == 'N'):
      exit(0)

  elif(choice == 'n' or choice == 'N'):
    getPage()
  else:
    exit(0)

getPage()
