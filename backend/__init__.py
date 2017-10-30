def process_user_query(query_string):
    y = []
    result = []
    result = query_string.split()
    for x in result:
        if x[0].isupper():
            y.append('hi ' + x )
    return y

print (process_user_query('Leo went to a party with Mario'))
