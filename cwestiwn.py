import csv
import random
import string
from ateb import ateb

class cwestiwn(object):
     openquestions=[]
     input_data=[] 
     cwa=[]
     welldone=[]
     def __init__(self):
        with open('questions.tsv','r') as tsv:
            self.input_data=[line.strip().split('\t') for line in tsv]
        for i in range(len(self.input_data)):
            a=ateb(self.input_data[i][0],self.input_data[i][1:])
            self.cwa.append(a)
        with open('congrats.tsv') as corpus_file:
            self.welldone= corpus_file.readlines()


  
     def tweeted_at(self,user,tweettext):
        print(tweettext)
        # set tweet to placeholder
        tweet="notset"
        # go through open questions to check if this might be a response
        delete=-1
        for i in range(0, len(self.openquestions)):
            if self.openquestions[i][0] == user: # that user has an open question
               tweet=self.check_answer(user,tweettext,self.openquestions[i]) 
               delete=i # keep track of which one you need to delete
        if (delete >= 0) : # it was an answer so delete the question
            del self.openquestions[delete] 
        else : # it's not a response so ask a new question
            tweet=self.get_question(user)
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
        match_string=tweettext.lower()
        match_string = match_string.translate({ord(c): None for c in string.punctuation})
        for i in range(0,len(a[1])):
            if match_string==a[1][i].lower():
               correct=True
        if correct==True:
            congrats=random.choice(self.welldone)
            tweet="@"+user+" "+congrats
        else :
            tweet="@"+user+" na sori, yr ateb yw "
            for i in range(0,len(a[1])-1):
                tweet+=a[1][i]
                tweet+=", "
                tweet+="neu "
            tweet+=a[1][-1]
        return(tweet)

     def test_q_dataset(self):
        for i in range(0,len(self.cwa)):
             print("question")
             print(self.cwa[i].que)
             print("answers")
             print(self.cwa[i].ans)



     def test_q_buffer(self):
         print(self.get_question("user0"))
         print(self.openquestions )
         print(self.get_question("user1"))
         print(self.openquestions )
         print(self.get_question("user2"))
         print(self.openquestions )
