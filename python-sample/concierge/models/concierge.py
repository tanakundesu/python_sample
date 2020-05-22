from concierge.models import concierge
from concierge.utils import csvutil
from concierge.utils import templateutil

DEFAULT_CONCIERGE_NAME = 'Gamin Bot'


class Concierge(object):
    """
        Base model for Concierge.
    """
    def __init__(self, concierge_name=DEFAULT_CONCIERGE_NAME, user_name='',
                 speak_color='blue'):
        self.concierge_name = concierge_name
        self.user_name = user_name
        self.speak_color = speak_color

    def welcome(self):
         while True:
            template = templateutil.get_template('welcome.txt', self.speak_color)
            user_name = input(template.substitute({
                'concierge_name': self.concierge_name}))

            if user_name:
                self.user_name = user_name.title()
                break

    def seeyou(self):
        template = templateutil.get_template('seeyou.txt', self.speak_color)
        print(template.substitute({
            'concierge_name': self.concierge_name,
            'user_name': self.user_name,
        }))

class GameConcierge(Concierge):
    """
        main model for Concierge.
    """
    def __init__(self, concierge_name=DEFAULT_CONCIERGE_NAME):
        super().__init__(concierge_name=concierge_name)
        self.csvutil = csvutil.RecommendUtil()

    def _welcome_decorator(func):
        def wrapper(self):
            if not self.user_name:
                self.welcome()
            return func(self)
        return wrapper

    @_welcome_decorator
    def popular_game(self):
        popular_game = self.csvutil.get_most_popular()
        if not popular_game:
            return None

        recommend_game = [popular_game]
        while True:
            template = templateutil.get_template('like_game.txt', self.speak_color)
            is_yes = input(template.substitute({
                'concierge_name': self.concierge_name,
                'user_name': self.user_name,
                'gametitle': recommend_game
            }))

            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                break

            if is_yes.lower() == 'n' or is_yes.lower() == 'no':
                popular_game = self.csvutil.get_most_popular(
                    not_list=recommend_game)
                if not popular_game:
                    break
                recommend_game.append(popular_game)

    @_welcome_decorator
    def ask_favorite_game(self):
        while True:
            template = templateutil.get_template(
                'ask_game.txt', self.speak_color)
            gametitle = input(template.substitute({
                'concierge_name': self.concierge_name,
                'user_name': self.user_name,
            }))
            if gametitle:
                self.csvutil.increment(gametitle)
                break

 
