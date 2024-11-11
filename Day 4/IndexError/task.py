# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# num_of_states=len(states_of_america)
# print(num_of_states)
# print(states_of_america[num_of_states-1])

#NESTED lists
#dirty_dozen=["Cherry", "Apple", "Pear","Cucumber", "Kale", "Spinach"]
fruits=["Cherry", "Apple", "Pear"]
vegetables=["Cucumber", "Kale", "Spinach"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][2])
print(dirty_dozen[1][1])
