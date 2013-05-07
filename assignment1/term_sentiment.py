import sys
import json
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # build word:sentiment dictionary
    word = []
    score = []
    for line in sent_file:
        a, b = line.split('\t')
        word.append(unicode(a, 'UTF-8'))
        score.append(int(b))
    sentiment = dict(zip(word, score))

    # the mapping is used for unicode `translate` method
    remove_punctuation_map = dict((ord(char), None) for char in '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~')

    for line in tweet_file:
        try:
            # chosen normalisation: lower case, no punctuation
            # we don't consider n-grams here, only one-words
            words = json.loads(line)['text'].translate(remove_punctuation_map).lower().strip().split()

            score = 0
            unk = []
            for x in words:
                if x in sentiment:
                    score += sentiment[x]
                else:
                    unk.append(x)

            # a very simplistic approach: assign unknown word a score equal to its tweet
            for x in unk:
                print '%s %.3f' % (x, score)
            
        except:
            pass

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
