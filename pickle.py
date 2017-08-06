import pickle as p #import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple','mango','carrot']
# Write to the file

f = open(shoplistfile,'wb')

p.dump(shoplist, f) # dump the object to a file

f.close()
