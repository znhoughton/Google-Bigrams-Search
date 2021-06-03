#important preface, if the instructions on the ZS library page don't work, try the following:
#download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#zs for whichever version of windows you have
#then use pip install "file location of the wheel without the quotes"

###POS Unspecified was used for the staub replication

if __name__ == '__main__':

    from zs import ZS
    import math
    import csv

    z = ZS("D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\google-books-eng-us-all-20120701-2gram.zs") #import the bigram corpus
    z_1gram = ZS("D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\google-books-eng-us-all-20120701-1gram.zs") #import the 1gram corpus

    corpus_size = 0
    for item in z_1gram.search():
        one_gram_string = item.decode('utf-8') #decode the string
        one_gram_output = one_gram_string.split('\t') #split the string
        one_gram_match_count = one_gram_output[2] #match count
        one_gram_volume_count = one_gram_output[3] #volume count
        word = one_gram_output[0]
        word = word.lower() #case sensitive

        if len(word.split('_')) == 2: #some words are coded as 'cat_NOUN' or 'cat', this line accounts for that
            word, POS = word.split('_')

        else:
            word = word
        
        if word.isalpha(): #no reason to factor numerical values in our corpus size for our task
            corpus_size = corpus_size + int(one_gram_match_count)
    
    
    def two_gram_odds_ratio(word1, word2, word1POS, word2POS): #calculate the odds ratio
        
        if __name__ == '__main__':
            word1 = word1.lower()
            word2 = word2.lower()
            word1_capital = word1.capitalize() #search query doesn't let us ignore case, so we have to account for each combination of capital and lowercase in English
            word2_capital = word2.capitalize()
            word1 = word1.encode("utf-8") #need to encode in order to search
            word2 = word2.encode("utf-8")
            word1_capital = word1_capital.encode("utf-8")
            word2_capital = word2_capital.encode("utf-8")
            two_gram_one = 0
            two_gram_two = 0
            for record in z.search(start=word1 + b" " + word2 + b"\t1980", stop=word1 + b" " + word2 + b"\t2009"): #search for each 2gram between 1980 and 2009
                navy_ship = record.decode("utf-8") #decode the string
                n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
                two_gram_one = two_gram_one + int(n_gram[2]) #column 3 gives us "match count"
                two_gram_two = two_gram_two + int(n_gram[3]) #column 4 gives us "volume count"
            for record in z.search(start=word1_capital + b" " + word2_capital + b"\t1980", stop=word1_capital + b" " + word2_capital + b"\t2009"): #accounting for capitalization
                navy_ship = record.decode("utf-8")
                n_gram = navy_ship.split("\t")   #split the string
                two_gram_one = two_gram_one + int(n_gram[2]) #match count
                two_gram_two = two_gram_two + int(n_gram[3]) #volume count
            for record in z.search(start=word1_capital + b" " + word2 + b"\t1980", stop=word1_capital + b" " + word2 + b"\t2009"): #accounting for capitalization
                navy_ship = record.decode("utf-8")
                n_gram = navy_ship.split("\t")   
                two_gram_one = two_gram_one + int(n_gram[2]) #match count
                two_gram_two = two_gram_two + int(n_gram[3]) #volume count
            for record in z.search(start=word1 + b" " + word2_capital + b"\t1980", stop=word1 + b" " + word2_capital + b"\t2009"): #accounting for capitalization
                navy_ship = record.decode("utf-8")
                n_gram = navy_ship.split("\t")   
                two_gram_one = two_gram_one + int(n_gram[2]) #match count
                two_gram_two = two_gram_two + int(n_gram[3]) #volume count
        
            one_gram_one = 0
            one_gram_two = 0
            for record in z_1gram.search(prefix=word1): #number of times word1 appears total
                navy = record.decode("utf-8") #decode string
                one_gram = navy.split("\t") #split string
                if int(one_gram[1]) >= 1980:
                    one_gram_one = one_gram_one +int(one_gram[2]) #match count
                    one_gram_two = one_gram_two +int(one_gram[3]) #volume count
            for record in z_1gram.search(prefix=word1_capital):  #need to account for capitalization for this as well
                navy = record.decode("utf-8") #decode string
                one_gram = navy.split("\t") #split string
                if int(one_gram[1]) >= 1980:
                    one_gram_one = one_gram_one +int(one_gram[2]) #match count
                    one_gram_two = one_gram_two +int(one_gram[3]) #volume count

            n2_count_one = 0
            n2_count_two = 0
            for record in z_1gram.search(prefix=word2): #number of times word1 appears total
                ship = record.decode("utf-8")
                n2_gram = ship.split("\t")
                if int(n2_gram[1]) >= 1980:
                    n2_count_one = n2_count_one +int(n2_gram[2]) #match count
                    n2_count_two = n2_count_two +int(n2_gram[3]) #volume count
            for record in z_1gram.search(prefix=word2_capital):  #need to account for capitalization for this as well
                ship = record.decode("utf-8") #decode string
                n2_gram = ship.split("\t") #split string
                if int(n2_gram[1]) >= 1980: #restrict the year
                    n2_count_one = n2_count_one +int(n2_gram[2]) #match count
                    n2_count_two = n2_count_two +int(n2_gram[3]) #volume count

            
            #count((count(gun rights)/count(gun)) / count(gun) - count(gun rights) / count(gun) --> this is the odds ratio
        
            if one_gram_one != 0 and one_gram_two != 0:
                P_value = (two_gram_one / one_gram_one)
                oddsratio_col1 = (two_gram_one / one_gram_one) / ((one_gram_one - two_gram_one) / one_gram_one)
                oddsratio_col2 = (two_gram_two / one_gram_two) / ((one_gram_two - two_gram_two) / one_gram_two)
                deltaP_col1 = (two_gram_one / one_gram_one) - ((n2_count_one - two_gram_one) / (corpus_size - one_gram_one))
                deltaP_col2 = (two_gram_two / one_gram_two) - ((n2_count_two - n2_count_two) / (corpus_size - one_gram_two))
                oddsratio_simplified1 = (two_gram_one / one_gram_one)
                oddsratio_simplified2 = (two_gram_two / one_gram_two)
                oddsratio_deltap_difference1 = oddsratio_col1 = deltaP_col1 #this is included so we can find words with the maximum difference between deltaP and oddsratio
                oddsratio_deltap_difference2 = oddsratio_col2 = deltaP_col2
            
        #this allows us to get an idea of how predictive word1 is of word 2
        #in other words, what are the odds of word2 given word1? p(word2|word1)
        
        
            if two_gram_one != 0 and one_gram_one != 0: #this prevents an error due to trying to divide by 0 and doesn't bother returning values for a bigram with no entries
                return(word1.decode('utf-8'), word2.decode('utf-8'), word1POS, word2POS, two_gram_one, two_gram_two, one_gram_one, one_gram_two, P_value, oddsratio_col1, oddsratio_col2, deltaP_col1, deltaP_col2, oddsratio_deltap_difference1, oddsratio_deltap_difference2, n2_count_one, n2_count_two, corpus_size)
            else: 
                return(word1.decode('utf-8'), word2.decode('utf-8'), word1POS, word2POS, two_gram_one, two_gram_two, one_gram_one, one_gram_two, "NA", "NA", "NA", "NA", "NA", "NA", "NA", n2_count_one, n2_count_two, corpus_size)

    if __name__ == '__main__':
        with open('D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\csvtest.csv', newline='') as csvfile_input: #open csv input
            with open('D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\Full Bigram.csv', 'w') as csvfile_output: #open csv output
                my_two_grams_reader = csv.reader(csvfile_input, delimiter=',') #read csv
                my_two_grams_writer = csv.writer(csvfile_output, delimiter=',', lineterminator='\n') #write csv
                my_two_grams_writer.writerow(["N1", "N2", "N1POS", "N2POS", "Match Count of 2gram", "Volume Count of 2gram", "Match Count of N1", "Volume Count of N1", "P Value", "Odds Ratio of Match count", "Odds Ratio of Volume Count", "Delta P of Match Count", "Delta P of Volume Count", "Difference Between Odds Ratio and DeltaP Match Count", "Difference Between Odds Ratio and DeltaP Volume Count", "N2 Match Count", "N2 Volume Count", "Corpus Size"])
                
                for i, item in enumerate (z.search()): #write a csv of the oddsratio
                    decoded_string = item.decode('utf-8')
                    output = decoded_string.split('\t')
                    bigram = output[0].split(' ')
                    if i % 10000000 == 0:
                        print(bigram) #added this to keep an idea on the progress
                    
                    if len(bigram[0].split('_')) == 2:
                        word1, word1POS = bigram[0].split('_') #split the bigram
                    else:
                        word1 = bigram[0]
                        word1POS = None
                    if len(bigram[1].split('_')) == 2:
                        word2, word2POS = bigram[1].split('_')
                    else:
                        word2 = bigram[1]
                        word2POS = None
                
                    if word1.isalpha() and word2.isalpha():
                        odds_ratio = two_gram_odds_ratio(word1, word2, word1POS, word2POS)
                        my_two_grams_writer.writerow(odds_ratio) #write the odds ratio
