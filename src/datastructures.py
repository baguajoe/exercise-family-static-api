from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": 0,
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 1,
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 2,
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            },
        ]

    # read-only: Use this method to generate random member IDs when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Adds a new member with generated or existing ID
        if "id" not in member:
            member["id"] = self._generateId()

        member["last_name"] = self.last_name

        if "first_name" in member and "age" in member and "lucky_numbers" in member:
            self._members.append(member)
            return self._members
        else:
            return False

    def delete_member(self, id):
        # Deletes a member by ID
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, updates):
        # Updates an existing member by ID with new data
        for member in self._members:
            if member["id"] == id:
                member.update(updates)
                return member
        return False

    def get_member(self, id):
        # Retrieves a member by ID
        for member in self._members:
            if member["id"] == id:
                return member
        return False

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
