import aiohttp_jinja2
from aiohttp import web
from datetime import datetime


@aiohttp_jinja2.template('index.html')
async def index(request):
    """
    HTML response (HTML Jinja template)

    :param request:
    :return:
    """

    print(f'{request = }')

    return {
        'title': 'Application on Aiohttp!',
    }


async def about(request):
    """
    JSON response

    :param request:
    :return:
    """

    data = {
        'about': 'This About page.',
        'request': str(request),
        'date_time': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
    }

    return web.json_response(data=data)
