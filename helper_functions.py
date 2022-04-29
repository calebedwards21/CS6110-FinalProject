def verify_chain(chain, hashes):
    '''
        Verify that the current blockchain is valid
    '''    
    last_hash = hashes[-1]
    verif_hash = hash(Hash(chain))
    
    if verif_hash != last_hash:
        return False
    else:
        return True


class Hash:
    def __init__(self, blockchain):
        self.blockchain = blockchain