from mycroft import MycroftSkill, intent_file_handler


class Turtleright(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtleright.intent')
    def handle_turtleright(self, message):
        self.speak_dialog('turtleright')


def create_skill():
    return Turtleright()

