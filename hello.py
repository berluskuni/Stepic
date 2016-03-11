from  cgi import parse_qs
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    qs = parse_qs(environ['QUERY_STRING'])
    return ['%s=%s' % (x, qs[x][0]) for x in qs]
