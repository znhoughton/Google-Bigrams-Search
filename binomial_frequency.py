#important preface, if the instructions on the ZS library page don't work, try the following:
#download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#zs for whichever version of windows you have
#then use pip install "file location of the wheel without the quotes"

import sys
#print(sys.version)
import re
from zs import ZS
#import math
import csv


def binomial_counts(word1, word2):
    if __name__ == '__main__':
        z = ZS("/data/eng-all/google-books-eng-all-20120701-3gram.zs")
        word1 = word1.lower()
        word2 = word2.lower()
        #alpha order variables
        binom_order_alpha1 = (word1 + ' and ' + word2).encode('utf-8')
        binom_order_alpha2 = (word1.capitalize() + ' and ' + word2).encode('utf-8')
        binom_order_alpha3 = (word1.capitalize() + ' and ' + word2.capitalize()).encode('utf-8')
        binom_order_alpha4 = (word1 + ' and ' + word2.capitalize()).encode('utf-8')
        #nonalpha order variables
        binom_order_nonalpha1 = (word2 + ' and ' + word1).encode('utf-8')
        binom_order_nonalpha2 = (word2.capitalize() + ' and ' + word1).encode('utf-8')
        binom_order_nonalpha3 = (word2.capitalize() + ' and ' + word1.capitalize()).encode('utf-8')
        binom_order_nonalpha4 = (word2 + ' and ' + word1.capitalize()).encode('utf-8')
        binomial_match_count = 0
        binomial_volume_count = 0
    ##### alpha order
        for record in z.search(start=binom_order_alpha1 + b"\t1900", stop=binom_order_alpha1 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        for record in z.search(start=binom_order_alpha2 + b"\t1900", stop=binom_order_alpha2 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        for record in z.search(start=binom_order_alpha3 + b"\t1900", stop=binom_order_alpha3 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        for record in z.search(start=binom_order_alpha4 + b"\t1900", stop=binom_order_alpha4 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
    ##### nonalpha order
        for record in z.search(start=binom_order_nonalpha1 + b"\t1900", stop=binom_order_nonalpha1 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        for record in z.search(start=binom_order_nonalpha2 + b"\t1900", stop=binom_order_nonalpha2 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        for record in z.search(start=binom_order_nonalpha3 + b"\t1900", stop=binom_order_nonalpha3 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        for record in z.search(start=binom_order_nonalpha4 + b"\t1900", stop=binom_order_nonalpha4 + b"\t2009"): #search for each binomial count for years after 1900 (up to 2009)
            navy_ship = record.decode("utf-8")
            #print(navy_ship)
            n_gram = navy_ship.split("\t")#separate the string so we can focus on what we care about 
            binomial_match_count = binomial_match_count + int(n_gram[2]) #column 3 gives us "match count"
            binomial_volume_count = binomial_volume_count + int(n_gram[3]) #column 4 gives us "volume count"
            
        return([binomial_match_count, binomial_volume_count])
        
def main():
    if __name__ == '__main__':
        with open('every_binomial_v2.csv', 'rb') as csvfile_input:
            with open('every_binomial_with_frequencies.csv', 'w') as csvfile_output:
                binom_reader = csv.reader(csvfile_input, delimiter=',')
                binom_writer = csv.writer(csvfile_output, delimiter=',', lineterminator='\n')
                binom_writer.writerow(["Word1", "Word2", "Match Count", "Volume Count", "Corpus Size (match count)"])
                #corpus_size = get_corpus_size()
                corpus_size = 323592921465 #instead of re-calculating this number, we'll just use Emily's number since the corpus hasn't changed since then.
                for row in binom_reader:
                    word1 = row[2]
                    word2 = row[3]
                    print(word1, word2)
                    freq = binomial_counts(word1, word2)
                    binom_writer.writerow([word1, word2, freq[0], freq[1], corpus_size])

main()

