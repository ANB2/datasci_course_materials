import sys
import string
import json

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
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

    for line in tweet_file:
        try:
            # chosen normalisation: lower case, no punctuation
            words = json.loads(line)['text'].translate(remove_punctuation_map).lower().strip().split()

            # chosen n-gram strategy: build all n-grams and consider all match
            # we know that there's only up to 3 words in the dict
            temp = list(words)
            for n in xrange(2, 4):
                myNgrams = [temp[i:i+n] for i in xrange(len(temp) - n)]
                for x in myNgrams:
                    words.append(' '.join(x))

            print float( sum([sentiment[x] if x in sentiment else 0 for x in words]) )
            
        except:
            pass    

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
