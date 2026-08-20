#list 1)
roll=1024170270
rollist=[]
i=0
while roll!=0:
    digit=roll%10
    roll=roll//10
    rollist.append(digit)
print("my rollnumber",rollist)
rollist.append(9)
rollist.insert(1,10)
print(rollist)
rollist.remove(9)
rollist.pop(1)
print(rollist)
rollist.sort(reverse=True)
print(rollist)
print(rollist[0:2])
average=sum(rollist)/len(rollist)
newlist=[x for x in rollist if x > average]
print(newlist)
#tuple 2)
scores = tuple(rollist[:8])
print(scores)
highest=max(scores)
lowest=min(scores)
high_index=scores.index(highest)
low_index=scores.index(lowest)
print(high_index,low_index)
reverse_scores=list(scores[::-1])
print(reverse_scores)
user_score=int(input("enter kro:"))
if user_score in scores:
    print(scores.index(user_score))
else:
    print("not here")
#score[0]=123 error as cant change in tuple
firs_score, second_score, *remaining_scores = scores
print("First score:", firs_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)
#random library 3)
import random
random.seed(1024170270)
numbers = [random.randint(100, 900) for _ in range(100)]
print(numbers)
odd_numbers = [x for x in numbers if x % 2 != 0]
print("odd numbers:")
print(odd_numbers)
even_numbers = [x for x in numbers if x % 2 == 0]
print("\nEven numbers:")
print(even_numbers)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
primenumber=[ x for x in numbers if is_prime(x)]
print("\n",primenumber)
most_frequent = max(set(numbers), key=numbers.count)

print("\nMost frequent number:", most_frequent)
print("It occurs:", numbers.count(most_frequent))
#4)
digits=[1,0,2,4,1,7,0,2,7,0]
A={digit * 7 for digit in digits}
B={digit * 9 for digit in digits}
print("Set A:",A)
print("Set B:",B)
union=A.union(B)
print("union:",union)
intersection=A.intersection(B)
print("intersection",intersection)
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)
print("A - B:", A_minus_B)
print("B - A:", B_minus_A)
symmetric = A.symmetric_difference(B)
print("Symmetric difference:", symmetric)
print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))
X = int(input("Enter a value X: "))
A.discard(X)
print("Set A after discard:", A)

#Q5

my_dict = {
    "name": "Gurshan",
    "roll_no": "1024170270",
    "branch": "Computer Engineering",
    "age": 20,
    "city": "Faridkot"
}

print("Original dictionary:")
print(my_dict)

my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city to location:")
print(my_dict)

my_dict["cgpa"] = 8.5

print("\nAfter adding CGPA:")
print(my_dict)
my_dict["age"] += 1

print("\nAfter increasing age:")
print(my_dict)
dict_pop = my_dict.copy()
dict_del = my_dict.copy()

removed_branch = dict_pop.pop("branch")
del dict_del["branch"]

print("\nUsing pop():")
print(dict_pop)
print("Returned value:", removed_branch)

print("\nUsing del:")
print(dict_del)


print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(key, "→", value)
if "email" in my_dict:
    print("\nEmail:", my_dict["email"])
else:
    print("\nEmail is not present in the dictionary.")

friend_dict = {
    "name": "Rahul",
    "roll_no": "1024170271",
    "branch": "Computer Engineering",
    "age": 20,
    "city": "Amritsar"
}

merged_dict = {**my_dict, **friend_dict}

print("\nMerged dictionary:")
print(merged_dict)

string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_values)