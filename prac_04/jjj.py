from gc import is_finalized
from operator import truediv
from tkinter.font import names


# names = ["Jerci", "John", "Julian"]
# which_name = int(input("Which name would you like to see?"))
# print(names[int(which_name-1)])
#
# def main():
#     names = ["Jerci", "John", "Julian"]
#     user_input(names)
#
# def user_input(peoples):
#     which_name = int(input("Which name would you like to see?"))
#     print(peoples[int(which_name - 1)])
#
# if __name__ == '__main__':
#     main()

# def main():
#     score = ["50", "75", "100"]
#     user_input(score)
#
# def user_input(grade):
#     while True:
#         which_score = int(input("What score would you like to see? "))
#         print(grade[which_score - 1])
#
# if __name__ == "__main__":
#     main()


# def main ():
#    guitars = ["Fender", "Ibanez", "Dean"]
#    user_input(guitars)
#
# def user_input(brands):
#     while True:
#         which_brands = int(input("What brands of guitar do you like it? "))
#         print(brands[which_brands - 0])
#
# if __name__ == "__main__":
#     main()


# text = "This is a sentence"
# words = text.split()
# long_words = [word for word in words if len(word)>3]
# print(long_words)


text = "Jerci Mauricio Huamani"
words = text.split()
long_words = [word for word in words if len(word)>6]
print(long_words)





