def palindrome(word, power):
    if power == len(word) // 2:
        return f"{word} is a palindrome"

    if word[power] != word[-power - 1]:
        return f"{word} is not a palindrome"

    return palindrome(word, power + 1)


print(palindrome("abcba", 0))
