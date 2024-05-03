from flask import Flask, request, Response
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=10)
def index():
    # Retrieve headers sent by the client
    headers = request.headers

    # Check for the presence of the X-Metachar-Header
    if 'X-Metachar-Header' in headers:
        return Response('X-Metachar-Header detected!', status=500)

    # Check for the presence of the X-Oversized-Header
    if 'X-Oversized-Header' in headers:
        return Response('X-Oversized-Header detected!', status=500)

    # Check for the presence of the X-HTTP-Method-Override
    if 'X-HTTP-Method-Override' in headers and request.method == 'DELETE':
        return Response('DELETE request detected!', status=500)

    # Check for the presence of the X-Fragmented-Header
    if 'X-Fragmented-Header' in headers:
        return Response('X-Fragmented-Header detected!', status=500)

    # Check for the presence of the multipart/form-data content type
    if 'multipart/form-data' in request.headers.get('Content-Type', ''):
        return Response('multipart/form-data detected!', status=500)

    # Check for HTTP Parameter Pollution
    if request.args.getlist('param1'):
        return Response('HTTP Parameter Pollution detected!', status=500)

    # Otherwise, return a generic response
    return 'No cache poisoning detected.', 200

if __name__ == '__main__':
    app.run(debug=True)
