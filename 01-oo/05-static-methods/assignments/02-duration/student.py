class Duration:
    def __init__(self, seconds):
        self.__seconds  = seconds

    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return int(self.__seconds / 60)
    
    @property
    def hours(self):
        return int(self.__seconds / 3600)


    @staticmethod
    def from_seconds(value):
        return Duration(value)
    
    @staticmethod
    def from_minutes(value):
        return Duration(int(value * 60))

    @staticmethod
    def from_hours(value):
        return Duration(int(value * 3600))



duration = Duration.from_seconds(60)
print(duration.seconds)
print(duration.minutes)
print("--------")
duration = Duration.from_hours(1)
print(duration.minutes)
print(duration.seconds)