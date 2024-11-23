#1
class Cat:
    def __init__(self, start, middle, end):
        self.start = start
        self.middle = middle
        self.end = end

    def cat_life(self):
     return f"Start of his life: {self.start} \n Middle of his life: {self.middle} \n End of his life: {self.end}"

cat=Cat("He borns as a homeless", "He was find by some kind person", "He dies as a very good cat")
print(cat.cat_life())