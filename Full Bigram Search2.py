#important preface, if the instructions on the ZS library page don't work, try the following:
#download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#zs for whichever version of windows you have
#then use pip install "file location of the wheel without the quotes"

###POS Unspecified was used for the staub replication
###huge thanks to Lily Houghton and Mariana Dematte for helping me optimize this and troubleshoot

if __name__ == '__main__':

    from zs import ZS
    import math
    import csv
   

    
    z = ZS("G:\Google NGRAMS Corpus\google-books-eng-us-all-20120701-2gram.zs")
    z_1gram = ZS("G:\Google NGRAMS Corpus\google-books-eng-us-all-20120701-1gram.zs")

    if __name__ == '__main__':
        with open('D:\PhD Stuff\Linguistics Stuff\Google NGRAMS\csvtest.csv', newline='') as csvfile_input:
            with open('G:\Google NGRAMS Corpus\Full Bigram.csv', 'w') as csvfile_output:
                bigram_writer = csv.writer(csvfile_output, delimiter=',', lineterminator='\n')
                bigram_writer.writerow(["N1", "N2", "N1POS", "N2POS", "N1 Match Count", "N2 Volume Count", "N2 Match Count", "N2 Volume Count", "Odds Ratio of Match count", "Odds Ratio of Volume Count", "Delta P of Match Count", "Delta P of Volume Count", "Difference Between Odds Ratio and DeltaP Match Count", "Difference Between Odds Ratio and DeltaP Volume Count", "Corpus Size"])
                
                corpus_size = 0
                onegram_memory = {}
                bigram_memory = {}
                for i, item in enumerate (z_1gram.search()):

                    one_gram_string = item.decode('utf-8')
                    one_gram_output = one_gram_string.split('\t')
                    one_gram_match_count = one_gram_output[2]
                    one_gram_volume_count = one_gram_output[3]
                    word = one_gram_output[0]
                    word = word.lower()
                    

                    if i % 10000000 == 0:
                        print(one_gram_string)
                        print(word)
                        print(len(onegram_memory))

                    if len(word.split('_')) == 2:
                        word, POS = word.split('_')

                    else:
                        word = word

                    if word.isalpha():
                        corpus_size = corpus_size + int(one_gram_match_count) #corpus size is a summation of all the match counts of all the words
                        if i % 1000000 == 0:
                            print(word)
                            print(corpus_size)
                        
                        if word in onegram_memory:
                            old_n1_match, old_n1_volume, old_POS = onegram_memory[word]
                            onegram_memory[word] = old_n1_match + one_gram_match_count, old_n1_volume + one_gram_volume_count, POS
                        else:
                             onegram_memory[word] = one_gram_match_count, one_gram_volume_count, POS   

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
                        print(len(bigram_memory))
                    
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
                        if i % 1000000 == 0:
                            print(word1 + " " + word2)
                        if (word1, word2) in bigram_memory:
                            old_output2, old_output3, old_POS1, old_POS2, old_one_gram2, old_one_gram3, old_n2_count2, old_n2_count3 = bigram_memory[(word1, word2)]
                            bigram_memory[(word1, word2)] = (old_output2 + output[2], old_output3 + output[3], word1POS, word2POS, old_one_gram2, old_one_gram3, old_n2_count2, old_n2_count3)
                        
                            
                        else:
                            if word1 not in onegram_memory:

                                print("Warning, " + word1 + " Not in Onegram Corpus!")
                                continue
                                

                            if word2 not in onegram_memory:
                                
                                print("Warning, " + word2 + " Not in Onegram Corpus!")
                                continue

                            
                            n1_match, n1_volume, N1_POS = onegram_memory[word1]
                            n2_match, n2_volume, N2_POS = onegram_memory[word2]
                            bigram_memory[(word1, word2)] = (output[2], output[3], word1POS, word2POS, n1_match, n1_volume, n2_match, n2_volume) 

                                                                  
                for word1, word2 in bigram_memory:
                    
                    bigram_match, bigram_volume, N1_match, N1_volume, N2_match, N2_volume = memory[(word1, word2)]
                    
                    odds_ratio_match = (bigram_match) / (N1_match - bigram_match)
                    odds_ratio_volume = (bigram_volume) / (N1_volume - bigram_volume)
                    deltap_match = (bigram_match / N1_match) - ((N2_match - bigram) / (corpus_size - N1_match))
                    deltap_volume = (bigram_volume / N1_volume) - ((N2_volume - bigram) / (corpus_size - N1_volume))
                    oddsratio_deltap_difference1 = abs(odds_ratio_match - deltap_match)
                    oddsratio_deltap_difference2 = abs(odds_ratio_volume - deltap_volume)

                    bigram_writer.writerow(word1, word2, word1POS, word2POS, N1_match, N1_volume, N2_match, N2_volume, bigram_match, bigram_volume, odds_artio_match, odds_ratio_volume, deltap_match, deltap_volume, oddsratio_deltap_difference1, oddsratio_deltap_difference2, corpus_size)
                
               
                
