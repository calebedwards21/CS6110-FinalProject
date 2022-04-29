from copy import deepcopy
from helper_functions import *

class CentralAuthority:
    
    voters = {}
    blockchain = []
    hashes = []
    
    def __init__(self, voters={}, blockchain=[], hashes=[]):
        '''
            Constructor
        '''
        self.voters = voters
        self.blockchain = blockchain
        self.hashes = hashes
    
    
    def add_voter(self, voter):
        '''
            Process of adding/verifying voter with central authority
        '''
        if voter.ssn in self.voters:
            return False
        else:
            self.voters[voter.ssn] = {voter}
            return True
        
    
    def get_blockchain(self):
        '''
            Return a copy of the blockchain and hashes
        '''
        return deepcopy(self.blockchain), deepcopy(self.hashes)
    
    
    def set_blockchain(self, new_blockchain, new_hashes):
        '''
            Set the blockchain, hashes to the new blockchain, hashes
        '''
        if verify_chain(new_blockchain, new_hashes):
            self.blockchain = new_blockchain
            self.hashes = new_hashes
            return True
        else:
            return False
    
    
