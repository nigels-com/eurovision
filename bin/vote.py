#!/usr/bin/env python3

import json

try:
    import click
except:
    print("Suggestion: $ sudo apt-get install python3-click")
    raise

@click.command()
@click.option('-c', type=click.STRING, help='Country')
@click.option('-v', type=click.INT,    help='Votes')
def cli(**kwargs):
  country = kwargs['c']
  votes = kwargs['v']
  f = open('votes.json')
  v = json.load(f)
  for i in v:
    if i['flag']==country or i['name']==country:
      i['votes'] += votes

  with open('votes.json', 'w') as f:
    json.dump(v, f, ensure_ascii=False)

if __name__ == '__main__':
    cli()

