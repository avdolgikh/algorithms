# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/5997990269157376


import random


class RandomPickWithWeight:
    def __init__(self, weights, verbose=False):
        self.verbose = verbose
        self.weight_sums = []
        sum = 0
        for weight in weights:
            sum += weight
            self.weight_sums.append(sum)
        self.max = sum
        if self.verbose:
            print(f"{weights} --> {self.weight_sums}")

    def pick_index(self):
        random_number = random.randint(1, self.max)
        if self.verbose:
            print(f"random_number = {random_number}")
        index = self._binary_search(self.weight_sums, random_number)
        if self.verbose:
            print(f"index = {index}")
        return index
    
    def _binary_search(self, nums, target):
        i, j = 0, len(nums)-1
        while i <= j:
            m = int((i + j)/2)
            if self.verbose:
                print(f"i={i}, j={j}, m={m}")
            if (target == nums[m]) or ((m > 0) and (nums[m - 1] < target < nums[m])) or ((m == 0) and (target < nums[m])):
                return m
            elif target < nums[m]:
                j = m - 1
            else:
                i = m + 1
        return m


# Driver code
def main():
    counter = 900

    weights = [[1, 2, 3, 4, 5],
                [1, 12, 23, 34, 45, 56, 67, 78, 89, 90],
                [10, 20, 30, 40, 50],
                [1, 10, 23, 32, 41, 56, 62, 75, 87, 90],
                [12, 20, 35, 42, 55],
                [10, 10, 10, 10, 10],
                [10, 10, 20, 20, 20, 30],
                [1, 2, 3],
                [10, 20, 30, 40],
                [5, 10, 15, 20, 25, 30]]

    dict = {}
    for i in range(len(weights)):
        print(i + 1, ".\tList of weights: ", weights[i], ", pick_index() called ", counter, " times", "\n", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        sol = RandomPickWithWeight(weights[i])
        for j in range(counter):
            index = sol.pick_index()
            dict[index] += 1
        print("-"*105)
        print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Actual Frequency", "|", "Expected Frequency"))
        print("-"*105)
        for key, value in dict.items():

            print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*105, "\n", sep="")


if __name__ == '__main__':
    main()

    # weights = [3, 6, 4]
    # rpww = RandomPickWithWeight(weights, verbose=True)
    # rpww.pick_index()
