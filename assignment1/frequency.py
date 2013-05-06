import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    wordict = {}

    for line in tweet_file:
        try:
            # chosen normalisation: don't consider n-grams
            words = json.loads(line)['text'].strip().split()

            for x in words:
                if x in wordict:
                    wordict[x] += 1
                else:
                    wordict[x] = 1            
            
            # a very simplistic approach: assign unknown word a score equal to its tweet
            for x in unk:
                print '%s %.3f' % (x, score)
            
        except:
            pass

    denom = sum(wordict.values())

    for k, v in wordict.iteritems():
        print '%s %.4f' % (k.encode('UTF-8'), float(v) / denom)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
