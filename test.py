from cwestiwn import *

botname="cwestiwnbot"
c=cwestiwn()

c.test_q_dataset()
c.test_q_buffer()

text="@cwestiwnbot Ydy"
print(text)
atstring="@"+botname+" "
usertext=text.replace(atstring,"") 
print usertext
print text

print "tweeting ydy from user1"
print c.tweeted_at('user1','Ydy!')
print "tweeting ydy from user0"
print c.tweeted_at('user0','Ydy!')
print "tweeting ydy from user2"
print c.tweeted_at('user2','Ydy!')
