#lab3.py jesse

#task 1
food = "borritos mac and chesse burguers"
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-0]
print(first_last)
seperated = food.split()
print(seperated)
joined = " " .join(seperated)
print(joined)

#task 2 
number_list = [22, 98, 0, 11, 998]
number_list.append(876)
print(number_list)
number_list.insert(3,65)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(98)
print(number_list)
print(number_list[0:3])
print(number_list[-3:])
first_last= number_list[0] + number_list[-1]
print(first_last)

#task 3 working with keys and values
books= {"barbra o conner":"wish", "Ebwhite":"charlottes web", "jeff kinny":"diary of a wompy kid", "jeff kinny":"diary of a wompy kid"}
print(books.keys())
print(books.values())
print(books.get("barbra o conner"))
books.pop("Ebwhite")
print(books)
del books["jeff kinny"]
print(books)
