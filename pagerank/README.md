This project was completed as part of CS50’s Introduction to Artificial Intelligence with Python. It consists of an implementation of the PageRank algorithm, which ranks web pages by importance using Python. PageRank is based on the idea that a page is more important if it is linked to by other important pages. To compute PageRank, two approaches were implemented: one using sampling from a Markov Chain representing a random surfer model, and another using iterative calculation based on the PageRank formula until convergence.

The program expects a directory containing a corpus of HTML pages. It first parses the pages and constructs a dictionary where each key is a page and the value is the set of pages it links to. Using this corpus, the program calculates PageRank values for each page. The random surfer model simulates a user clicking links at random with a damping factor to allow jumping to any page, producing estimated probabilities for each page being visited. The iterative algorithm repeatedly updates page ranks based on the current ranks of linking pages until values converge.

The key functions implemented include:

transition_model(corpus, page, damping_factor) – Returns a probability distribution over the next page the random surfer would visit.

sample_pagerank(corpus, damping_factor, n) – Estimates PageRank values by simulating n samples from the random surfer model.

iterate_pagerank(corpus, damping_factor) – Calculates PageRank values using the iterative formula until all ranks change by less than 0.001.

This project demonstrates proficiency in Python programming, probabilistic modeling, and algorithmic thinking, while also providing insight into the foundations of search engine ranking algorithms.
