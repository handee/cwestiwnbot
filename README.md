# cwestiwnbot

A bot for helping Welsh learners with question answering.

The file questions.tsv contains the content; it has questions in the first
column, and answers in subsequent columns. A question can have multiple
possible answers.

If the bot is tweeted at, it 
 * if the user who has tweeted @ it has an unanswered question, it checks the tweet to see if it's an answer to that question
 * if they haven't got an unanswered question, it asks a randome question

## Installation

This uses Python and Tweepy. To install, change the contents of
secrets\_example.py to match your own twitter credentials, and rename it to
secrets.py.

To run this with different questions, just replace questions.tsv with a file
that has questions and answers which match your own use case(s)
