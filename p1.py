'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
#Start time: 17:40
#End Time: 17:58

def solution1(list, k):
    for i in range(len(list)):
        j = i
        while j != 0:
            if list[i]+list[j-1] == k:
                return True
            j-=1
    return False

def solution2(list,k):
    seen_num = set()
    for num in list:
        if k - num in seen_num:
            return True
        seen_num.add(num)
    return False

def main():
    test_list = [10, 15, 3, 7]
    k = 17
    print (solution2(test_list, k))

if __name__ == '__main__':
    main()

