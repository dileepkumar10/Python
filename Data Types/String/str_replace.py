# Replacing the string


# str1="i am learning python"
# r=str1.replace("python", "Docker")
# print(r)


str1=input("Enter a sentence: ")
print(f'Your Sentence is {str1}')
re=input("Enter the word to replace: ")
ne=input("Enter the new word :")
res=str1.replace(re, ne)
print(f"The modified sentence is {res}")




# str1=input("Enter a sentence: ")
# word = input("Enter word to replace: ")
# new_word = input("Enter new word :")

# if word in str1:
#     str1=str1.replace(word, new_word)
# else:
#     print('The given word is not present in the sentence')
    
# print("Modified Sentence: ",str1) 