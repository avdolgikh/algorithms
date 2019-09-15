# python3

class HashMap:
    def __init__(self, cardinality):
        self.cardinality = cardinality
        self.array = [None] * cardinality

    def set(self, key, value):
        hash = self.__get_hash(key, self.cardinality)

        if self.array[ hash ] is None:
            self.array[ hash ] = []

        list_ = self.array[ hash ]        

        for item in list_:
            if item[0] == key:
                item[1] = value
                return

        list_.append([key, value])

    def get(self, key):
        hash = self.__get_hash(key, self.cardinality)
        if self.array[ hash ] is not None:
            list_ = self.array[ hash ]
            for item in list_:
                if item[0] == key:
                    return item[1]
        return "not found"

    def remove(self, key):
        hash = self.__get_hash(key, self.cardinality)
        if self.array[ hash ] is not None:
            list_ = self.array[ hash ]
            item_index = 0
            while item_index < len(list_):
                if list_[item_index][0] == key:
                    del list_[item_index]
                else:
                    item_index += 1
            if not any(list_):
                self.array[ hash ] = None
    
    @staticmethod
    def __get_hash(x, m):
        p = 10000019
        a = 34
        b = 2        
        return ((a * x + b) % p ) % m


def process_query(query, phone_book):
    query = query.split()
    type = query[0]
    number = int(query[1])
    if type == 'add':
        name = query[2]
        phone_book.set(number, name)
    elif type == 'find':
        print(phone_book.get(number))
    elif type == 'del':
        phone_book.remove(number)
        

if __name__ == '__main__':    
    #queries = [ "add 911 police", "add 76213 Mom", "add 17239 Bob", "find 76213", "find 910", "find 911", "del 910", "del 911", "find 911", "find 76213", "add 76213 daddy", "find 76213" ]
    #queries = [ "find 3839442", "add 123456 me", "add 0 granny", "find 0", "find 123456", "del 0", "del 0", "find 0" ]
    #N = len(queries)

    N = int(input())
    queries = [input() for i in range(N)]
    
    phone_book = HashMap( int( N * 0.75 ) )

    for query in queries:
        process_query(query, phone_book)