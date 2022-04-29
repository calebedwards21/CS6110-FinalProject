from helper_functions import *

class Voter:
    
    def __init__(self, fn, ln, dob, ssn, pk):
        '''
            Constructor
        '''
        self.fn = fn
        self.ln = ln
        self.dob = dob
        self.ssn = ssn
        self.pk = pk
        
        
    def create_block(self, votes, block_chain=None, hashes=None):
        '''
        '''
        block = {}
        # Create 1st block in chain
        if not block_chain and not hashes:
            hashes = []
            block_chain = []
            block['fn'] = self.fn # Encrypt
            block['ln'] = self.ln # Encrypt
            block['dob'] = self.dob # Encrypt
            block['ssn'] = self.ssn # Encrypt
            block['votes'] = votes
            block_chain.append(block)
            block_hash = hash(Hash(block_chain))
            hashes.append(block_hash)
            return (block, hashes)
        # Create             
        else:
            isVerified = verify_chain(block_chain, hashes)
            if not isVerified:
                return None
            else:
                block['fn'] = self.fn # Encrypt
                block['ln'] = self.ln # Encrypt
                block['dob'] = self.dob # Encrypt
                block['ssn'] = self.ssn # Encrypt
                block['votes'] = votes
                block_chain.append(block)
                new_hash = hash(block_chain)
                hashes.append(new_hash)
                return (block_chain, hashes)