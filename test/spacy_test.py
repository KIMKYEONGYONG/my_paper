$ python -m spacy download ja_core_news_sm

import spacy

nlp = spacy.load("ja_core_news_sm")
sentences = "私は今日も学校に行きます。"
doc = nlp(sentences)
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)
