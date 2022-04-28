

if __name__ == "__main__":

    # Get Voter 1 Info
    # ---------------------------------------------------------------------------
    print("\nWelcome Voter 1, Please enter the following info to vote...")
    print("---------------------------------------------------------")

    inputFlag = True
    while inputFlag:
        firstName1 = input("First Name: ")
        firstName1 = firstName1.lower()
        if not firstName1.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        lastName1 = input("Last Name: ")
        lastName1 = lastName1.lower()
        if not lastName1.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        dateOfBirth1 = input("Date of Birth (MMDDYYYY): ")
        if len(dateOfBirth1) != 8 or not dateOfBirth1.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        social1 = input("Social Security Number (No Dashes or Spaces): ")
        if len(social1) != 9 or not social1.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False
    print('\n')
    
    # ---------------------------------------------------------------------------


    # Verify User
    # ---------------------------------------------------------------------------
    
    # ---------------------------------------------------------------------------


    # Get Voter 1 Votes
    # ---------------------------------------------------------------------------
    votes1 = []
    candidates = ['a', 'b', 'c', 'd', 'e']
    print("Candidates: A, B, C, D, E")
    print("Rank the candidates from favorite (1) to least favorite (5)")
    print("-----------------------------------------------------------")

    # 1st Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(1) = "))
        vote = vote.lower()
        if vote in candidates:
            votes1.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 2nd Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(2) = "))
        vote = vote.lower()
        if vote in candidates:
            votes1.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 3rd Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(3) = "))
        vote = vote.lower()
        if vote in candidates:
            votes1.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 4th Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(4) = "))
        vote = vote.lower()
        if vote in candidates:
            votes1.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 5th Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(5) = "))
        vote = vote.lower()
        if vote in candidates:
            votes1.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    print(votes1)
    # ---------------------------------------------------------------------------


    # Get Voter 2 Info
    # ---------------------------------------------------------------------------
    print("\nWelcome Voter 2, Please enter the following info to vote...")
    print("---------------------------------------------------------")

    inputFlag = True
    while inputFlag:
        firstName2 = input("First Name: ")
        firstName2 = firstName2.lower()
        if not firstName2.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        lastName2 = input("Last Name: ")
        lastName2 = lastName2.lower()
        if not lastName2.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        dateOfBirth2 = input("Date of Birth (MMDDYYYY): ")
        if len(dateOfBirth2) != 8 or not dateOfBirth2.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        social2 = input("Social Security Number (No Dashes or Spaces): ")
        if len(social2) != 9 or not social2.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False
    print('\n')
    
    # ---------------------------------------------------------------------------


    # Verify User
    # ---------------------------------------------------------------------------
    
    # ---------------------------------------------------------------------------


    # Get Voter 2 Votes
    # ---------------------------------------------------------------------------
    votes2 = []
    candidates = ['a', 'b', 'c', 'd', 'e']
    print("Candidates: A, B, C, D, E")
    print("Rank the candidates from favorite (1) to least favorite (5)")
    print("-----------------------------------------------------------")

    # 1st Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(1) = "))
        vote = vote.lower()
        if vote in candidates:
            votes2.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 2nd Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(2) = "))
        vote = vote.lower()
        if vote in candidates:
            votes2.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 3rd Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(3) = "))
        vote = vote.lower()
        if vote in candidates:
            votes2.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 4th Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(4) = "))
        vote = vote.lower()
        if vote in candidates:
            votes2.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 5th Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(5) = "))
        vote = vote.lower()
        if vote in candidates:
            votes2.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    print(votes2)
    # ---------------------------------------------------------------------------


    # Get Voter 3 Info
    # ---------------------------------------------------------------------------
    print("\nWelcome Voter 3, Please enter the following info to vote...")
    print("---------------------------------------------------------")

    inputFlag = True
    while inputFlag:
        firstName2 = input("First Name: ")
        firstName2 = firstName2.lower()
        if not firstName2.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        lastName2 = input("Last Name: ")
        lastName2 = lastName2.lower()
        if not lastName2.isalpha():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        dateOfBirth2 = input("Date of Birth (MMDDYYYY): ")
        if len(dateOfBirth2) != 8 or not dateOfBirth2.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False

    inputFlag = True
    while inputFlag:
        social2 = input("Social Security Number (No Dashes or Spaces): ")
        if len(social2) != 9 or not social2.isnumeric():
            print("** Invalid Input. Try Again... **")
        else:
            inputFlag = False
    print('\n')
    
    # ---------------------------------------------------------------------------


    # Verify User
    # ---------------------------------------------------------------------------
    
    # ---------------------------------------------------------------------------


    # Get Voter 3 Votes
    # ---------------------------------------------------------------------------
    votes3 = []
    candidates = ['a', 'b', 'c', 'd', 'e']
    print("Candidates: A, B, C, D, E")
    print("Rank the candidates from favorite (1) to least favorite (5)")
    print("-----------------------------------------------------------")

    # 1st Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(1) = "))
        vote = vote.lower()
        if vote in candidates:
            votes3.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 2nd Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(2) = "))
        vote = vote.lower()
        if vote in candidates:
            votes3.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 3rd Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(3) = "))
        vote = vote.lower()
        if vote in candidates:
            votes3.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 4th Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(4) = "))
        vote = vote.lower()
        if vote in candidates:
            votes3.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    # 5th Ranking
    voteFlag = True
    while voteFlag:
        vote = (input("(5) = "))
        vote = vote.lower()
        if vote in candidates:
            votes3.append(vote)
            candidates.remove(vote)
            voteFlag = False
        else:
            print("** Invalid Input. Try Again **")

    print(votes3)
    # ---------------------------------------------------------------------------

