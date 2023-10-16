class Account:
    class Node:
        
        def __init__(self, key, value, next = None):
            
            self.key = key
            self.value = value
            self.next = next

    class Data:

        def __init__(self, balance = 0, trans = [], password = ""):
            self.data = [balance, trans, password]

        def getBal(self):
            return self.data[0]

        def setBal(self, bal):
            self.data[0] = bal

        def getTrans(self):
            return self.data[1]

        def addTrans(self, trans):
            self.data[1].append(trans)

        def getPass(self):
            return self.data[2]

        def setPass(self, newPass):
            self.data[2] = newPass

        def __repr__(self):
            return " with password: " + str(self.getPass()) + " and Balance: " + str(self.getBal())


    def __init__(self, n = 1000):

        self.table = [None] * n
        self.keys = []

    def __len__(self):

        return len(self.keys)

    def __setitem__(self, key, value):

        index = hash(key) % len(self.table)
        if (key in self) is False:
            cur = self.table[index]
            self.table[index] = self.Node(key, value, cur)
            self.keys.append(key)
        else:
            cur = self.table[index]
            while cur is not None:
                if cur.key is key:
                    cur.value = value
                cur = cur.next

    def __getitem__(self, key):

        index = hash(key) % len(self.table)
        cur = self.table[index]
        while cur is not None:
            if cur.key is key:
                return cur.value
            cur = cur.next
        raise KeyError(key)

    def __contains__(self, key):

        index = hash(key) % len(self.table)
        cur = self.table[index]
        while cur is not None:
            if cur.key is key:
                return True
            cur = cur.next
        return False

    def __iter__(self):

        for key in self.keys:
            yield key

    def verify(self, key, password):
        #for login verification, 1 means everything matches, 0 means wrong password, 404 means id isnt in our database
        if key in self:
            if self[key].getPass() is password:
                return 1
            else:
                return 0
        else:
            return 404


    def __repr__(self):

        return "{" + ', '.join(repr(key) + ':' + repr(self[key]) for key in self) + "}"

########################################################################################################################

n = 10 #ACCOUNT AMOUNT
account = Account(n)
IDs = []
passwords = []
for i in range(0, n):
    arg = "user" + str(i)
    IDs.append(arg)
for i in range(0, n):
    passwords.append(hash(str(i ** i)))
print(IDs)
print(passwords)
for val in IDs:
    account[val] = Account.Data()
    account[val].setPass(passwords[int(val[4])])
print(account)
print("For verify method, if a 1 is returned then the password matches the ID, if a 0 is returned than the password doesn't match the ID, and if a 404 is return than the ID doesnt exist")
print(str(account.verify(IDs[0], passwords[0])) + " " + str(account.verify(IDs[1], passwords[0])) + " " + str(account.verify("user1", passwords[0])))
account[IDs[0]].addTrans(12)
account[IDs[0]].addTrans(13)
account[IDs[0]].addTrans(167)
print(account[IDs[0]].getTrans())

