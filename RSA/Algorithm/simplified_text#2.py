import copy
import math

IndexTable = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"," ",".","?","$","0","1","2","3","4","5",
              "6","7","8","9"]

def string2num(*List):
    message = copy.deepcopy(*List)
    num = []
    for i in message:
        #print("i: {}".format(i))
        for j in IndexTable:
            if i == j:
                num.append(IndexTable.index(j))
                #print("numerircal: {}".format(num))
    #print("num:{}".format(num))
    return num

def plaintext_digraphs(*List):
    List = copy.deepcopy(*List)
    digraphs = []
    for i in range(len(List)):
        if i % 2 != 0:
            continue
        if i + 1 == len(List):
            break
        else:
            num = 40 * (List[i]) + 1 * (List[i+1])

        digraphs.append(num)
    return digraphs

def ciphertext_trigraphs(*List):

    List = copy.deepcopy(*List)
    trigraphs = []
    for i in range(len(List)):
        a = List[i] // (40**2)
        r1 = List[i] - (a * 40**2)
        b = r1 // 40
        c = ( List[i] - (a * 40**2 + b * 40) ) % 40
        trigraphs.append(a)
        trigraphs.append(b)
        trigraphs.append(c)
    return trigraphs

def num2string(*List):
    List = copy.deepcopy(*List)
    # Convert it into the text
    text = []
    for j in range(len(List)):
        text.append(IndexTable[List[j]])
    text = ''.join(text)
    
    return text

def RSA(pub_key,n):
    floor_number = math.floor(math.sqrt(n))
    for i in range(1, floor_number):
        if n % i == 0 and i != 1:
            p = i
            q = n // i

    phi_n = (p-1) * (q-1)

    for j in range(1, n):
        if (j * pub_key) % phi_n == 1:
            pri_key = j

    return pri_key

def ciphertext_encryption_graphs(Encrypted_Message, blocks, base):
    length = len(Encrypted_Message)
    segment = length // blocks

    print(Encrypted_Message)
    print("length:{}".format(length))
    print("segment:{}".format(segment))
    
    chunks = []
    for i in range(0, len(Encrypted_Message), blocks):
        chunk = Encrypted_Message[i:i+blocks]
        chunk = string2num(chunk)
        chunks.append(chunk)
    print(chunks)

    nums_chuncks = []
    for sub_chuncks in chunks:
        print(sub_chuncks)
        for element in range(len(sub_chuncks)):
            if element + blocks - 1 == len(sub_chuncks):
                break
            chunks_nums = 0
            for index in range(blocks):
                co_num = blocks - 1 - index
                chunks_nums = chunks_nums + (base**index) * sub_chuncks[element + co_num]
                if co_num == 0:
                    num_chunks = chunks_nums
                    nums_chuncks.append(num_chunks)
    print(nums_chuncks)
    return nums_chuncks
            # Calculation Procedure
            # chunks_nums = (base**0) * sub_chuncks[k+6] + \
            #               (base**1) * sub_chuncks[k+5] + \
            #               (base**2) * sub_chuncks[k+4] + \
            #               (base**3) * sub_chuncks[k+3] + \
            #               (base**4) * sub_chuncks[k+2] + \
            #               (base**5) * sub_chuncks[k+1] + \
            #               (base**6) * sub_chuncks[k] + \

def plaintext_decryption_graphs(blocks, base, *List):
    List = copy.deepcopy(*List)
    plaintext_nums = []
    for i in List:
        remainder = i
        for index in range(blocks):
            co_num = blocks -1 - index
            plaintext_num = remainder // (base ** (co_num))
            remainder = i % (26 ** (co_num))
            plaintext_nums.append(plaintext_num)
    print(plaintext_nums)
    return plaintext_nums
    
def rsa_algorithm(key, n, *List):
    List = copy.deepcopy(*List)
    results = []
    # Encryption and Decryption
    for num in List:
        result = pow(num, key) % n
        results.append(result)
    return results

def example1():
    print("\n-------------example #1-------------\n")

    message = "SEND $7500"
    message = list(message)
    print("plaintext: {}".format("".join(message)))

    num = string2num(message)
    digraphs = plaintext_digraphs(num)
    
    pub_key = 179
    n = 2047

    num_ciphertext = ciphertext_encryption_graphs(message, 2, 40)
    trigraphs = rsa_algorithm(pub_key, n, num_ciphertext)
    print(trigraphs)
    # TODO 
    ciphertext = num2string(trigraphs)
    print("ciphertext: {}".format(ciphertext))

def example2():
    print("\n-------------example #2-------------\n")
    # The Encrypted Message
    Encrypted_Message = "ARHILFKAODSTOSBSTWFQL"
    Encrypted_Message = list(Encrypted_Message)
    
    n = 536813567
    pri_key = 201934721
    cipher_num = []
    cipher_num = ciphertext_encryption_graphs(Encrypted_Message, 7, 26)
    #text_num = rsa_algorithm(pri_key, n, cipher_num)
    # Modular Exponentiation Calculator
    cipher_num = [20002966, 11198842, 12223445]
    print("After Modular:{}".format(cipher_num))
    plaintext_nums = plaintext_decryption_graphs(6, 26, cipher_num)

    plaintext = num2string(plaintext_nums)
    print(plaintext)

def example3():
    print("\n-------------example #3-------------\n")
    # The Encrypted Message
    Encrypted_Message = "BNBPPKZAVQZLBJ"
    Encrypted_Message = list(Encrypted_Message)
    
    n = 536813567
    pri_key = 201934721
    cipher_num = []
    cipher_num = ciphertext_encryption_graphs(Encrypted_Message, 7, 26)
    #text_num = rsa_algorithm(pri_key, n, cipher_num)
    # Modular Exponentiation Calculator
    cipher_num = [45005201, 56094542]
    print("After Modular:{}".format(cipher_num))
    plaintext_nums = plaintext_decryption_graphs(6, 26, cipher_num)

    plaintext = num2string(plaintext_nums)
    print(plaintext)

if __name__== "__main__":
    
    #example1()
    example2()
    example3()
    


