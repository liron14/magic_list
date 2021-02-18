import json

from sanic import Sanic
from sanic import response

app = Sanic('lirons_server')


@app.route("/api", methods=["POST"])
def refine_items(request):
    return response.json({item['name']: [item[key] for key in item.keys() if 'val' in key.lower()][0]
                          for item in json.loads(str(request.body, encoding='UTF-8'))['items']})


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
