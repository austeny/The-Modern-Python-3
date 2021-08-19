class GrumpyDict(dict):
    #don't need __init__ since we don't want to change attributes or store data just override methods
    def __repr__(self):
        return "None of your business"
    
    def __missing__(self, key):
        return f"{key} don't exist!"

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        print(f"Fine I set {key} to {val}")
    
data = GrumpyDict({'fisrt': 'Tom', 'animal': 'dog'})
print(data)
data['city'] = 'Boston'
print(data['test'])