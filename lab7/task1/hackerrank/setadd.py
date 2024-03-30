# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    N = int(input())
    my_set = set()
    for _ in range(N):
        my_set.add(input())
    print(len(my_set))