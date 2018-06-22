from basic import db, Puppy

# create
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()
frank = Puppy('Frankie', 4)
db.session.add(frank)
# read
all_puppies = Puppy.query.all() # list of puppie obj in table
print("PRINTING ALL PUPPIES")
print(all_puppies)

# select by id
puppy_one = Puppy.query.get(1)

print("PRINTING ONE PUPPY")
print(puppy_one.name)

# filters
# produce some sql code
puppy_frankie = Puppy.query.filter_by(name="Frankie")
print("PRINTING ALL FRANKIES")
print(puppy_frankie.all())

# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# delete
second_pup = Puppy.query.get(3)
print("PRINTING SECOND PUP\n", second_pup)
db.session.delete(second_pup)
db.session.commit()

#
all_puppies = Puppy.query.all()
print("PRINTING ALL PUPPIES")
print(all_puppies)

