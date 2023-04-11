import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dic)

word = input("Enter word for it's nato spellings: ").upper()
answer_list = [data_dic[letter] for letter in word]
print(answer_list)
