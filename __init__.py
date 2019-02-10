from mycroft import MycroftSkill, intent_file_handler
import subprocess

class Turtleright(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtleright.intent')
    def handle_turtleright(self, message):
        self.speak_dialog('turtleright')
        s = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'"
        subprocess.call([s],shell=True)

def create_skill():
    return Turtleright()

