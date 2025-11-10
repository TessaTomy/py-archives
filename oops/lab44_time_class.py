class Time:
    def __init__(self):
        self.__hr,self.__min,self.__sec = 0,0,0
    def setTime(self):
        try:
            self.__hr = int(input("Enter Hours (1–12): "))
            self.__min = int(input("Enter Minutes (0–59): "))
            self.__sec = int(input("Enter Seconds (0–59): "))
        except ValueError:
            self.__hr, self.__min, self.__sec = 12, 0, 0
            return

        if not (1 <= self.__hr <= 12 and 0 <= self.__min < 60 and 0 <= self.__sec < 60):
            print("Invalid time range. Defaulting to 12:00:00")
            self.__hr, self.__min, self.__sec = 12, 0, 0

    def __str__(self):
        return f"{self.__hr:02}:{self.__min:02}:{self.__sec:02}"

    def __add__(self, other):
        t1=Time()
        t1.__sec=self.__sec+other.__sec
        t1.__min=self.__min+other.__min+t1.__sec//60
        t1.__sec%=60
        t1.__hr=self.__hr+other.__hr+t1.__min//60
        t1.__min%=60
        return t1

t1=Time()
t1.setTime()
t2=Time()
t2.setTime()
print(f' {t1}\n+\n {t2}\n--------------------\n {t1 + t2}')
