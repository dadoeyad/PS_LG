
def classify(num_list):
    for n in num_list:
        num_sum = 0
        for divisor in range(1, n):
            if not n % divisor:
                num_sum += divisor
        if num_sum == n:
            print n, " is perfect"
        elif num_sum > n:
            print n, " is abundant"
        else:
            print n, " is deficient"

if __name__ == "__main__":
    classify(range(1, 100))
