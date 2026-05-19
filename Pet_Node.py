class PetNode:
    def __init__(self, pet_id, name, breed, owner, severity):
        self.pet_id   = pet_id
        self.name     = name
        self.breed    = breed
        self.owner    = owner
        self.severity = severity
        self.next     = None