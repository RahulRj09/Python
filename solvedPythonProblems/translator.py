from textblob import TextBlob
def trans(value):
    text = value
    blob = TextBlob(text)
    blob.tags
    blob.noun_phrases
    value = (blob.translate(to="hi"))
    print(value)
