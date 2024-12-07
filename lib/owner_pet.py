class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if not isinstance(name, str) or not isinstance(pet_type, str):
            raise Exception("Name and pet type must be strings.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type. Valid types are: {', '.join(Pet.PET_TYPES)}")
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        
        if pet.owner is None:
            pet.owner = self
        else:
            print(f"{pet.name} already has an owner: {pet.owner.name}") 
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

