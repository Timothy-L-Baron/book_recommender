"""This program will take user input (asking for book genre) and return a book suggestion (title and author). The data
used for the book selection will be stored in a spreadsheet called book_data.csv. Make the program case insensitive to user input.
Create an error message if they do not pick one of the genres"""

#import module
import string

#create a list of valid genres
genres = ['horror','mystery','classics','fantasy','science fiction','romance','plays']

#open up the .csv file for reading
open_file = open('book_data.csv', 'r')

#get a list of strings, each of which is a single line[row] of the spreadsheet
get_lines = open_file.readlines()

# get user input to obtain which genre they would like and make case insensitive
user_input = input("Please choose a genre (Classics, Fantasy, Horror, Mystery, Plays, Romance, or Science Fiction) \nto receive a book suggestion:")

#write a function that will search the spreadsheet and match up the user input genre with an author and title from the ss and print this out as a suggestion
def get_book_title(str,u_in):
    #loop through each line [row] of the ss, each line is currently a string of title, author, genre
    for line in get_lines[1:]:
        #make everything in the line [row] of the ss lowercase, so that user input is case insensitive
        line = line.lower()
        #strip any \n's from the line
        line = line.strip()
        #change the string into a list of strings where the 3 elements are title, author, genre
        new_lst = line.split(',')
        if u_in in new_lst:
            #x = print('You should check out "{}" by {}.'.format(string.capwords(new_lst[0], sep = None), string.capwords(new_lst[1], sep = None)))
            break
    return print('You should check out "{}" by {}.'.format(string.capwords(new_lst[0], sep = None), string.capwords(new_lst[1], sep = None)))

#if the user input is not a valid genre, prompt them again
while user_input not in genres:
    user_input = input("Please choose a valid genre ---\n(Classics, Fantasy, Horror, Mystery, Plays, Romance, or Science Fiction)\ngenre:").lower()

get_book_title(get_lines, user_input.lower())
