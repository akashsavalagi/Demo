ten_things = "apple mangao orange pineapple grape rasberry chickoo"

print "wait there are not yet 10 things in list"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding : ", next_one
	stuff.append(next_one)
	print "there are %d items now." % len(stuff)

print "there we go ", stuff

print "Lets do some stuff."

print stuff[1]
print stuff[-1]

print stuff.pop()

print ' '.join(stuff)
print '#'.join(stuff[3:5])