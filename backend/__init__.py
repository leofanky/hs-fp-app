def process_user_query(query_string):
    y = []
    result = []
    result = query_string.split()
    for x in result:
        y.append('hi ' + x )
    return y
