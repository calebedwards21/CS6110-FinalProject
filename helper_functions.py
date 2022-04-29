
def verify_chain(chain, hashes):
    '''
        Verify that the current blockchain is valid
    ''' 
    verif_hash = compute_hash(chain)
    last_hash = hashes[-1]
    print(last_hash)
    print(verif_hash)
    
    if verif_hash != last_hash:
        return False
    else:
        return True
    
    
def compute_hash(block_chain):
    '''
        Computes the hash of the blockchain
    '''
    hash_string = '' 
    for c in block_chain:
        hash_string += c['fn'] + c['ln'] + c['dob'] + c['ssn']
        for v in c['votes']:
            hash_string += v
    return hash(hash_string)

# class Hash:
#     def __init__(self, blockchain):
#         self.blockchain = blockchain