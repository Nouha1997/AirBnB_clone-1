#!usr/bin/python3
"""Test delete feature"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

#All states
all_states = fs.all(State)
print("All States: {}": format(len(all_states.keys())))
for state_key in all_states.keys():
print(all_states[state_key])

#Creates a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

#All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
print(all_states[state_key])

#Creates another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save
print("Another State: {}".format(another_state))

#All States 
all_states = fs.all(State)
print("All States: : {}".format(len(all_states.keys())))
for state_key in all states.keys():
print(all_states[state_key])

#deletes the new State
fs.delete(new_state)


#All States
all_states = fs.all(State)
print("Allstates: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
print(all_states[states_key])
