import sys
def calc_sum(str_input):
    print(int(str_input[0])+ int(str_input[1]))

if __name__ == "__main__":
    str_input= input("please inter the input numbers: ") #sys.stdin.read()
    calc_sum(str_input.split())