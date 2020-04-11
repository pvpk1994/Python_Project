'''
Crazy Jumpball
Author: Pavan Kumar Paluri
Dynamic Programming Approach
'''


class crazy_jumpball:
    def __init__(self, runway: list):
        self.runway = runway

    def runway_result(self, speed, runway_position) -> bool:
        # Stopping conditions check
        if speed == 0:
            return True
        if runway_position >= len(self.runway) or runway_position < 0 or self.runway[runway_position] is False:
            return False
        # Explore all the paths
        return self.runway_result(speed, runway_position + speed) or self.runway_result(speed - 1, runway_position + (speed - 1)) or self.runway_result(speed+1, runway_position + (speed + 1))

    def print_result(self):
        return self.runway_result(1, 1)


if __name__ == '__main__':
    run_list = [True, True, False, False, True]
    jump_result = crazy_jumpball(run_list)
    print(f"Result is: {jump_result.print_result()}")

