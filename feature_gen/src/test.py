import sys
sys.path.append("../")

from preprocess import text_preprocess
from feature_repo import bag_of_words, tokenizer
from model_repo import model_repo

def main():
    url = "https://clinicaltrials.gov/ct2/show/NCT03254875?cond=Cancer&rank=1"

if __name__ == '__main__':
    main()