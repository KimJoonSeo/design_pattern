class Light:
    def on(self):
        print("조명이 켜졌습니다.")

    def off(self):
        print("조명이 꺼졌습니다.")

class GarageDoor:
    def up(self):
        print("창고 문이 열럈습니다.")
    def off(self):
        print("창고 문이 닫혔습니다.")
    def stop(self):
        print("창고 문이 멈췄습니다.")
    def light_on(self):
        print("창고 문빛이 켜졌습니다.")
    def light_off(self):
        print("창고 문빛이 꺼졌습니다.")