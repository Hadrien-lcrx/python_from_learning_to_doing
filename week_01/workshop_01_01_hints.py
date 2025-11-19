# A few friends just created their car company. At first it's just the founders, three friends.
staff = ["Barry Dalive", "Ellie Kopter", "Zoltan Pepper"]

# They built the product, now they need a sales team to sell it. They hired four salesmen.
sales = ["Joe King", "Sue Perman", "Hayden Seek", "Iona Faskar"]

# Add the salesmen to the staff. Check to make sure the final list has length 7.
## WHich function lets you extend a list with another one?_
____

## Which function gives you the length of a Python object?
____

# It would be easier to find employees if they were sorted. Sort the list alphabetically. Check that it worked.
# Which function lets you sort a list?

# An investor took a majority share in the company, and is planning to get involved with day-to-day business activities.
# He wants to be considered a founder, and employee #1.
investor = "Leon Mux"

# Zoltan Pepper, Iona Faskar and Sue Perman say the company culture has changed and they'd rather leave if the
# new investor insists on going through with his decision.
leaving_employees = ["Zoltan Pepper", "Iona Faskar", "Sue Perman"]

# Apparently Leon changed his mind and won't be going through with his decision.
# Which type lets you declare a condition that is not true in Python?
going_through = ____

# Leon says he reconsidered, and it's important that he comes first in the list.
# Which type lets you declare a condition that is true in Python?
going_through = ____

# The group leaves as announced.
# If Leon goes though with his decision...
if going_through == True:
    # then he is shows up first in the list...
    ____
    # and for each employee that is leaving
    ____
        # We throw them a farewell party and remove them from the staff
        ____
        # We can check who is left in the employees after each departure
        ____

# Leon says it's time to reorganize the company and store the names and titles in a dictionary.
# Barry Dalive will be Chief Happyness Officer.
# Ellie Kopter will be Chief Visionary Officer.
# The other ones will be Solutions Consultants.
# They are employee number how much and how much again?
# How do you get the index of a specific value in a list?
____

# If we build a company dictionary, what do we put as keys and what do we put as values?
____

# Leon realizes in Python he's actually Employee #0:
# He doesn't find that funny at all.
# He wants the staff list to be deleted immediately. His dictionary is much better anyway.
# Which function allows you to clear a list?

# There's more managers than employees, it doesn't look serious.
# They need to hire a new Solutions Consultant.
# A guy shows up and says he's interested in the job.
# He fits the profile, but he says he doesn't like the job title.
# He will only join if he can change his job title to Assistant Regional Manager.
# Leon says OK.
applicant = {"Dwight Schrute": "Assistant to the Regional Manager"}

# How do you update a dictionary with another dictionary?
____

while company["Dwight Schrute"] != "Assistant Regional Manager":
    print("")
    print(f"Dwight: \"There's been a mistake in my title! I'm {company["Dwight Schrute"]}!!!\"")
    print("Leon:   \"Too bad... It's too hard to change now. Don't get so worked up about a title!\"")
    # Show Leon it's easy to change the title.
    # How do you update the value of an existing key in a dictionary?
    ____
    print("Title changed")
    print("")

print(f"Dwight's title is now {company["Dwight Schrute"]}")

print(company)