import nltk
from nltk.corpus import wordnet as wn
import csv

# Tải dữ liệu WordNet
nltk.download('wordnet')

# Mở file CSV để ghi dữ liệu
with open('wordnet_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['word', 'part_of_speech', 'definition', 'example'])

    # Lặp qua tất cả các từ trong WordNet
    for synset in wn.all_synsets():
        word = synset.name().split('.')[0]  # Lấy tên từ
        part_of_speech = synset.pos()       # Loại từ (noun, verb, adj, adv)
        definition = synset.definition()    # Định nghĩa
        examples = ', '.join(synset.examples())  # Ví dụ

        # Ghi dữ liệu vào CSV
        writer.writerow([word, part_of_speech, definition, examples])

print("Dữ liệu WordNet đã được chuyển đổi thành công vào file 'wordnet_data.csv'.")