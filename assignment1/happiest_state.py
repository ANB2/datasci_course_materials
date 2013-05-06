import sys
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
    remove_punctuation_map = dict((ord(char), None) for char in '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~')

    # data structure: state : [count, sum]
    states = {x : [0, 0] for x in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",\
                                   "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",\
                                   "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",\
                                   "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",\
                                   "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]}

    for line in tweet_file:
        try:
            tweet = json.loads(line)
            
            country = tweet['place']['country']
            state = tweet['place']['full_name'][-2::]
            
            if country=='United States' and state in states:
                # chosen normalisation: lower case, no punctuation, don't consider n-grams
                words = tweet['text'].translate(remove_punctuation_map).lower().strip().split()
                sent = float( sum([sentiment[x] if x in sentiment else 0 for x in words]) )
            
                states[state][0] += 1
                states[state][1] += sent
            
        except:
            pass 

    # compute the value that should be used for ranking
    def get_rank(v):
        if states[v][0]:
            return float(states[v][1]) / states[v][0]
        else:
            # if there's no tweet from the state, give large negative
            return -1000
    
    print str(max(states, key=get_rank)).encode('UTF-8')

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
