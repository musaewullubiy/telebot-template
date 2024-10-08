from handlers.handler import Handler


class HandlerAllText(Handler):
    def __init__(self, bot):
        super().__init__(bot)

    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            pass