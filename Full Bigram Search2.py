#important preface, if the instructions on the ZS library page don't work, try the following:
#download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#zs for whichever version of windows you have
#then use pip install "file location of the wheel without the quotes"

###POS Unspecified was used for the staub replication

if __name__ == '__main__':

    from zs import ZS
    import math
    import csv
   

    
    z = ZS("D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\google-books-eng-us-all-20120701-2gram.zs")
    z_1gram = ZS("D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\google-books-eng-us-all-20120701-1gram.zs")

    corpus_size = 0
    for item in z_1gram.search():
       corpus_size += 1
    

    if __name__ == '__main__':
        with open('D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\csvtest.csv', newline='') as csvfile_input:
            with open('D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\Full Bigram2.csv', 'w') as csvfile_output:
                bigram_writer = csv.writer(csvfile_output, delimiter=',', lineterminator='\n')
                bigram_writer.writerow(["N1", "N2", "N1POS", "N2POS", "N1 Match Count", "N2 Volume Count", "N2 Match Count", "N2 Volume Count", "Odds Ratio of Match count", "Odds Ratio of Volume Count", "Delta P of Match Count", "Delta P of Volume Count", "Difference Between Odds Ratio and DeltaP Match Count", "Difference Between Odds Ratio and DeltaP Volume Count", "Corpus Size"])
                
                memory = {}
                for i, item in enumerate (z.search()):
                    decoded_string = item.decode('utf-8')
                    output = decoded_string.split('\t')
                    match_count = output[2]
                    volume_count = output[3]
                    year = output[1]
                    bigram = output[0].split(' ')
                    if i % 10000000 == 0:
                        print(decoded_string)
                        print(bigram)
                    
                    if len(bigram[0].split('_')) == 2:
                        word1, word1POS = bigram[0].split('_')
                    else:
                        word1 = bigram[0]
                        word1POS = None
                    if len(bigram[1].split('_')) == 2:
                        word2, word2POS = bigram[1].split('_')
                    else:
                        word2 = bigram[1]
                        word2POS = None
                    word1 = word1.lower()
                    word2 = word2.lower()

                    if word1.isalpha() and word2.isalpha():
                        if (word1, word2) in memory:
                            old_output2, old_output3, old_POS1, old_POS2, old_one_gram2, old_one_gram3, old_n2_count2, old_n2_count3 = memory[(word1, word2)]
                            memory[(word1, word2)] = (old_output2 + output[2], old_output3 + output[3], word1POS, word2POS, old_one_gram2, old_one_gram3, old_n2_count2, old_n2_count3)
                        
                        else:
                            n1_match = 0
                            n1_volume = 0

                            word1_capital = word1.capitalize() #search query doesn't let us ignore case, so we have to account for each combination of capital and lowercase in English
                            word2_capital = word2.capitalize()
                            
                            word1_encoded = word1.encode('utf-8')
                            word2_encoded = word2.encode('utf-8')
                            word1_capital = word1_capital.encode('utf-8')
                            word2_capital = word2_capital.encode('utf-8')

                            for record in z_1gram.search(prefix=word1_encoded): #number of times word1 appears total
                                navy = record.decode("utf-8")
                                one_gram = navy.split("\t")
                                if int(one_gram[1]) >= 1980:
                                    n1_match = n1_match +int(one_gram[2]) #match count
                                    n1_volume = n1_volume +int(one_gram[3]) #volume count
                            for record in z_1gram.search(prefix=word1_capital):  #need to account for capitalization for this as well
                                navy = record.decode("utf-8")
                                one_gram = navy.split("\t")
                                if int(one_gram[1]) >= 1980:
                                    n1_match = n1_match +int(one_gram[2]) #match count
                                    n1_volume = n1_volume +int(one_gram[3]) #volume count

                            n2_count_one = 0
                            n2_count_two = 0
                            for record in z_1gram.search(prefix=word2_encoded): #number of times word1 appears total
                                ship = record.decode("utf-8")
                                n2_gram = ship.split("\t")
                                if int(n2_gram[1]) >= 1980:
                                    n2_count_one = n2_count_one +int(n2_gram[2]) #match count
                                    n2_count_two = n2_count_two +int(n2_gram[3]) #volume count
                            for record in z_1gram.search(prefix=word2_capital):  #need to account for capitalization for this as well
                                ship = record.decode("utf-8")
                                n2_gram = ship.split("\t")
                                if int(n2_gram[1]) >= 1980:
                                    n2_count_one = n2_count_one +int(n2_gram[2]) #match count
                                    n2_count_two = n2_count_two +int(n2_gram[3]) #volume count

                            memory[(word1, word2)] = (output[2], output[3], word1POS, word2POS, n1_match, n1_volume, n2_count_two, n2_count_two) 
                        
                                      
                for word1, word2 in memory:
                    
                    bigram_match, bigram_volume, N1_match, N1_volume, N2_match, N2_volume = memory[(word1, word2)]
                    
                    odds_ratio_match = (bigram_match) / (N1_match - bigram_match)
                    odds_ratio_volume = (bigram_volume) / (N1_volume - bigram_volume)
                    deltap_match = (bigram_match / N1_match) - ((N2_match - bigram) / (corpus_size - N1_match))
                    deltap_volume = (bigram_volume / N1_volume) - ((N2_volume - bigram) / (corpus_size - N1_volume))
                    oddsratio_deltap_difference1 = abs(odds_ratio_match - deltap_match)
                    oddsratio_deltap_difference2 = abs(odds_ratio_volume - deltap_volume)

                    bigram_writer.writerow(word1, word2, word1POS, word2POS, N1_match, N1_volume, N2_match, N2_volume, bigram_match, bigram_volume, odds_artio_match, odds_ratio_volume, deltap_match, deltap_volume, oddsratio_deltap_difference1, oddsratio_deltap_difference2, corpus_size)
                
               
                
