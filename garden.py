'''Program designed to : Tokenise each sentence in the list and perform named entity recognition.'''
import spacy
nlp = spacy.load('en_core_web_sm')
#List of sentensis to analyse
garden_path_sentences = ["The NIKE old man the boat.",
                        "The complex houses married and single soldiers and their families.",
                        "Mary gave the child a Band-Aid.",
                        "That Jill is never here hurts.",
                        "The cotton clothing is made of grows in Mississipi."]
# Loop through list to seperate each sentence and tokenise and assign entities
for sentence in garden_path_sentences:
    nlp_sentence = nlp(sentence)
    print("\nSentnece analysis:")
    for token in nlp_sentence:
        print(f"\nToken: {token} || Entity:{token.ent_type_}")

# For each entity answer the following questions:
# What was the entity and its explanation that you looked up?
print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))
# Did the entity make sense in terms of the word associated with it? - YES


