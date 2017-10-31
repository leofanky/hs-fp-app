#def process_user_query(query_string):
#    y = []
#    result = []
#    result = query_string.split()
#    for x in result:
#        if x[0].isupper():
#            y.append('hi ' + x )
#    return y

def process_user_query(query_string):  #better way of doing it cause it doesn't repeat
    words = query_string.split()
    greetings = []
    for word in sorted(set(words)):
        if word[0].isupper():
            greetings = f'Hi {word}'
    return greetings


def process_user_query(query_string):  #better way of doing it cause it doesn't repeat
    return [f'Hi {word}' for word in sorted(set(query_string.split())) if word[0].isupper()]


#print (process_user_query('Leo went to a party with Mario'))
