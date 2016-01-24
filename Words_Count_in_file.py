""" Takes an input file of text. Sorts the each word and prints how many time it repeats. Output is in CSV file """

import csv
def read_words(words_file):
    word_count =[]
    word_list = []
    dict_words = {}
    """ Reads a file and assigns to list"""
    with open(words_file, "r") as my_file:
        word_list = my_file.read().split()
        word_list.sort() #sort the word list
    for i in range(len(word_list)):
        word_count.append( word_list.count(word_list[i]) )
        for j in range(len(word_list)):
            
            if word_list[i][0] == word_list[j][0]:
                
                if i == j:                    
                    
                    dict_words.update ({word_list[i][0]+ str(i) + "SW" : [ word_list[i],word_list.count(word_list[i])]})
                else:
                    
                    dict_words.update ({word_list[i][0]+ str(i) :[ word_list[i],word_list.count(word_list[i])] })
                
   
    return dict_words
                
def filter_words_csv(d_words):
    with open('sorted.csv', 'a') as csvfile:
        fieldnames = ['Start_letter', 'Word']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        sorted_d = [[0 for x in range(len(d_words))] for x in range(len(d_words))]
        sd1 =[]
        sd2= []
        counter=0              
        for key in sorted(d_words):
            #print key[0], d_words[key]
            sd1.append(key[0])
            sd2.append(d_words[key])
       
        print "***start**"
        for i in range (len(d_words)-2):
            if( sd2[i] != sd2[i+1]):
                print sd1[i],sd2[i]
                writer.writerow({'Start_letter':sd1[i], 'Word': str(sd2[i][0]) + '  x'+str(sd2[i][1])})


print filter_words_csv (read_words ("ipfile1.txt"))



