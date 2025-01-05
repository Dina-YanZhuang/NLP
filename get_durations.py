from collections import defaultdict

def get_csv_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

'''
filename = "sentence1.csv"
lines = get_lines(filename)
# print(lines)
'''

def get_durations(lines):
    # Build an empty dic to store words and its duration
    id_durations = defaultdict(int)
    # In .csv file, the first two rows are titles, so start from index[2] row
    for line in lines[2:]:
        lines_list = line.split(';') # each element are seperated by ';'
        id_word = lines_list[2]
        word = lines_list[5].lower() # index[5] is the word, e.g. He, was, ...
        try:
            hz_value = int(lines_list[1]) # index[1] is duration in hz
            ms_value = hz_value / 48
            if (id_word,word) in id_durations:
                id_durations[(id_word,word)] += ms_value
            else:
                id_durations[(id_word,word)] = ms_value
        except ValueError:
            print(lines_list, lines_list[1])
    return id_durations

'''
filename = "sentence1.csv"
lines = get_lines(filename)
words_durations = get_durations(lines)

print(words_durations)
'''