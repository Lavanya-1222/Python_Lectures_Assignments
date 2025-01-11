# 1. A library has a list of books with their respective ratings. Write a function to find the top-rated book. If multiple books have the same highest rating, return the first one alphabetically. Use appropriate data structures and a combination of lambda and sorted.
# d={'man':8,'frog':10,'mindset':4,'deepwork':10}
# max=max(d.values())
# l=[k for k,v in d.items() if v==max]

# print(sorted(l))
# output:
# ['deepwork', 'frog']
    

# 2. A chef is organizing ingredients stored in different categories. Write a program that takes two lists of categories and items, zips them together, and prints a sorted list of the items for each category using a loop.
cat=['kiteche','Clothing','Acsseries']
ite=['Mixer','T-Shirt','Ear-Rings']

for i,v in zip(cat,ite):
    print(i,v)
# output:
# kiteche Mixer
# Clothing T-Shirt
# Acsseries Ear-Rings



# 3. A game development company wants to evaluate player scores. Write a function that takes a list of player scores, removes the highest and lowest scores, and returns the average of the remaining scores. Ensure the function handles cases where there are fewer than three scores gracefully.
l=[10,20,30,40,50,60]

# 4. A store has a weekly sale where the discount percentage depends on the day of the week. Write a program using zip to pair each day with its discount percentage and print the day with the highest discount.

# 5. A sports coach needs to evaluate athletes' performance metrics. Write a program that uses a list of tuples, where each tuple contains an athlete's name and scores in three events. Use enumerate and a loop to find the athlete with the highest average score.

# 6. A gardener tracks the growth of plants each day. Write a program that takes a list of daily heights and calculates the maximum growth in one day, the total growth over a week, and the average growth. Use a combination of loops, functions, and eval.

# 7. A teacher has a list of students and their test scores. Write a function using lambda and filter to find all students who scored above a certain threshold. Then, return their names and scores sorted by scores in descending order.

# 8. A weather monitoring app stores daily temperatures in two lists: one for city A and one for city B. Write a program that uses zip to pair the temperatures and finds the day when the temperature difference between the two cities was the highest.

# 9. An artist has multiple paintings, each priced differently. Write a function to calculate the total cost after applying a discount based on the number of paintings purchased. Use lambda for the discount calculation and ensure it handles cases where no paintings are bought.

# 10. A bakery tracks daily sales of different items. Write a program that uses enumerate to assign a unique ID to each item and prints a sorted list of items based on their sales.

# 11. A treasure hunter deciphers clues using patterns of numbers. Write a function that generates a sequence of numbers based on a formula using eval. Ensure the formula can be dynamically entered by the user.

# 12. A tech company conducts coding challenges. Write a program that accepts a list of participants' names and their scores, uses lambda to sort them by scores, and finds the top three participants.

# 13. A travel agency pairs countries with their capitals in two separate lists. Write a program that zips them together, sorts the pairs alphabetically by country name, and displays the results in a user-friendly format.

# 14. A bookstore offers discounts based on the total number of books purchased. Write a function that calculates the total cost using lambda and returns the discounted price for a given number of books and their prices.

# 15. A wildlife researcher tracks the weights of animals over time. Write a program that takes two lists of weights recorded on different days, zips them together, and uses a loop to find the maximum weight change between any two days.\