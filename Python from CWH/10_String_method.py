a = "Harry"
print(len(a))
print(a.upper())
print(a.lower())

b = "Fahad!!!!!"
print(b.upper())
print(b.lower())
print(b.rstrip("!"))

print(a.replace("Harry", "Arafat"))
print(a)

c = "Fahad Sarker !!!"
print(c.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())
print(blogHeading.center(60))

d = "My name is Fahad"
print(d.count("a"))

e = "Welcome to the Console !!!"
print(e.endswith("!"))
print(e.endswith("q"))
print(e.endswith("to", 4, 10))

f = "He's name is Dan. He is an honest man."
print(f.find("is"))
print(f.index("is"))

g = "WelcomeToTheConsole"
print(g.isalnum())

h = "Welcome00"
print(h.isalpha())
print(h.islower())

i = "We wish you Happy Birthday"
i1 = "We wish you Happy Birthday\n"
print(i.isprintable())
print(i1.isprintable())

j = "           "
j1 = "ashjdfgygavdsgh"
print(j.isspace())
print(j1.isspace())

k = "World Health Organization"
print(k.istitle())
k1 = "To kill a Mocking bird"
print(k1.istitle())

l = "python is a Interpreted Language"
print(l.swapcase())

m = "His name is Dan. Dan is a honest man."
print(m.title())