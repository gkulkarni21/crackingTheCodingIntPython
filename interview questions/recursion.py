import itertools

__author__ = 'Gaurav'


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else: return fibo(n-1) + fibo(n-2)

def paren(left, right=None):
    '''
    If right not specifies, left = right. Go down on number of lefts until it reaches 0 and yield "("+p every time. Go down on
    rights until it is > left and yield ")"+p every time
    :param left:
    :param right:
    :return:
    '''
    if not right:
        right = left

    if left == right == 0:
        yield ""
    else:
        if left > 0:
            for p in paren(left-1, right):
                yield "(" + p

        if right > left:
            for p in paren(left, right - 1):
                yield ")"+ p


def power_set(seq):
   seq_set = set(seq)
   for subset in itertools.chain.from_iterable(itertools.combinations(seq_set, r) for r in range(len(seq_set) + 1)):
       yield set(subset)


def string_perms(input_string):
    permutations = []
    if len(input_string) == 1:
        permutations.append(input_string)
    else:
        first = input_string[0]
        remainder = input_string[1:]
        words = string_perms(remainder)
        for word in words:
            for j in range(len(word)):
                permutations.append(insertCharAt(word, first, j))

    return set(permutations)

def insertCharAt(string, char, position):
    start = string[0:position]
    end = string[position:]
    return start + char + end

def coin_change(list_of_coins, change, known_change):
    min_coins = change #worst case where all pennies are needed
    if change in list_of_coins:
        known_change[change] = 1
        return 1
    elif known_change[change] > 0:
        return known_change[change]
    else:
        for i in [c for c in list_of_coins if c <= change]: #choose each denomination from list_of_coins
            num_coins = 1 + coin_change(list_of_coins, change - i, known_change)
            if num_coins < min_coins:
                min_coins = num_coins
                known_change[change] = min_coins
    return min_coins


def min_coins_DP_solution(list_of_coins, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coins_count = cents
        new_coin = 1
        for j in [c for c in list_of_coins if c <= change]:
            if 1 + minCoins[cents - j] < coins_count:
                coins_count = 1 + minCoins[cents - j]
                new_coin = j
        minCoins[cents] = coins_count
        coinsUsed[cents] = new_coin
    return minCoins[cents]



def main():
    # input_s = [1, 2, 4]
    # for i in power_set(input_s):
    #     print i
    # input_str = "gaurav"
    # perm = string_perms(input_str)
    # print perm
    # for i in paren(3):
    #     print i
    # out = itertools.permutations("gaurav")
    # print str(list(out))
    # dict_change = {}
    # dict_change[1]= 0
    # dict_change[3] = 0
    # dict_change[4] = 0
    # print coin_change([1, 3, 4], 25,[0]*64)

    print min_coins_DP_solution([1, 5, 10, 21, 25], 65, [0]*66, [0]*66)
if __name__ == '__main__':
    main()