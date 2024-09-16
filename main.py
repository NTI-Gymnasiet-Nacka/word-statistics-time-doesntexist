# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()

#Räknar antal ord i inputen "sentences"
def wordcounter(sentences):
    counter = 0
    all_words = []
    for row in sentences:
        word_list=row.split()
        for word in word_list:
            if word == "-":
                continue
            else:
    
                counter += 1
                all_words.append(word)
    return counter


def word_list(sentences):
    all_words = []
    for row in sentences:
        word_list=row.split()
        for word in word_list:
            if word == "-":
                continue
            else:
                while word[-1].isalpha() == False:
                    word = word[:-1]
                all_words.append(word.lower())
                
    return all_words


def get_average_wordlength(all_words):
    counter = 0
    for word in all_words:
        word_length = len(word)
        counter = counter + word_length
    average_wordlength = counter/len(all_words)
    return(average_wordlength)


def most_frequent_word(all_words):   
    winner_word = ""
    winner_counter = 0
    for word in all_words:
        counter = 0
        for comp_word in all_words:
            if word == comp_word:
                counter += 1
        if counter > winner_counter:
            winner_word = word
            winner_counter = counter
    return(winner_word, winner_counter)








def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.
    #print(sentences)
    total_words = wordcounter(sentences)
    #print(total_words)
    all_words = word_list(sentences)
    #print(all_words)
    average_wordlength = get_average_wordlength(all_words)
    #print(round(average_wordlength,3))
    winner = most_frequent_word(all_words)
    print(winner)




if __name__ == "__main__":
    main()