Profanity Detection:
A program to detect the degree of profanity in a file of Twitter tweets, based on a set of specified words that indicate offensive language.

Requirements:
Python 3.x

Usage:
Clone or download the repository
Replace the placeholder ... in the code with a list of words that you consider to indicate offensive language.

Run the program with the following command in the terminal:
python profanity_detection.py <input_file> ,
where <input_file> is the path to the file containing the Twitter tweets.

Output:
The program outputs the degree of profanity for each sentence in the file, where the degree of profanity is calculated as the ratio of the number of offensive words to the total number of words in the sentence.

Assumptions:

The input file contains one tweet per line.
The program uses a simple approach to calculate the degree of profanity by counting the number of slurs in each tweet and dividing by the number of words in the tweet.
The program converts the tweets to lowercase and removes non-alphanumeric characters for consistency.
The program assumes that the list of slurs is provided as a Python list and is case-insensitive.
The program returns a list of tuples, where each tuple contains a tweet and its degree of profanity.

Contributions:
Contributions are welcome! If you find a bug or want to suggest a feature, please open an issue or a pull request.
