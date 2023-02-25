# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# print()

# # modifying a list in a function


# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left.
#     Move each design to the completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# # The slice notation [:] makes a copy of the list to send to the function.
# print_models(unprinted_designs[:], completed_models)


# importing the printing functions module
import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
