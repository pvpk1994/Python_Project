'''
Angle b/n Hour-hand and minute-hand calc
Author: Pavan Kumar Paluri
'''


def mins(a: int, b: int) -> int:
    if a > b:
        return b
    else:
        return a


class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    '''
    hour angle: example 3:30 
    then hour hand will advance at 0.5 degree per minute.
    Start from 12:00 ~0 which will be (3*60 + 30)*0.5 degrees
    and minute hand will advance 6 degrees per minute
    which will be 30*6 ~ 180 degrees 
    So for 3:30 hour_angle - min_angle ~ (210)*0.5 - 180 ~ 75 degrees
    '''
    def hour_angle(self):
        if self.hour >= 12 and self.hour < 24:
            self.hour -= 12
        elif self.hour == 24:
            self.hour = 0
        elif self.hour > 24:
            raise ValueError('Time entered is invalid')
        if self.minute == 60:
            self.minute = 0
        angle_hour = (self.hour*60 + self.minute)*0.5
        return angle_hour

    def minute_angle(self):
        if self.minute == 60:
            self.minute = 0
        elif self.minute >60:
            raise ValueError('Invalid Minute')
        angle_minute = self.minute*6
        return angle_minute

    def actual_angle(self):
        angle = int(abs(self.hour_angle() - self.minute_angle()))
        return mins(360-angle, angle)

    def __str__(self):
        return f'Angle b/n {self.hour} and {self.minute} is {self.actual_angle()}'


hour_hand = int(input('Enter the hour:'))
minute_hand = int(input('Enter the minute:'))
calc = Clock(hour_hand, minute_hand)
print(calc.__str__())

hours = []
for hour in range(0, 12):
    hours.append(hour)

minutes = []
for minute in range(0, 60):
    minutes.append(minute)

hours_minutes = []
for hour in range(0, 12):
    for minute in range(0, 60):
        hours_minutes.append((hour, minute))

print(hours_minutes)

'''
Now we try to print all time instances where the minute hand exactly superimposes
with the hour hand
'''
for hour, minute in hours_minutes:
    if Clock(hour, minute).actual_angle() == 0:
        print(f'{hour}:{minute}')



