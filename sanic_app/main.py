import json

from sanic import Sanic
from sanic import response
import jwt

from sanic_app.users import USERS

app = Sanic('lirons_server')


@app.route("/login", methods=["GET"])
def login(request):
    # user: dict = json.loads(str(request.body, encoding='UTF-8'))['user']
    # name: str = user['name']
    # password: str = user['password']
    # input_jwt: str = 'ttt'
    #
    return response.text('You are in!')


@app.route("/items_refine", methods=["POST"])
def refine_items(request):
    return response.json({item['name']: [item[key] for key in item.keys() if 'val' in key.lower()][0]
                          for item in json.loads(str(request.body, encoding='UTF-8'))['items']})


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
