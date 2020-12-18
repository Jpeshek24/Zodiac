#We decided to use pyton turtle to integrate loops
import turtle

#This function delivers the message when you answer no to the first question.
def rubber_ducky():
  print("you are a rubber duck")

#This function makes the eyes of the smiley of sad face and is also where we put out loop.
def eyes():
    for i in range(2):    
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(60)

#This function creates the base yellow circle for the happy/sad face.
def yellow_circle():
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

#This is the user input that starts the code.
question = input("Would you like to know your astrological sign? ")

#If the user says yes to the previous question, this part will tell the user their zodiac sign.
if question == "yes":
  #This part draws the smiley face.
  turtle.speed(0)
  turtle.setposition(0,-100)
  turtle.pendown()
  turtle.color("yellow")

  yellow_circle()

  turtle.setposition(-25,25)
  turtle.color("black")
  eyes()
  turtle.right(90)
  turtle.penup()
  turtle.setposition(-50,30)
  turtle.pendown()
  turtle.pensize(10)
  turtle.color("black")
  turtle.circle(55,180,100)
  month = input("What month were you born? ")
  if question == "yes":
    month
  if month == "October":
    october = input("Was the day you were born between the 1st-22nd? ")
    if october == "yes":
      print("\nYou are a Libra. Libras love to be surrounded by art, culture and beauty in a soft, \nharmonious environment. You love good food and expensive things.\n")
    if october == "no":
      print("\nYou are a Scorpio. Many Scorpios are also drawn to “dark” things, and often wear the \ncolor black, or a shocking tone like red or hot pink. Like Pluto, Scorpio’s \npower often emanates from a hidden source, even when you don’t say a word. Mysterious\nScorpio is the zodiac’s most misunderstood sign.")
  if month == "November":
    november = input("Was the day you were born between the 1st-21st? ")
    if november == "yes":
      print("\nYou are a Scorpio. Many Scorpios are also drawn to “dark” things, and often wear the \ncolor black, or a shocking tone like red or hot pink. Like Pluto, Scorpio’s \npower often emanates from a hidden source, even when you don’t say a word. Mysterious\nScorpio is the zodiac’s most misunderstood sign.")
    if november == "no":
      print("\nYou are a Saggitarius. As the zodiac’s traveler, Sagittarius is the ultimate free spirit: \noptimistic, open-minded and ambitious. You’re happiest in wide-open spaces with plenty \nof adventure and excitement.")
  if month == "December":
    december = input("Was the day you were born between the 1st-21st? ")
    if december == "yes":
      print("\nYou are a Saggitarius. As the zodiac’s traveler, Sagittarius is the ultimate free spirit: \noptimistic, open-minded and ambitious. You’re happiest in wide-open spaces with plenty \nof adventure and excitement.")
    if december == "no":
      print("\nYou are a Capricorn. Accustomed to regular butt-kickings from Saturn, you often see life \nas an uphill battle, with the ultimate reward arriving only through suffering and sacrifice.")  
  if month == "January":
    january = input("Was the day you were born between the 1st-21st? ")
    if january == "yes":
      print("\nYou are a Capricorn. Accustomed to regular butt-kickings from Saturn, you often see life \nas an uphill battle, with the ultimate reward arriving only through suffering and sacrifice.")
    if january == "no":
      print("\nYou are an Aquarius. Just like your celestial overlord, \nyou’ve been known to do things your own way, moving on a path different \nfrom everyone else’s. Some call you eccentric, others appreciate your cutting-edge \noriginality and authentic style.")  
  if month == "February":
    february = input("Was the day you were born between the 1st-18th? ")
    if february == "yes":
      print("\nYou are an Aquarius. Just like your celestial overlord, \nyou’ve been known to do things your own way, moving on a path different \nfrom everyone else’s. Some call you eccentric, others appreciate your cutting-edge \noriginality and authentic style.")
    if february == "no":
      print("\nYou are a Pisces. Your imagination is the perfect hideout \nwhen you want to escape, since Pisces is so creative. You love dancing \n(Pisces rules the feet), movies, poetry, and music.") 
  if month == "March":
    march = input("Was the day you were born between the 1st-20th? ")
    if march == "yes":
      print("\nYou are a Pisces. Your imagination is the perfect hideout \nwhen you want to escape, since Pisces is so creative. You love dancing \n(Pisces rules the feet), movies, poetry, and music.")
    if march == "no":
      print("\nYou are an Aries. Highly impatient and competitive, many Aries have the fighting spirit of \nyour mythological ruler. You love to be a hero–or to be swept away by one.") 
  if month == "April":
    april = input("Was the day you were born between the 1st-19th? ")
    if april == "yes":
      print("\nYou are an Aries. Highly impatient and competitive, many Aries have the fighting spirit of \nyour mythological ruler. You love to be a hero–or to be swept away by one.")
    if april == "no":
      print("\nYou are a Taurus. Your sign loves great food, romance and beautiful things. Venus kicks \nyour five senses into high gear, so you are are happiest when surrounded by the best of \neverything. Satin sheets, gourmet dinners, a glass of red wine, and boom… you’re \nrelaxing into one of your famous, 14-hour naps. Not that you don’t work hard, too.")
  if month == "May":
    may = input("Was the day you were born between the 1st-20th? ")
    if may == "yes":
      print("\nYou are a Taurus. Your sign loves great food, romance and beautiful things. Venus kicks \nyour five senses into high gear, so you are are happiest when surrounded by the best of \neverything. Satin sheets, gourmet dinners, a glass of red wine, and boom… you’re \nrelaxing into one of your famous, 14-hour naps. Not that you don’t work hard, too.")
    if may == "no":
      print("\nYou are a Gemini. The Gemini mind (and mouth!) is a busy machine, always moving at \nwarp speed. That’s because your sign is ruled by Mercury, the planet of communication.")
  if month == "June":
    june = input("Was the day you were born between the 1st-20th? ")
    if june == "yes":
      print("\nYou are a Gemini. The Gemini mind (and mouth!) is a busy machine, always moving at \nwarp speed. That’s because your sign is ruled by Mercury, the planet of communication.")
    if june == "no":
      print("\nYou are a Cancer. You’re intuitive and nurturing, even psychic. Pay attention to your \ndreams, especially near a Full Moon.")
  if month == "July":
    ly = input("Was the day you were born between the 1st-22nd? ")
    if july == "yes":
      print("\nYou are a Cancer. You’re intuitive and nurturing, even psychic. Pay attention to your \ndreams, especially near a Full Moon.")
    if july == "no":
      print("\nYou are a Leo. When the whole universe revolves around you, it’s hard to be humble! Like the \nSun, Leo heats everything up with its dazzling drama. And when the Sun sets, it’s ice, ice \nbaby. That’s why friends of Leo know to keep them happy and shining… or else.")
  if month == "August":
    august = input("Was the day you were born between the 1st-22nd? ")
    if august == "yes":
      print("\nYou are a Leo. When the whole universe revolves around you, it’s hard to be humble! Like the \nSun, Leo heats everything up with its dazzling drama. And when the Sun sets, it’s ice, ice \nbaby. That’s why friends of Leo know to keep them happy and shining… or else.")
    if august == "no":
      print("\nYou are a Virgo. Virgos are always analyzing everything, forming opinions and judgments. \nOn the outside, you seem sweet and innocent, but your quick mind never misses a detail.")
  if month == "September":
    september = input("Was the day you were born between the 1st-22nd? ")
    if september == "yes":
      print("\nYou are a Virgo. Virgos are always analyzing everything, forming opinions and judgments. \nOn the outside, you seem sweet and innocent, but your quick mind never misses a detail.")
    if september == "no":
      print("\nYou are a Libra. Libras love to be surrounded by art, culture and beauty in a soft, \nharmonious environment. You love good food and expensive things.\n")

#This is the message given when the user says no
else:
  rubber_ducky()
  #This part of the code draws the sad face.
  turtle.speed(0)
  turtle.setposition(0,-100)
  turtle.pendown()
  turtle.color("yellow")

  yellow_circle()

  turtle.setposition(-25,25)
  turtle.color("black")
  eyes()
  turtle.left(90)
  turtle.penup()
  turtle.setposition(57,-50)
  turtle.pendown()
  turtle.pensize(10)
  turtle.color("black")
  turtle.circle(55,180,100)