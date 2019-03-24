# urban-dictionary-lookup


# urban-dictionary-lookup cli

This cli takes a user-input word and returns an Urban Dictionary word prominence score (based on count of reactions) as well as the word's top definition. The data gathering happens through scraping the crowd-sourced Urban Dictionary website.

*Note: look up words at your own risk. This tool was developed for friends for whom English is their second language in order to provide a quick way to look up new slag :)*

## Getting Started

### Prerequisites

* Beautiful Soup 4

### To run

`$ python3 index.py`


## How `prominence score` works

I added in the idea of prominence score to help highlight the obscurity of the looked-up word. The idea is that if few people have reacted positively to a word, it's probably very uncommonly known or used, therefor not worth learning.

**High prominence:** more than 1000 thumbs up for the top definition. <br>
**Medium prominence:** between 300 and 1000 thumbs up for the top definition. <br>
**Low prominence:** less than 300 thumbs up for the top definition. 
