# A few friends just created their car company. At first it's just the founders, three friends.
staff = ["Barry Dalive", "Ellie Kopter", "Zoltan Pepper"]

# They built the product, now they need a sales team to sell it. They hired four salesmen.
sales = ["Joe King", "Sue Perman", "Hayden Seek", "Iona Faskar"]

# Add the salesmen to the staff. Check to make sure the final list has length 7.
staff.____(sales)
print(f"There are now {len(staff)} staff members.")

# It would be easier to find employees if they were sorted. Sort the list alphabetically. Check that it worked.
staff.____()
print(staff)

# An investor took a majority share in the company, and is planning to get involved with day-to-day business activities.
# He wants to be considered a founder, and employee #1.
investor = "Leon Mux"

# Zoltan Pepper, Iona Faskar and Sue Perman say the company culture has changed and they'd rather leave if the
# new investor insists on going through with his decision.
leaving_employees = ["Zoltan Pepper", "Iona Faskar", "Sue Perman"]

# Apparently Leon changed his mind and won't be going through with his decision.
going_through = ____

# Leon says he reconsidered, and it's important that he comes first in the list.
going_through = ____

# Leon adds himself as Employee ## and the group leaves as announced.
    print("\nWelcome to the company, Employee #1!")
    staff.____(0, investor)
    print(staff)
    for ____ in leaving_employees:
        print(f"\n{employee}'s farewell party is on! 🥳")
        staff.____(employee)
        print(f"There are now {len(staff)} staff members:")
        for ____ in staff:
            print(f"- {staff_member}")

# Leon says it's time to reorganize the company and store the names and titles in a dictionary.
# Barry Dalive will be Chief Happyness Officer.
# Ellie Kopter will be Chief Visionary Officer.
# The other ones will be Solutions Consultants.
# They are employee number how much and how much again?
barry_dalive_index = staff.____("Barry Dalive")
ellie_kopter_index = staff.____("Ellie Kopter")
print(f"\nBarry Dalive is employee #{barry_dalive_index + 1} (but in Python he's Employee #{barry_dalive_index})")
print(f"Ellie Kopter is employee #{ellie_kopter_index + 1} (but in Python she's Employee #{ellie_kopter_index})")

company = {
    staff[0]: "Founder",
    staff[1]: "Chief Happyness Officer",
    staff[2]: "Chief Visionary Officer",
}

solutions_consultants = []
for ____ in staff :
    if ____ not in company.____():
        solutions_consultants.____(staff_member)

for ____ in solutions_consultants:
    company[consultant] = "____"

print("")
for name, title in company.____():
    print(f"{name} is now {title}.")

# Leon realizes in Python he's actually Employee #0:
print(f"Leon is Employee #{staff.index("Leon Mux")}. Not funny! Let's clear the list")
# He doesn't find that funny at all.
# He wants the staff list to be deleted immediately. His dictionary is much better anyway.
staff.____()
print(f"\nStaff cleared: {staff}")

# There's more managers than employees, it doesn't look serious.
# They need to hire a new Solutions Consultant.
# A guy shows up and says he's interested in the job.
# He fits the profile, but he says he doesn't like the job title.
# He will only join if he can change his job title to Assistant Regional Manager.
# Leon says OK.
applicant = {"Dwight Schrute": "Assistant to the Regional Manager"}
company.____(applicant)

while company["Dwight Schrute"] != "Assistant Regional Manager":
    print("")
    print(f"Dwight: \"There's been a mistake in my title! I'm {company["Dwight Schrute"]}!!!\"")
    print("Leon:   \"Too bad... It's too hard to change now. Don't get so worked up about a title!\"")
    # Show Leon it's easy to change the title.
    company["Dwight Schrute"] = "____"
    print("Title changed")
    print("")


print(f"Dwight's title is now {company["Dwight Schrute"]}")
