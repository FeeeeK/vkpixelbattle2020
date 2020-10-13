from aiohttp import web
import json


class JsonStotage:
    def __init__(self, path):

        self.data = {}
        self._path = path
        self.load()

    def save(self):
        with open(self._path, "w") as data:
            json.dump(self.data, data, ensure_ascii=False)

    def load(self):
        with open(self._path, "r") as data:
            self.data = json.load(data)


storage = JsonStotage("tokens.json")
url = "https://sample.com"


async def handler(request):
    event = request.rel_url.query
    if not all(i in event for i in ["sign", "vk_user_id", "vk_language"]):
        return web.HTTPFound(f"{url}/error")
    storage.data[event["vk_user_id"]] = request.path_qs.split("code=")[1]
    storage.save()
    return web.HTTPFound(f"{url}/thanks")


app = web.Application()


app.router.add_route(path="/", method="GET", handler=handler)
web.run_app(app, port=888)
