user= input("Enter a word: ")
word = user
length = len(word)
is_palindrome = True

for i in range(length // 2):
    if word[i] != word[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print(user+ " is a palindrome.")
else:
    print(user+ " is not a palindrome.")