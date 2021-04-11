import vk_api
from datetime import datetime
from config import token

'''класс TableOfPosts, хранящий все посты по стены конкретного сообщества,
стастику о сообществе мы получаем с помощью методо класса'''


class TableOfPosts:

    parameters = ['likes', 'reposts', 'comments', 'views']

    def __init__(self, domain, start_date, end_date):
        self.domain = domain
        self.start_date = datetime.strptime(str(start_date), '%d.%m.%y').timestamp()
        self.end_date = datetime.strptime(str(end_date), '%d.%m.%y').timestamp()

        vk_session = vk_api.VkApi(token=token)
        tools = vk_api.VkTools(vk_session)
        self.wall = tools.get_all('wall.get', 100, {'domain': self.domain})

        # при инициализации класса сразу насчитаем некоторые параметры, для ускорения работы приложения
        self.common_value = dict.fromkeys(TableOfPosts.parameters, 0)
        self.max_value = dict.fromkeys(TableOfPosts.parameters, 0)
        self.count_posts = 0

        for post in self.wall['items']:
            if post['date'] <= self.end_date:
                if post['date'] >= self.start_date:
                    for param in TableOfPosts.parameters:
                        self.common_value[param] += post[param]['count']
                        self.max_value[param] = max(post[param]['count'], self.max_value[param])
                    self.count_posts += 1
                else:
                    break

    def __getattr__(self, attr_name):
        if attr_name[-7:] == 'average':
            return self.common_value[attr_name[:-8]] / self.count_posts
        if attr_name[-3:] == 'max':
            return self.max_value[attr_name[:-4]]
