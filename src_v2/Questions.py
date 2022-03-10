import csv

class Question:
    def __init__(self,q,v1,v2):
        self.q = q
        self.v1 = v1
        self.v2 = v2
        self.used = False

class Questions:

    from Questions import Question

    def __init__(self):
        self.list_of_q = []
        with open('./../data/questions_v1.csv') as f:
            reader = csv.reader(f, delimiter='\t')
            for line in reader:
                new_q = Question(line[0],line[1],line[2])
                self.list_of_q.append(new_q)

    def __len__(self):
        return len(self.list_of_q)
    def __repr__(self):
        return "Question-thing"
    def __str__(self):
        return  str(self.list_of_q[0])+' '+str(self.list_of_q[1])+\
            ' '+self.list_of_q[2]
    def __getitem__(self,item):
        return self.list_of_q[item]
