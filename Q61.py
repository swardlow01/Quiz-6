#sarah wardlow
import dbm
db1 = dbm.open("photo_category", "c")
db1["cat.png"] = "a cat purring"
db1["bird.png"] = "a bird eating"
db1["dog.png"] = "a dog running"

for item in db1:
    print(item, db1[item])
