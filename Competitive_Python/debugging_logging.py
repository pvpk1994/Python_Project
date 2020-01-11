from collections import Counter
'''
Debugging Logging Program
Developer: Pavan Kumar Paluri
'''
# Note: Function Overriding not possible in python, it has to be method overriding
# In order to implement function overriding which is otherwise not possible in dynamically
# typed python language, an alternative is to initiate all params with None as their default values
# and then have if, else cases to enumerate each of the plausible scenarios


class debug(object):
    def DEBUG(self, str_a, param_1=None, param_2=None):
        prefix = "[DEBUG] "
        # Default Type Conversions to string type
        param_1 = str(param_1)
        param_2 = str(param_2)
        if param_1 is None and param_2 is None:
            return prefix + str_a
        elif param_1 is not None and param_2 is None:
            return prefix + self.find_and_replace(str_a, param_1)
        elif param_1 is not None and param_2 is not None:
            str_a = self.find_and_replace(str_a, param_1)
            print(str_a)
            str_a = self.find_and_replace(str_a, param_2)
            return prefix + str_a

    def WARN(self, str_a, param_1=None, param_2=None):
        prefix = "[WARN] "
        # Default Type Conversions to string type
        param_1 = str(param_1)
        param_2 = str(param_2)
        if param_1 is None and param_2 is None:
            return prefix + str_a
        elif param_1 is not None and param_2 is None:
            return prefix + self.find_and_replace(str_a, param_1)
        elif param_1 is not None and param_2 is not None:
            str_a = self.find_and_replace(str_a, param_1)
            print(str_a)
            str_a = self.find_and_replace(str_a, param_2)
            return prefix + str_a

    def ERROR(self, str_a, param_1=None, param_2=None):
        prefix = "[ERROR] "
        # Default Type Conversions to string type
        param_1 = str(param_1)
        param_2 = str(param_2)
        if param_1 is None and param_2 is None:
            return prefix + str_a
        elif param_1 is not None and param_2 is None:
            return prefix + self.find_and_replace(str_a, param_1)
        elif param_1 is not None and param_2 is not None:
            str_a = self.find_and_replace(str_a, param_1)
            print(str_a)
            str_a = self.find_and_replace(str_a, param_2)
            return prefix + str_a

    def INFO(self, str_a, param_1=None, param_2=None):
        prefix = "[INFO] "
        # Default Type Conversions to string type
        param_1 = str(param_1)
        param_2 = str(param_2)
        if param_1 is None and param_2 is None:
            return prefix + str_a
        elif param_1 is not None and param_2 is None:
            return prefix + self.find_and_replace(str_a, param_1)
        elif param_1 is not None and param_2 is not None:
            str_a = self.find_and_replace(str_a, param_1)
            print(str_a)
            str_a = self.find_and_replace(str_a, param_2)
            return prefix + str_a

    def find_and_replace(self, original_str: str, str_replace_with: str) -> str:
        str_to_replace = '{}'
        # replace only the first found {} occurrence
        original_str = original_str.replace(str_to_replace, str_replace_with, 1)
        return original_str


if __name__ == '__main__':
    deb = debug()

    # call the method
    print(deb.INFO("Hello World #{} {}!", 123, "Kumar"))



