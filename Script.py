import FindSmall
import Data

my_file = "Result.txt"
file = open(my_file, 'w')

file.write("List 1 smallest: {}\n".format(FindSmall.find_two_smallest(Data.list1)))
file.write("List 2 smallest: {}\n".format(FindSmall.find_two_smallest(Data.list2)))
file.write("List 3 smallest: {}\n".format(FindSmall.find_two_smallest(Data.list3)))
file.write("List 4 smallest: {}\n".format(FindSmall.find_two_smallest(Data.list4)))
file.write("List 5 smallest: {}\n".format(FindSmall.find_two_smallest(Data.list5)))

file.close()

file = open(my_file, 'r')
text = file.read()
file.close()

print(text)