from handlers.handler import Handler


class HandlerInlineQuery(Handler):
    def __init__(self, bot):
        super().__init__(bot)

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data