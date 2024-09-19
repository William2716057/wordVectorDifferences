import gensim.downloader as api

#twitter model to provide words
model = api.load("glove-twitter-25")

#function for calculating difference between first and second word
def display_vector_difference():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    
    #get vector for each word
    if word1 in model.key_to_index and word2 in model.key_to_index:
        vector1 = model.get_vector(word1)
        vector2 = model.get_vector(word2)
        
        #subtract vector2 from vector1
        difference = vector1 - vector2
        
        print(f"Vector for '{word1}' = {vector1}")
        print(f"Vector for '{word2}' = {vector2}")
        print(f"Difference between '{word1}' and '{word2}' = {difference}")
    else:
        missing_words = [word for word in [word1, word2] if word not in model.key_to_index]
        print(f"Word(s) not found in model: {', '.join(missing_words)}")

if __name__ == "__main__":
    display_vector_difference()
