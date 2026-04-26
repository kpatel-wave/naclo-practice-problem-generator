from generator.blueprints.vocab_match import create_vocab_match_puzzle
import json
import random

def generate_new_problem():
    # Factory picks a random blueprint
    problem = create_vocab_match_puzzle()
    
    # Save it
    filename = f"problem.json"
    with open(filename, "w") as f:
        json.dump(problem, f, indent=2)
    print(f"Generated a new random problem in {filename}")

if __name__ == "__main__":
    generate_new_problem()
