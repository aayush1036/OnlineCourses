# ML-practice - Spam Classifier

This code is intended to classify spam and non spam emails using Naive Bayes algorithm 

In this repository, we are going to 
1. Convert each word to lower case 
2. Tokenize (separate each word)
3. Remove stop words (common words like and/or/the etc) which are just there to signify grammar and they do not add to the meaning in the sentence
4. Remove HTML tags 
5. Word Stemming (eg gone, going, go) because many words are alternate forms of other words and can be treated as one word
6. Remove punctuation as punctuation has no role to play in the email being spam or legitimate 

Formula for Bayes Theorem 

<img src="https://i.ibb.co/yVgLzQg/bayes-theorem.png">

We will use the above formula to calculate the probability of our email being spam or legitimate where A is our word and B is spam/legitimate<br>

Then we repeat the same steps of all the words in the email and we calculate the probability of entire text in the email to be spam by the formula
P(A∩B∩C....) = P(A) * P(B) * P(C)..

Then we repeat the same steps above to calculate P(Word|Leigitimate) for all words in the email and the probability of all entire text in the email to be legitimate 

Then we compare the probabilities and decide which is greater and assign the labels accordingly

Python libraries used 
1. nltk
2. os
3. pandas
4. matplotlib
5. beautifulsoup
6. wordcloud
7. pillow
8. numpy
9. scikitlearn

STRUCTURE OF THE REPOSITORY 
All the data (preprocessing data, training data, testing data) are stored in the SpamData folder<br>

Structure of SpamData folder
1. The data for preprocessing is stored in 01_Processing folder which contains the corpus for training the data, images and icons for making a word cloud, JSON file for the preproccessed data, sample email for practice purpose and a CSV file which has words matched to their word ids
2. The data for training the Naive Bayes classifier is stored in the 02_Training folder which contains the txt file for training data
3. The data for testing the model along with the probabilities of the token is stored in 03_Testing folder 

Then there are three separate notebooks for preprocessing, training and testing the model 

The training data and testing data are also stored as csv files for convinience 


More about me:<br>
[Website](https://aayush1036.github.io/profile_website/)<br>
[Medium Profile](https://aayushmaan1306.medium.com/)<br>
[Github Profile](https://github.com/aayush1036)<br>
[Statsitics and Data science website/blog](https://aayush1036.github.io/statistics/)<br>
[Aayushmaan Jain](mailto:jain_aayushmaan2001@hotmail.com)<br>