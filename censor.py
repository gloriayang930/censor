# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()

email_two = open("email_two.txt", "r").read()

email_three = open("email_three.txt", "r").read()

email_four = open("email_four.txt", "r").read()



proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]



negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]



def censor_word(text,word):

    censor = ""

    # Make the sensor the same length as the original word (incl spaces).

    for letter in word:

        if letter == " ":

            censor += " "

        else:

            censor += "#"

    result = text.replace(word,censor)

    return result



#print(censor_word(email_one,'learning algorithms'))



for word in proprietary_terms:

  email_two = censor_word(email_two,word)

#print(email_two)



for word in negative_words:

  words = email_three.split(' ')

  for i,w in enumerate(words):

    if w == word:

      words[i+1]='xx'

      email_three = ' '.join(words)

  email_three = censor_word(email_three,word)

#print(email_three)

