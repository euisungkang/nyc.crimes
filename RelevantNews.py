from pygooglenews import GoogleNews
import json

class News :
    def __init__(self) :
        self.gn = GoogleNews('en', 'US')
       

    def search(self, loc, query, yr) :
        query = self.gn.search(loc + " " + query, from_ = yr + "-01-01", to_ = yr + "-12-31")
        #query = gn.search("Staten Island Crimes", from_ = "2012-01-01", to_ = "2012-12-31")

        print(query['feed'].title)

        return query['entries']