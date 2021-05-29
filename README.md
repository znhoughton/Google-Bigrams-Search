# Google-Bigrams-Search

Special thanks to Lily Houghton and Mariana Dematte for their invaluable help in optimizing these scripts so they don't take 5 years to run.

Please note that these scripts are designed to work on Python 2.7.16 (as the ZS package is not compatible with Python 3.0 and above). 

The various python scripts in this repository are designed to make corpus research a lot easier, specifically for searching the google ngrams corpus. The scripts rely on the Python package "ZS," details about installing it can be found at the top of each script.

A short summary describing each program is included below:

**2Gram Odds Ratio Manual Input**

   You can use this script to manually input two words (bigram) and receive their match counts, volume counts, and 
   odd ratio (how predictive of N2 is N1). 
   The script should be easy enough to modify for similar purposes.

**2 Grams Odds Ratio Write CSV (POS unspecified/Noun Specified)**

   Similar to the manual input but has been modified to run across an entire .csv in order to make it more convenient for mass searches. 
   There are two versions: one which specifies the part of speech (Noun specified) and one that does not specify the part of speech.
    
**Full Bigram Search2**

   This program searches the entire google corpus (1gram and 2gram) in order to calculate odds ratio and deltaP for each bigram. Note that it takes ~30 hours for the program to complete on my computer with 32gb of RAM and may take longer or shorter depending on your computer.
   
**Full Bigram Compound Noun Search**

   This program is pretty much the same as the Full Bigram Search but is restricted to compound nouns.
   
**Acknowledgements**

Again, a huge shout out to Lily Houghton and Mariana Dematte.

Additionally, if you use any of these programs for scientific research, please cite the following papers:

The paper on ZS: 

Smith, N. J. (2014). ZS: A file format for efficiently distributing, using, and archiving record-oriented data sets of any size. *Manuscript submitted for publication. School of Informatics, University of Edinburgh. Retrieved from http://vorpus.org/papers/draft/zs-paper.pdf.*

My paper employing these scripts:






