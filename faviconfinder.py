#!/usr/bin/env python3
import mmh3
import sys
import codecs
import requests

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [URL]")
    sys.exit(0)

try:
    response = requests.get(sys.argv[1])
    favicon = codecs.encode(response.content, 'base64')
    hash = mmh3.hash(favicon)
    print(f"Favicon Hash: {hash}")
except Exception as e:
    print(f"Error occured as: {e}", file=sys.stderr)
