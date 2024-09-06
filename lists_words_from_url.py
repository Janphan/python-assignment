from urllib.request import urlopen
def lists_words_from_url():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    word_list = urlopen(url).read().splitlines()


    word_list = [word.decode("utf-8") for word in word_list if word]
    word_count = len(word_list)
    total_word_length = sum(len(word) for word in word_list)
    average_word_length = total_word_length / word_count
    counters = [0] * 23
    for word in word_list:
        word_len = len(word)
        if 1 <= word_len <= 22:
            counters[word_len] += 1
    
    print(f"{word_count} words")
    print(f"The average word length is {average_word_length}")
    print(f"{'Length':>6} {'Count':>5}")
    for i in range(1, 23):
        print(f"{i:>6} {counters[i]:>5}")

lists_words_from_url()    