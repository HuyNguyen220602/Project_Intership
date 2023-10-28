import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

# Input text
text = "Natural Language Processing is a fascinating field!"

# Tokenization
tokens = word_tokenize(text)

# Text preprocessing
tokens = [token.lower() for token in tokens if token.isalpha()]    # Convert to lowercase and remove non-alphabetic tokens
tokens = [token for token in tokens if token not in stopwords.words('english')]    # Remove stopwords

# Part-of-speech tagging
pos_tags = pos_tag(tokens)

# Print the tokens and their POS tags
for token, pos in pos_tags:
    print(f"{token}: {pos}")