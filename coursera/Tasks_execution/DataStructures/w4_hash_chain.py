# python3


def poly_hash(s, p, x):
    hash = 0
    for index in reversed(range(len(s))):
        hash = (hash * x + s[index]) % p
    return hash
    

class HashTable:
    def __init__(self, cardinality):
        self.cardinality = cardinality
        self.array = [None] * cardinality

    def add(self, value):
        hash = self.__get_hash(value, self.cardinality)
        if self.array[ hash ] is None:
            self.array[ hash ] = []
        list_ = self.array[ hash ]
        if value not in list_:
            list_.append(value)

    def delete(self, value):
        hash = self.__get_hash(value, self.cardinality)
        if self.array[ hash ] is not None:
            list_ = self.array[ hash ]
            item_index = 0
            while item_index < len(list_):
                if list_[item_index] == value:
                    del list_[item_index]
                    break
                else:
                    item_index += 1
            if not any(list_):
                self.array[ hash ] = None

    def find(self, value):
        hash = self.__get_hash(value, self.cardinality)
        if self.array[ hash ] is not None:
            list_ = self.array[ hash ]
            for item in list_:
                if item == value:
                    return "yes"
        return "no"

    def check(self, index):
        if index < len(self.array) and self.array[ index ] is not None:
            return " ".join(reversed(self.array[index]))
        return ""
    
    @staticmethod
    def __get_hash(value, m):
        p =  1000000007
        x = 263
        return poly_hash([ord(char) for char in value], p, x) % m


def process_query(query, hash_table):
    query = query.split()
    type = query[0]
    value = query[1]
    if type == 'add':        
        hash_table.add(value)
    elif type == 'find':
        print(hash_table.find(value))
    elif type == 'del':
        hash_table.delete(value)
    elif type == 'check':
        print(hash_table.check(int(value)))


if __name__ == '__main__':
    #queries = [ "add world", "add HellO", "check 4", "find World", "find world", "del world", "check 4", "del HellO", "add luck", "add GooD", "check 2", "del good" ]
    #queries = [ "add test", "add test", "find test", "del test", "find test", "find Test", "add Test", "find Test" ]
    #queries = [ "check 0", "find help", "add help", "add del", "add add", "find add", "find del", "del del", "find del", "check 0", "check 1", "check 2" ]
    #N = len(queries)
    #m = 3

    m = int(input())
    N = int(input())
    queries = [input() for i in range(N)]
    
    hash_table = HashTable(m)

    for query in queries:
        process_query(query, hash_table)