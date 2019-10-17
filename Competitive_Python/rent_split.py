'''
210 Rent-Split
'''
room_mates = []


class Rent:
    def __init__(self, total_rent, current_bill):
        self.total_rent = total_rent
        self.current_bill = current_bill

    def basic_rent(self):
        split_half = 1155/2
        room_mates.append({'Kishan': split_half})
        room_mates.append({'Pavan': split_half/2})
        room_mates.append({'Suyash': split_half/2})
        basic_rent = 1155
        # print(f'{room_mates}')
        return basic_rent

    def utility_rent(self):
        remaining_rent = self.total_rent - self.basic_rent()
        individual_contri = remaining_rent/len(room_mates)
        split_amt = self.current_bill / len(room_mates)
        for roommate in room_mates:
            for mate in roommate.keys():
                roommate[mate] += individual_contri + split_amt
        return room_mates


rent = float(input('Enter the total rent amount:'))
current = float(input('Enter the total current bill amt:'))
persons = Rent(rent, current).utility_rent()

for person in persons:
    for key, value in person.items():
        print(f'{key} has to pay {round(value,2)}$')
