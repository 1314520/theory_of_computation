from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    ################is_going_to_state#################
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'cavalier will win nba finals'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'warrior will win nba finals'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == "i don't care who win nba finals"
    
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'cavalier will win nba finals'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'warrior will win nba finals'
    
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'cavalier will win nba finals'

    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == 'warrior will win nba finals'
    
    ##################################################
    def on_enter_state1(self, update):
        update.message.reply_text("right")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("but cavalier has lebron james.\n so you think which team will win nba finals")

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("ok")
        self.go_back(update)
    
    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("right")
        self.go_back(update)
    
    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("but cavalier has kyrie irving.\n so you think which team will win nba finals")
    
    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_text("right")
        self.go_back(update)
    
    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_enter_state7(self, update):
        update.message.reply_text("i think i can't convince you.")
        self.go_back(update)
    
    def on_exit_state7(self, update):
        print('Leaving state7')








