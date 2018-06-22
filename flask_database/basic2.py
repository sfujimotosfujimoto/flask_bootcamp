from models import db,Puppy,Owner,Toy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

#check
# print(Puppy.query.all())

# rufus = Puppy.query.filter_by(name='Rufus').first()

# create owner project
jose = Owner('Jose',rufus.id,)

# give rufus some toys
toy1 = Toy("Chew Toy", rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

#grab rufus after add
rufus = Puppy.query.filter_by(name='Rufus').first()

print(rufus)