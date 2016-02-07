#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import feedparser
import arrow


BASE_URL = 'http://b.hatena.ne.jp/satojkovic/rss?date='

def main():
    date = arrow.utcnow().to('local').format('YYYYMMDD')
    from_url = BASE_URL + date
    feed = feedparser.parse(from_url)
    for entry in range(len(feed.entries)):
        title = feed.entries[entry].title
        link = feed.entries[entry].link
        print(title, link)


if __name__ == '__main__':
    main()
