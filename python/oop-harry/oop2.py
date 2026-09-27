class River:
    all_river = []
    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all_river
        River.all_river.append(self)

    def get_info(self):
        print(f"The length is {self.name} rive is {self.length} km")

volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# instance method
volga.get_info()
# class method
River.get_info(volga)


    