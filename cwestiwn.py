import csv
import random
import string
from ateb import ateb

class cwestiwn(object):
     openquestions=[]
     input_data=[] 
     cwa=[]
     def __init__(self):
        with open('questions.tsv','r') as tsv:
            self.input_data=[line.strip().split('\t') for line in tsv]
            print("read in the questions\n")
        for i in range(len(self.input_data)):
            a=ateb(self.input_data[i][0],self.input_data[i][1:])
            self.cwa.append(a)

  
     def tweeted_at(self,user,tweettext):
        print(tweettext)
        # set tweet to placeholder
        tweet="notset"
        # go through open questions to check if this might be a response
        for q in self.openquestions:
            if q[0] == user:
               print(q[0])
               print(user)
               tweet=self.check_answer(user,tweettext,q) 
        # it's not a response so ask a new question
        if (tweet=="notset"):
            tweet=self.get_question(user)
        print(tweet)
        return(tweet)

     def get_question(self,user):
        # pick a random number
        r=random.randint(0,len(self.cwa)-1)
        # find the relevant question, positive answer and negative answer
        q=self.cwa[r].que
        a=self.cwa[r].ans
        self.openquestions.append([user,a])
	    
        tweetstring="@"+user+" "+q;
        return(tweetstring)

     def check_answer(self,user,tweettext,a):
        correct=False
        lower_answer=tweettext.lower()
        match_string=lower_answer.translate(None, string.punctuation)
        print(tweettext)
        print(match_string)
        print (a)
        print (a[1])
        print (len(a[1]))
        for i in range(0,len(a[1])-1):
            if match_string==a[1][i].lower():
               correct=True
        if correct==True:
            tweet="@"+user+" bendigedig!"
        else :
            tweet="@"+user+" na sori, yr ateb ywr "
            for i in range(0,len(a[1])-1):
                print i
                tweet+=a[1][i]
                tweet+=", "
            tweet+="neu "
	    tweet+=a[1][-1]
        print(tweet)
        return(tweet)

     def test_q_dataset(self):
        for i in range(0,len(self.cwa)):
             print "question"
             print self.cwa[i].que
             print "answers"
             print self.cwa[i].ans



     def test_q_buffer(self):
         print(self.get_question("user0"))
         print self.openquestions 
         print(self.get_question("user1"))
         print self.openquestions 
         print(self.get_question("user2"))
         print self.openquestions 
