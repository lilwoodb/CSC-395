# CSC-395 Programming Assignment 1: Steffie Ochoa and Lilya Woodburn

## General Notes
  * Program only crawls pages within the Wikipedia domain.
  * The seed list comprises 10 pre-selected Wikipedia articles, which can be swapped out for other Wikipedia articles.
  * The number of randomly-chosen links for getlinks must be at least 20, to ensure the total pages crawled is at least 100.
  * Uses a Boolean Information Retrieval model (does not incorporate PageRank).
  * Prints a list of URLs in order of decreasing relevance, so that the most relevant URL is listed first.

## Instructions for using search-engine
  * Must have a total of three words, each separated by a space. Like so: 
      `term1 boolean term2`
  * There must be exactly one boolean and it must be between exactly two search terms.
  * A search term cannot contain a space. It must be a single-unit word.
  * A search term must be a noun.
  * Available boolean terms are "and", "not", and "or". No other terms may be used.
      * If the query doesn't match a given boolean term, program prints "Please enter a valid query."
  * If search terms' documents don't match the given boolean requirements, program prints an empty list.
  * Typing only "q" will quit the program.
