import re
from collections import Counter
with open('stopwords.txt', 'r') as file:
    stopwords=set(file.read().split())
with open('paragraphs.txt', 'r') as file:
    text=file.read()
words = re.findall(r'\b\w+\b', text.lower())
sortedfreq=Counter(word for word in words if word not in stopwords).most_common()
for word, frequency in sortedfreq:
    print(f"{word}: {frequency}")
