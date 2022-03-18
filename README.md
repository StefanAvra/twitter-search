# twitter-search

~~Nodejs twitter search tool.
Built to be used with the Twitter API v2 to [search tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction).~~

~~Your app needs the "Academic Research access" for searching the full archive.~~

Since it's not that easy to get approved for Twitters full archive search this code just uses [snscrape](https://github.com/JustAnotherArchivist/snscrape)

## Getting started

create virtual environment:

```sh
python3 -m venv venv
```

activate it:

```sh
source venv/bin/activate
```

install requirements:

```sh
pip install -r requirements.txt
```

scrape tweets like this:

```sh
python twitter_search.py scrape --query 'butterbrezel' --since 2020-01-01
```

convert it to csv like this:

```sh
python twitter_search.py convert --file tweets-butterbrezel-2020-01-01-2022-03-18.json
```
