##print("nessage")

class Tweet:
    def __init__(self,message):
        self.message = message
    def print_tweet(self):
        print (self.message)


t = Tweet('An instance of Tweet')

##Tweet.print_tweet()
##wrong use case name not class name


##self referring to ther instance

Tweet.print_tweet(t)