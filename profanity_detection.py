import re

def calculate_profanity_level(sentence, words):
    """
    Calculates the profanity level of a sentence based on the number of racial slurs found in it.
    :param sentence: The sentence to be evaluated.
    :param words: A set of words that indicate racial slurs.
    :return: The profanity level of the sentence.
    """
    profanity_level = 0
    for word in words:
        profanity_level += len(re.findall(r'\b' + word + r'\b', sentence))
    return profanity_level

def profanity_analysis(tweet_file, words):
    """
    Analyzes the profanity level of all tweets in a file.
    :param tweet_file: The file containing the tweets.
    :param words: A set of words that indicate racial slurs.
    :return: A list of tuples, each containing the tweet and its corresponding profanity level.
    """
    results = []
    with open(tweet_file, 'r') as f:
        for line in f:
            tweet = line.strip()
            profanity_level = calculate_profanity_level(tweet, words)
            results.append((tweet, profanity_level))
    return results

def main():
    words = {"racial", "slur", "hate", "bigotry", "discrimination", "prejudice", "intolerance"}
    tweet_file = 'tweets.txt'
    results = profanity_analysis(tweet_file, words)
    for tweet, profanity_level in results:
        print(f'Tweet: {tweet}\nProfanity level: {profanity_level}\n')

if __name__ == '__main__':
    main()
