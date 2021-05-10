


class character :
    def __init__(self,name,streetname,age,gender,metatype,height,weight,ethnic,body,agility,reaction,strength,willpower,logic,intuition,charisma,edge,essence,magic):
        self.name = name
        self.streetname = streetname
        self.age = age
        self.gender = gender
        self.metatype = metatype
        self.height = height
        self.weight = weight
        self.ethnic = ethnic
        self.body = body
        self.agility = agility
        self.reaction = reaction
        self.strength = strength
        self.willpower = willpower
        self.logic = logic
        self.intuition = intuition
        self.charisma = charisma
        self.edge = edge
        self.essence = essence
        self.magic = magic

        def initiative(self):
            return reaction+intuition

        def composure(self):
            return charisma+willpower

        def judgeIntentions(self):
            return charisma+intuition

        def lifting(self):
            return body+strength

        def memory(self):
            return logic+willpower

        

print ('hello world')



 





