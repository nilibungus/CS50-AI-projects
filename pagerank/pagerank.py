import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """




def sample_pagerank(corpus, damping_factor, n):
    #make a dictionary to count the pages, with keys the same keys as in the corpus dictionary:
    page_counter = dict()
    for page in corpus:
        page_counter[page] = 0
    #make a list out of corpus over which we can iterate and randomise:
    corpus_list = list(corpus.keys())
    #obtain the first page at random from the keys of corpus:
    random_index = random.randrange(len(corpus_list))

    new_page = corpus_list[random_index]


    #iterate n times, to obtain n samples:
    k = 0
    while k < n:
        rando = random.randint(0, 100)
        if rando <= damping_factor*100 and list(corpus[new_page]):

                new_page= random.choice(list(corpus[new_page]))


        else:
            new_page = random.choice(corpus_list)
        page_counter[new_page] += 1
        k += 1

    #make the dictionary of page ranks:

    pageranks_dic = dict()

    for key in page_counter:
        pageranks_dic[key] = page_counter[key]/n

    return pageranks_dic










def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """


    #calculate the number of pages
    n = len(list(corpus.keys()))
    #create a dictionary with keys being the pages in corpus and th values being a list with each PR at each time step:
    pagerank_dictionary = dict()

    for key in corpus:
        pagerank_dictionary[key] = [1/n]
    #check convergence:
    converge = False


    while not converge:
        new_values = dict()
        dangling_sum = sum(pagerank_dictionary[p][-1]/n for p in corpus if not corpus[p])
        for key in pagerank_dictionary:
            linking_pages = []
            for page in corpus:
                if key in corpus[page]:
                    linking_pages.append(page)

            sigma = 0

            for page in linking_pages:
                if corpus[page]:

                    sigma += pagerank_dictionary[page][-1]/ len(corpus[page])


            new_value = ((1 - damping_factor)/n) + damping_factor*(sigma + dangling_sum)


            new_values[key] = new_value
        for page in pagerank_dictionary:
            pagerank_dictionary[page].append(new_values[page])


        converge = all(abs(pagerank_dictionary[page][-1] - pagerank_dictionary[page][-2]) < 0.001 for page in corpus)
    return {p: pagerank_dictionary[p][-1] for p in pagerank_dictionary}



if __name__ == "__main__":
    main()
