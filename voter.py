from helper_functions import *
import rsa
from cryptography.fernet import Fernet

class Voter:
    
    def __init__(self, fn, ln, dob, ssn, ca_pub_key):
        '''
            Constructor
        '''
        self.fn = fn
        self.ln = ln
        self.dob = dob
        self.ssn = ssn
        self.ca_pub_key = ca_pub_key
        
        # generate a key for encryption and decryption
        # You can use fernet to generate
        # the key or use random key generator
        # here I'm using fernet to generate key        
        key = Fernet.generate_key()
        
        # Instance the Fernet class with the key        
        self.key = Fernet(key)
        
        self.enc_ssn = rsa.encrypt(self.ssn.encode(), self.ca_pub_key)
        
        
    def get_info(self):
        '''
            Returns voter info
        '''        
        # Usually the central authority would get the symmetric key from a trusted 3rd party so no 
        # chance of interception in transfer of this message        
        return {'fn':self.fn, 'ln':self.ln, 'dob':self.dob, 'ssn':self.enc_ssn}
        
        
    def add_block(self, votes, block_chain=None, hashes=None):
        '''
        '''
        block = {}
        # Create 1st block in chain
        if not block_chain and not hashes:
            hashes = []
            block_chain = []
            block['fn'] = rsa.encrypt(self.fn.encode(), self.ca_pub_key) # Encrypt
            block['ln'] = rsa.encrypt(self.ln.encode(), self.ca_pub_key) # Encrypt
            block['dob'] = rsa.encrypt(self.dob.encode(), self.ca_pub_key) # Encrypt
            block['ssn'] = rsa.encrypt(self.ssn.encode(), self.ca_pub_key) # Encrypt
            block['votes'] = votes
            block_chain.append(block)
            block_hash = compute_hash(block_chain)
            hashes.append(block_hash)
            return (block_chain, hashes)
        # Create             
        else:
            print('Chain is not empty')
            isVerified = verify_chain(block_chain, hashes)
            if not isVerified:
                return None
            else:
                block['fn'] = rsa.encrypt(self.fn.encode(), self.ca_pub_key) # Encrypt
                block['ln'] = rsa.encrypt(self.ln.encode(), self.ca_pub_key) # Encrypt
                block['dob'] = rsa.encrypt(self.dob.encode(), self.ca_pub_key) # Encrypt
                block['ssn'] = rsa.encrypt(self.ssn.encode(), self.ca_pub_key) # Encrypt
                block['votes'] = votes
                block_chain.append(block)
                new_hash = compute_hash(block_chain)
                hashes.append(new_hash)
                return (block_chain, hashes)