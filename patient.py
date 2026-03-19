class Patient:
    def __init__(self, temp, bpm):
        print("parent  init")
        self.temp = temp
        self.bpm = bpm

    def run(self):
        print("parent run")
        self.bpm += 5
        self.temp += 1


p1 = Patient(98, 75)
p1.run()
print(p1.temp)
print(p1.bpm)


class CancerPatient(Patient):
    pass
    # def __init__(self, temp, bpm):
    #     temp = temp * 2
    #     super().__init__(temp, bpm)

    # def run(self):
    #     self.bpm += 10
    #     self.temp += 2


p2 = CancerPatient(100, 75)
p2.run()
print(p2.temp)
print(p2.bpm)
