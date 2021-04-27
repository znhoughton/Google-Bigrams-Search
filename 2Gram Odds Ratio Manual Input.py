#important preface, if the instructions on the ZS library page don't work, try the following:
#download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#zs for whichever version of windows you have
#then use pip install "file location of the wheel without the quotes"

from zs import ZS
import math

if __name__ == '__main__':
    z = ZS("D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\google-books-eng-us-all-20120701-2gram.zs")
    z_1gram = ZS("D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\google-books-eng-us-all-20120701-1gram.zs")


    print("please type the first word of your compound noun in all lowercase: ")
    word1 = input()
    print("please type the second word of your compound noun in all lowercase: ")
    word2 = input()
    
    word1_capital = word1.capitalize() #search query doesn't let us ignore case, so we have to account for each combination of capital and lowercase in English
    word2_capital = word2.capitalize()
    word1 = word1.encode("utf-8")
    word2 = word2.encode("utf-8")
    word1_capital = word1_capital.encode("utf-8")
    word2_capital = word2_capital.encode("utf-8")
    two_gram_one = 0
    two_gram_two = 0
    for record in z.search(start=word1 + b"_NOUN " + word2 + b"_NOUN\t1980", stop=word1 + b"_NOUN " + word2 + b"_NOUN\t2009"): #search for each 2gram between 1980 and 2009
        navy_ship = record.decode("utf-8")
        n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
        two_gram_one = two_gram_one + int(n_gram[2]) #column 3 gives us "match count"
        two_gram_two = two_gram_two + int(n_gram[3]) #column 4 gives us "volume count"
    for record in z.search(start=word1_capital + b"_NOUN " + word2_capital + b"_NOUN\t1980", stop=word1_capital + b"_NOUN " + word2_capital + b"_NOUN\t2009"): #accounting for capitalization
        navy_ship = record.decode("utf-8")
        n_gram = navy_ship.split("\t")   
        two_gram_one = two_gram_one + int(n_gram[2])
        two_gram_two = two_gram_two + int(n_gram[3])
    for record in z.search(start=word1_capital + b"_NOUN " + word2 + b"_NOUN\t1980", stop=word1_capital + b"_NOUN " + word2 + b"_NOUN\t2009"): #accounting for capitalization
        navy_ship = record.decode("utf-8")
        n_gram = navy_ship.split("\t")   
        two_gram_one = two_gram_one + int(n_gram[2])
        two_gram_two = two_gram_two + int(n_gram[3])
    for record in z.search(start=word1 + b"_NOUN " + word2_capital + b"_NOUN\t1980", stop=word1 + b"_NOUN " + word2_capital + b"_NOUN\t2009"): #accounting for capitalization
        navy_ship = record.decode("utf-8")
        n_gram = navy_ship.split("\t")   
        two_gram_one = two_gram_one + int(n_gram[2])
        two_gram_two = two_gram_two + int(n_gram[3])
    print("This is the match count of " + str(word1.decode('utf-8')) + " " +str(word2.decode('utf-8')) + ": " + str(two_gram_one)) #total sum of match count (total number)
    print("This is the volume count of " + str(word1.decode('utf-8')) + " " + str(word2.decode('utf-8')) + ": " + str(two_gram_two)) #total sum of volume count (number of different environments)

    one_gram_one = 0
    one_gram_two = 0
    for record in z_1gram.search(prefix=word1 + b"_NOUN"): #number of times word1 appears total
        navy = record.decode("utf-8")
        one_gram = navy.split("\t")
        if int(one_gram[1]) >= 1980:
            one_gram_one = one_gram_one +int(one_gram[2]) #match count
            one_gram_two = one_gram_two +int(one_gram[3]) #volume count
    for record in z_1gram.search(prefix=word1_capital + b"_NOUN"):  #need to account for capitalization for this as well
        navy = record.decode("utf-8")
        one_gram = navy.split("\t")
        if int(one_gram[1]) >= 1980:
            one_gram_one = one_gram_one +int(one_gram[2]) #match count
            one_gram_two = one_gram_two +int(one_gram[3]) #volume count
    print("this is the match count of " + str(word1.decode('utf-8')) + ": " + str(one_gram_one))
    print("this is the volume count of " + str(word1.decode('utf-8')) + ": " + str(one_gram_two))
        
    #count((count(gun rights)/count(gun)) / count(gun) - count(gun rights) / count(gun) --> this is the odds ratio
    
    
    P_value = (two_gram_one / one_gram_one)
    oddsratio_col1 = (two_gram_one / one_gram_one) / ((one_gram_one - two_gram_one) / one_gram_one)
    oddsratio_col2 = (two_gram_two / one_gram_two) / ((one_gram_two - two_gram_two) / one_gram_two)
    print("this is our P value of " + str(word1.decode('utf-8')) + " " + str(word2.decode('utf-8')) + ": " + str(P_value))
    
    print("this is the match count odds ratio of " + str(word1.decode('utf-8')) + " " + str(word2.decode('utf-8')) + ": " + str(oddsratio_col1)) #match count odds ratio
    print("this is the volume count odds ratio of " + str(word1.decode('utf-8')) + " " + str(word2.decode('utf-8')) + ": " + str(oddsratio_col2)) #volume count odds ratio
  #this allows us to get an idea of how predictive word1 is of word 2
  #in other words, what are the odds of word2 given word1?
    
    print("this is log match count odds ratio of: " + str(word1.decode('utf-8')) + " " + str(word2.decode('utf-8')) + ": " + str(math.log(oddsratio_col1))) #"log" it to get a more manageable number
    print("this is log volume count odds ratio of " + str(word1.decode('utf-8')) + " " + str(word2.decode('utf-8')) + ": " + str(math.log(oddsratio_col2))) # ^

#apple juice
#apple pie
#orange juice
#internet troll
#tuna sandwich
#game console
#video game
#living room
#living cost
#honey pot
#ice cream
#fan fiction
#camping car
#bowling alley
#bowling pin
#toilet paper
#paper towel
#picture frame


#read file --> run the calculations on all the phrases
#write 
#pandas library

#

