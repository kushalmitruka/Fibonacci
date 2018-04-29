
def formatter(filter_object, req_object=''):

    if req_object == 'ig':
        return filter_object

    if req_object == 'num':
        return '{:,.0f}'.format(float(filter_object))

    return '{}'.format(filter_object)
