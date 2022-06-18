import random

lucky_num = random.randint(1,101)

fortune_num = random.randint(1,5)

fortune_text = ""

if fortune_num == 1:
  fortune_text = "You are stepping into your highest Potential."

if fortune_num == 2:
  fortune_text = "Use your insight of perception to achieve Success."

if fortune_num == 3:
  fortune_text = "Enjoy this new month's coming abundance!"

if fortune_num == 4:
  fortune_text = "You are entering your time of Unlimited Potential."

if fortune_num == 5:
  fortune_text = "Awaken your deepest desires & receive your Gifts!"

print(f"{fortune_text} Your Lucky Number is: {lucky_num}")


