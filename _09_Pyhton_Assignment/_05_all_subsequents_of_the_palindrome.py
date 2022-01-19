'''Al subsequents of the palindrome'''
def find_all_subsets(seq, n):

    if n == 0:
        return [[]]

    else:
        result = []
        subsets = find_all_subsets(seq, n-1)

        for subset in subsets:
            result += [subset]

            result += [[seq[n-1]] + subset]

        return result


def check_palindrome(subsetsList):
    finalList = []
    for set in subsetsList:
        if set[::-1] == set:
            finalList.append(set)
        else:
           continue

    return finalList




word = "aaccb"
palindromicSubsets = check_palindrome(find_all_subsets(word, len(word)))
print(palindromicSubsets)
