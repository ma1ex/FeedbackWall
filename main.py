from aiohttp import web
import jinja2
import aiohttp_jinja2


def setup_routes(application):
    """
    Настройка url-путей для всего приложения

    :param application:
    :return:
    """

    # Импорт роутов модуля "отзывов"
    from app.forum.routes import setup_routes as setup_forum_routes

    # Настраиваем url-пути приложения forum
    setup_forum_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    """
    Указываем шаблонизатору, что html-шаблоны надо искать в папке templates

    :param application: aiohttp application
    :return: None
    """

    aiohttp_jinja2.setup(
        application,
        loader=jinja2.FileSystemLoader('templates')
    )


def setup_app(application):
    """
    Настройка всего приложения

    :param application:
    :return:
    """

    # Настройки внешних библиотек, например шаблонизатора
    setup_external_libraries(application)

    # Настройки роутера приложения
    setup_routes(application)


# Создание веб-сервера
app = web.Application()


if __name__ == '__main__':
    setup_app(application=app)
    web.run_app(app=app)
