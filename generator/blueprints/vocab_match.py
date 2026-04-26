from generator.languages.phonology import generate_random_word
import random

def create_vocab_match_puzzle():
    concepts = ["water", "fire", "house", "tree", "mountain", "sun", "moon"]
    selected_concepts = random.sample(concepts, 5)
    
    # Create the mapping
    mapping = {c: generate_random_word() for c in selected_concepts}
    
    # Create the problem structure
    problem = {
        "title": "Vocabulary Matching",
        "instructions": "Match the English words to the words in this unknown language.",
        "examples": [{"underlying": eng, "surface": foreign} for eng, foreign in mapping.items()],
        "unknowns": [{"underlying": "cat"}] # You can add more logic here
    }
    return problem
