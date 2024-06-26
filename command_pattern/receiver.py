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


class Stereo:
    def on(self):
        print("오디오가 켜졌습니다.")

    def off(self):
        print("오디오가 꺼졌습니다.")

    def set_cd(self):
        print("오디오에 CD를 재생합니다..")

    def set_dvd(self):
        print("오디오에 DVD를 재생합니다.")

    def set_volume(self, volume: int):
        print("오디오의 볼륨을 {}으로 세팅합니다.".format(str(volume)))


class CellingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0
    location: str
    speed: int

    def __init__(self, location: str):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH

    def medium(self):
        self.speed = self.MEDIUM

    def low(self):
        self.speed = self.LOW

    def off(self):
        self.speed = self.OFF

    def get_speed(self) -> int:
        return self.speed
