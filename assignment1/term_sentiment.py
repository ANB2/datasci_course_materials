import sys
import json
import string
from collections import defaultdict

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # build word:sentiment dictionary
    sentiment = {}
    for line in sent_file:
        term, score = line.split('\t')
        sentiment[term] = int(score)

    unknowns = defaultdict(int)

    for line in tweet_file:
        try:
            # chosen normalisation: 
            # we don't consider n-grams here, only one-words
            words = json.loads(line)['text'].encode('ascii', 'ignore').strip().split()

            score = 0
            unk = []
            for x in words:
                if x in sentiment:
                    score += sentiment[x]
                else:
                    unk.append(x)
            
            # the score of an unknown word is defined as:
            # the sum of the tweet scores in which the word appears
            for x in unk:
                unknowns[x] += score
            
        except:
            pass
    
    for k, v in unknowns.iteritems():
        print '%s\t%.3f' % (k.encode('UTF-8'), float(v))

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
