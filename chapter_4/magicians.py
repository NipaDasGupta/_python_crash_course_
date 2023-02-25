magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}")

print()

cats = ['persian', 'maine coon', 'british shorthair', 'bengal']
for cat in cats:
    print(cat)

print()

# for magician in magicians:
# # IndentationError: expected an indented block
# print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
#
# print("Thank you, everyone. That was a great show!")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
# logical error
print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great show!")

# message = "hello python world!"
# # IndentationError: unexpected indent
#     print(message)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# logical error
    print("Thank you everyone, that was a great magic show!")

# # SyntaxError: invalid syntax, no colon
# for magician in magicians
#     print(magician)
