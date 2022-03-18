#!/usr/bin/env python3

import json
import os
import pandas as pd
import sys
import argparse
from datetime import date
import csv


def scrape(since, query, until, max_results):

    filename = "".join(
        [c for c in f'tweets-{query}-{since}-{until}' if c.isalnum() or c in ['-', '.']]).rstrip()+'.json'
    cmd_line = f'snscrape {"--max-results " + str(max_results) if max_results else ""} --jsonl --progress --since {since} twitter-search \'{query} until:{until}\'> {filename}'
    print(cmd_line)
    os.system(cmd_line)


def convert(filename):

    fields = ['date', 'id', 'username',
              'displayname', 'followersCount', 'verified', 'content', 'url', 'replyCount', 'retweetCount', 'likeCount']
    rows = []

    with open(filename, "r") as file:
        for line in file.readlines():
            tweet = json.loads(line)
            user = tweet.get('user')
            rows.append([tweet.get('date'), tweet.get('id'),
                        user.get('username'), user.get('displayname'), user.get('followersCount'), user.get('verified'), tweet.get('content'), tweet.get('url'), tweet.get('replyCount'), tweet.get('retweetCount'), tweet.get('likeCount')])

    with open(''.join(filename.rsplit('.json', 1))+'.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


if __name__ == "__main__":
    since = '2006-07-15'
    query = '"ich habe keine zeit"'
    until = str(date.today())
    max_results = 0

    # check for arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "mode", help="mode can be 'scrape' or 'convert'")
    arg_parser.add_argument(
        "--since", help="date since which to scrape (oldest), YYYY-MM-DD")
    arg_parser.add_argument(
        "--until", help="date until when to scrape (newest), YYYY-MM-DD")
    arg_parser.add_argument(
        "--query", help="your search query string")
    arg_parser.add_argument(
        "--limit", help="max limit of tweets to scrape")
    arg_parser.add_argument(
        "--file", help="json file that you want to convert (required for 'convert')")

    args = arg_parser.parse_args()

    if args.since:
        since = args.since
    if args.query:
        query = f'"{args.query}"'
    if args.until:
        until = args.until
    if args.limit:
        max_results = args.limit

    if args.mode == 'scrape':
        scrape(since, query, until, max_results)
    elif args.mode == 'convert':
        if not args.file:
            print('provide file pls')
            exit(2)
        convert(args.file)
