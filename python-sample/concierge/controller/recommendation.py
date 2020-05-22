from concierge.models import concierge


def recommend_game():
    game_bot = concierge.GameConcierge()
    game_bot.welcome()
    game_bot.popular_game()
    game_bot.ask_favorite_game()
    game_bot.seeyou()

