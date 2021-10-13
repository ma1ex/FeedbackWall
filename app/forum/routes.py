from app.forum import views


def setup_routes(app):
    """
    Настройка путей текущего приложения - forum

    :param app:
    :return:
    """

    app.router.add_get('/', views.index)  # Main page
    app.router.add_get('/about', views.about)  # About page (second)
