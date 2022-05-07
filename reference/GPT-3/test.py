import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

group1 = 'cup is broken.'
group2 = 'faucet has no water.'
group3 = 'cup is dusty.'
group4 = 'cup is missing.'
group5 = 'water is dirty.'
group6 = 'water is hot.'
group7 = 'faucet is broken.'
group8 = 'faucet is turned off.'
group9 = 'sink is not found.'
group10 = 'faucet is dripping.'
group11 = 'faucet is too tight.'
group12 = 'faucet is not found.'
group13 = 'cup is in the box.'
group14 = 'water spills on the ground.'
group15 = 'cup is not full.'
group16 = 'water is drunk by others.'

tagged = nltk.pos_tag(word_tokenize(group1))
print(tagged)