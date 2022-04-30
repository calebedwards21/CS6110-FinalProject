from central_authority import CentralAuthority
from voter import Voter

def get_voter_info(voter):
    # Get Voter Info
    print(f'\nWelcome Voter {voter}, Please enter the following info to vote...')
    print("---------------------------------------------------------")

    # Get first name
    inputFlag = True
    while inputFlag:
        firstName = input("First Name: ")
        firstName = firstName.lower()
        if not firstName.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    # Get last name
    inputFlag = True
    while inputFlag:
        lastName = input("Last Name: ")
        lastName = lastName.lower()
        if not lastName.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    # Get date of birth
    inputFlag = True
    while inputFlag:
        dateOfBirth = input("Date of Birth (MMDDYYYY): ")
        if len(dateOfBirth) != 8 or not dateOfBirth.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    # Get social security number
    inputFlag = True
    while inputFlag:
        social = input("Social Security Number (No Dashes or Spaces): ")
        if len(social) != 9 or not social.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False
    print('\n')

    return (firstName, lastName, dateOfBirth, social)


def get_votes():
    votes = []
    candidates = ['a', 'b', 'c', 'd', 'e']
    print("Candidates: A, B, C, D, E")
    print("Rank the candidates from favorite (1) to least favorite (5)")
    print("-----------------------------------------------------------")

    # Get 5 votes
    for i in range(5):
        voteFlag = True
        while voteFlag:
            vote = (input(f'({i+1}) = '))
            vote = vote.lower()
            if vote in candidates:
                votes.append(vote)
                candidates.remove(vote)
                voteFlag = False
            else:
                print("** Invalid Input. Try Again **")

    return votes

if __name__ == "__main__":
    
    central_authority = CentralAuthority()
    ca_pub_key = central_authority.get_pub_key()

    # Voter 1
    v1 = get_voter_info(1)
    voter1 = Voter(v1[0], v1[1], v1[2], v1[3], ca_pub_key)
    
    if central_authority.add_voter(voter1.get_info()):
        votes1 = get_votes()
        block_chain1, hashes1 = central_authority.get_blockchain()
        print(block_chain1)
        print(hashes1)
        (block1, hash1) = voter1.add_block(votes1, block_chain1, hashes1)
        print(block1)
        print(hash1)
        if not block1:
            raise Exception('Current BlockChain is Invalid')
        if not central_authority.set_blockchain(block1, hash1):
            raise Exception('Cannot Add New Block')
    print(central_authority.get_blockchain())
        
    

    # Voter 2
    v2 = get_voter_info(2)
    voter2 = Voter(v2[0], v2[1], v2[2], v2[3], ca_pub_key)
    if central_authority.add_voter(voter2.get_info()):
        votes2 = get_votes()
        block_chain2, hashes2 = central_authority.get_blockchain()
        print(block_chain2)
        print(hashes2)
        (block2, hash2) = voter2.add_block(votes2, block_chain2, hashes2)
        if not block2:
            raise Exception('Current BlockChain is Invalid')
        if not central_authority.set_blockchain(block2, hash2):
            raise Exception('Cannot Add New Block')
    print(central_authority.get_blockchain())    

    # Voter 3
    v3 = get_voter_info(3)
    voter3 = Voter(v3[0], v3[1], v3[2], v3[3], ca_pub_key)
    if central_authority.add_voter(voter3.get_info()):
        votes3 = get_votes()
        block_chain3, hashes3 = central_authority.get_blockchain()
        (block3, hash3) = voter3.add_block(votes3, block_chain3, hashes3)
        if not block3:
            raise Exception('Current BlockChain is Invalid')
        if not central_authority.set_blockchain(block3, hash3):
            raise Exception('Cannot Add New Block')
    print(central_authority.get_blockchain())
    
    
    # Central Authority produce winner
    # winner = central_authority.get_winner()
    # Encrypt and Decrypt
