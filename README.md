# Google-Bigrams-Search

Special thanks to Lily Houghton and Mariana Dematte for their invaluable help in optimizing this program

The various python scripts in this repository are designed to make corpus research a lot easier. Specifically, these scripts are designed for searching the google ngrams corpus. The scripts rely on the Python package "ZS," details about installing it can be found at the top of each script.

A short summary describing each program is included below:

**2Gram Odds Ratio Manual Input**

   You can use this script to manually input two words (bigram) and receive their match counts, volume counts, and 
   odd ratio (how predictive of N2 is N1). 
   The script should be easy enough to modify for similar purposes.

**2 Gramds Odds Ratio Write CSV (POS unspecified/Noun Specified)**

   Similar to the manual input but has been modified to run across an entire .csv in order to make it more convenient for mass searches. 
   There are two versions: one which specifies the part of speech (Noun specified) and one that does not specify the part of speech.
    
**Full Bigram Search2**

   This program searches the entire google corpus (1gram and 2gram) in order to calculate odds ratio and deltaP for each bigram.
