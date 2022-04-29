
def get_voter_info(voter):
    # Get Voter Info
    # ---------------------------------------------------------------------------
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

    return firstName, lastName, dateOfBirth, social


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

    # Get Voter 1 Info
    firstName1, lastName1, dateOfBirth1, social1 = get_voter_info(1)

    # Verify Voter 1

    # Get Voter 1 Votes
    votes1 = get_votes()

    # Get Voter 2 Info
    firstName2, lastName2, dateOfBirth2, social2 = get_voter_info(2)

    # Verify Voter 2

    # Get Voter 2 Votes
    votes2 = get_votes()

    # Get Voter 3 Info
    firstName3, lastName3, dateOfBirth3, social3 = get_voter_info(3)

    # Verify Voter 3

    # Get Voter 3 Votes
    votes3 = get_votes()

