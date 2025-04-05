menu = [
    {'title': 'Курсы', 'url_page': 'courses'},
    {'title': 'Игры', 'url_page': 'games'},
    {'title': 'Английский', 'url_page': 'english'},
    {'title': 'О сайте', 'url_page': 'about'},
    {'title': 'Контакты', 'url_page': 'contact'},
    {'title': 'Вход', 'url_page': 'login'},
    {'title': 'Регистрация', 'url_page': 'registration'},
]


class DataMixins:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title_page'] = self.title_page

