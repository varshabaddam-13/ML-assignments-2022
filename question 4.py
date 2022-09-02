# given list of it companies
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("length of it_companies : ", len(it_companies))

# adding twitter to it_companies
it_companies.add("Twitter")
print("it_companies after adding twitter :", it_companies)

# inserting multiple it companies
companies = ["NCR", "Wipro", "TCS"]
it_companies.update(companies)
print("it_companies after adding multiple companies :", it_companies)

# removing one company
it_companies.remove("Twitter")
print("it_companies after removing one company : ", it_companies)

# Difference between remove and discard method
# The remove() method will raise an error if the specified item does not exist, and the discard() method will not raise error.

# joining A and B
C = A.union(B)
print("joining A and B gives :", C)

# finding A intersection B
I = A.intersection(B)
print("Intersection of A and B is:", I)

# checking is A subset of B
check = A.issubset(B)
if check:
    print("A is subset of B")
else:
    print("A is not a subset of B")

# checking are A and B are disjoint sets
check1 = A.isdisjoint(B)
if check1:
    print("A and B are disjoint sets")
else:
    print("A and B are not disjoint sets")

# joining A with B and B with A
A_join_B = A.union(B)
B_join_A = B.union(A)
print("A join B is :", A_join_B)
print("B join A is :", B_join_A)

# symmetric difference between A and B
D = A.symmetric_difference(B)
print("symmetric difference between A and B is :", D)

# deleting all the sets
it_companies.clear()
A.clear()
B.clear()

# converting ages list to set
age_set = set(age)
print("length of ages list is : ", len(age))
print("length of ages set is :", len(age_set))
print("length of ages list is greater than the ages set")
