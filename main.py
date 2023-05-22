import pandas

# Functions go here

# Checks that user response is not blank
def not_blank(question):

  while True:
    response = input(question)

    # If response is blank, outputs an error
    if response == "":
      print("Please enter a name. This cannot be blank.")
    else:
      return response

# Checks that user enters an integer to a given question
def num_check(question):

  while True:
    try:
      response = int(input(question))
      return response
    
    except ValueError:
      print("Please enter an integer.")

# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

  # Ticket is $7.50 for under 16s
  if var_age < 16:
    price = 7.5

  # Ticket is $10.50 for users from 16-64
  elif var_age < 65:
    price = 10.5

  # Ticket is $6.50 for 65+
  else:
    price = 6.5

  return price

# Checks the user entered a valid reponse based on a list of options
def string_checker(question, num_letters, valid_responses):

  error = "Please choose {} or {}".format(valid_responses[0], valid_responses [1])
    
  while True:
    response = input(question).lower()
    for item in valid_responses:
      if response == item[:num_letters] or response == item:
        return item

    print(error)

# Currency formatting function
def currency(x):
  return "${:.2f}".format(x)

# main routine starts here

# Set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# List to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {"Name": all_names, "Ticket Price": all_ticket_costs, "Surcharge": all_surcharges}

# Ask user if they want to see instructions
want_instructions = string_checker("Do you want to read the instructions? (Yes or No): ", 1, yes_no_list)

if want_instructions == "yes":
  print("Instructions go here")


print()

# Loop to sell tickets

while tickets_sold < MAX_TICKETS:
   name = not_blank("Enter your name (or xxx to quit): ")
  
   if name == 'xxx':
     break

   age = num_check("Age: ")

   if 12 <= age <= 120:
      pass
   elif age < 12:
      print("Sorry, you are too young for this movie")
      continue
   else:
      print("That looks like a typo, please try again.")
      continue

   # Calculate ticket cost
   ticket_cost = calc_ticket_price(age)

   # Get payment method 
   pay_method = string_checker("Choose a payment method. (Cash or Credit): ", 2, payment_list)

   if pay_method == "cash":
    surcharge = 0
   else:
    # Calculate 5% surcharge if users are paying by credit card
    surcharge = ticket_cost * 0.05

   tickets_sold += 1

   # Add ticket name, cost and surcharge to lists
   all_names.append(name)
   all_ticket_costs.append(ticket_cost)
   all_surcharges.append(surcharge)

#create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency formatting (Uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
  mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("----- Ticket Data -----")
print()

# Output table with ticket data
print(mini_movie_frame)

# Output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))

print()
# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
  print("Congratulations, you have sold all of the tickets.")
else:
  print("You have sold {} ticket/s. There are {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))