import requests
import time
import TwitterOauthAuthentication


class tweets:
    def __init__(self):

      self.url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s'
      self.company_names = [ '#citrix','#ibm','#twitter', '#capitolone','#dell' ]


    def get_tweet(self):
      i=0
      print (i)
      print (self.company_names[0])
      while i < 5:  

        print (i,self.company_names[i])
       
        # POST with form-encoded data

        print (self.url %self.company_names[i] )
        r = requests.get(self.url, data= {'company':self.company_names[i]})


        # Response, status etc
        print (r.message)
        print (r.text)
        print (r.status_code)
        i = i+1



def main():
    """Start running the service to get incident information."""
    bl = tweets()
    while True:
        
        bl.get_tweet()

if __name__ == "__main__":
    main() 
