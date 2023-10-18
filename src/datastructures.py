
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

family_initial_data = [{
    "name":"John",
    "age":33,
    "lucky_numbers":[7, 13, 22]
},{
    "name":"Jane",
    "age":35,
    "lucky_numbers":[10, 14, 3]
},{
    "name":"Jimmy",
    "age":5,
    "lucky_numbers":[1]
}]

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = []
        for member_data in family_initial_data:
            member_data.update(
                id=self._generateId()
            )
            self._members.append(member_data)


    def update_member(self, id, updated_data):
        # fill this method and update the return
        for member in self._members:
            if member.get("id") == id:
                member.update(updated_data)
                return True
        return False

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member.get("id") == id:
                self._members.remove(member)
                return True
        return False
        pass

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member.get("id") == id:
                return {
                    "name": member.get("name"),
                    "id": member.get("id"),
                    "age": member.get("age"),
                    "lucky_numbers": member.get("lucky_numbers")
                }
        return None
        pass
    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
