def get_lines(filename):
    with open(filename, 'r+') as f:
        return f.readlines()

def get_lines(filename):
    with open(filename, 'r+') as f:
        for line in f:
            print(line)
            
def get_lines(filename):
    with open(filename, 'r+') as f:
        for line in f:
            yield line
            

def get_lines(filename, n):
    l = []
    i = 1
    with open(filename, 'r+') as f:
        for line in f:
            l.append(line)
            i += 1
            if i%n == 0:
                yield l
            
f = open("test.py", 'r+') 
f.readlines()          