import spacy
nlp = spacy.load('en_core_web_lg')

# Gloabl variable: The score of the movie most similar
similarity_num = 0 

# Global variable: The index of the most similar movie from movies.txt list
index = 0   

def movie_suggestions(description):
    """Function takes in a description and returns a movie suggestion description
    :param description: Description of last viewed movie
    :type description: string
    ...
    ...
    :return: title[0]: The title of the most similar movie
    :rtype: string
"""
    global index
    global similarity_num

    with open('movies.txt', 'r') as file:
        contents = file.read()

        # Splitting file into sentences
        sentences = contents.split('\n')
       
       # Looping through sentences and checking similarity to description
        for i, sentence in enumerate(sentences):
            doc_sentence = nlp(sentence)
            doc_description = nlp(description)
            similarity_score = doc_sentence.similarity(doc_description)
            
            # If the current similarity score is higher than the gobal similarity number, updating similarity number and index to current
            if similarity_score > similarity_num:
                similarity_num = similarity_score
                index = i
        
        print(index)
        print(similarity_num)
        print(sentences[index])

        # Splitting the title from the most similar movie and returning it
        title = sentences[index].rsplit(':')

        print(title[0])
        return title[0]



description = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

movie_suggestions(description)