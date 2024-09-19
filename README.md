# Word Vector Difference Calculator
A simple Python script that computes the difference between the word vectors of two input words using the GloVe (Global Vectors for Word Representation) model trained on Twitter data. It leverages the Gensim library to load the model and perform vector operations.

## Features
- Load pre-trained GloVe Twitter embeddings (25-dimensional).
- Calculate and display the vector representation of two user-input words.
- Compute and print the difference between the two word vectors.
- Inform the user if any of the input words are not found in the model's vocabulary.

## Requirements
- Python 3.x
- Gensim library
- Installation

1. Clone this repository:
```
git clone https://github.com/William2716057/wordVectorDifferences.git
```
2. Install the required libraries:
```
pip install gensim

```
## Usage 
Run the script using Python:
```
python wordVectorDifferences.py
```
Enter the first and second word into the prompt

1. Retrieve the vectors for the input words.
2. Compute the difference between the two vectors.
3. Display the vectors and their difference.

## Example
```
Enter first word: king
Enter second word: queen
Vector for 'king' = [0.1, -0.2, ...]
Vector for 'queen' = [0.2, -0.1, ...]
Difference between 'king' and 'queen' = [-0.1, -0.1, ...]
```
