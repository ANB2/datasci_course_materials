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
            tweet = json.loads(line)
            
            for ht in tweet['entities']['hashtags']:
                word = ht['text']
                
                if word in wordict:
                    wordict[word] += 1
                else:
                    wordict[word] = 1
       
       except:
           pass

    top_ten = sorted(wordict, key=lambda x: wordict[x], reverse=True)[:10]

    for i in top_ten:
        print i.encode('UTF-8'), float(wordict[i]) 

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
