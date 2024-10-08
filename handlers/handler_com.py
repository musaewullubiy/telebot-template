from handlers.handler import Handler


class HandlerCommands(Handler):
    def __init__(self, bot):
        super().__init__(bot)

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                print('yes')