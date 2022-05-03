from copy import deepcopy
from helper_functions import *
from cryptography.fernet import Fernet
import rsa
import matplotlib.pyplot as plt
import numpy as np

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
        self.publicKey, self.privateKey = rsa.newkeys(512)
        
        
    def get_pub_key(self):
        '''
            Public Key is available to everyone
        '''
        return self.publicKey
    
    
    def add_voter(self, voter):
        '''
            Process of adding/verifying voter with central authority
        '''
        dec_ssn = rsa.decrypt(voter['ssn'], self.privateKey).decode()
        if dec_ssn in self.voters:
            return False
        else:
            self.voters[dec_ssn] = voter
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
        
        
    def get_winner(self):
        '''
            Get the winner from the borda protocol and produce visualizations
        '''
        totalVotes = []
        print("\n\n")
        print("Getting the Winner")
        print("------------------")
        for item in self.blockchain:
            totalVotes.append(item["votes"])

        # Print votes from each voter
        for i in range(3):
            print(f"Voter {i+1}'s votes: {totalVotes[i]}")

        # Get value of votes from each voter
        votesWorthTotal = [0,0,0,0,0]
        votesWorth = []

        for votes in totalVotes:
            vw = [0,0,0,0,0]
            for i in range(5):
                if i == 0:
                    if votes[i] == 'a':
                        vw[0] = 5
                    elif votes[i] == 'b':
                        vw[1] = 5
                    elif votes[i] == 'c':
                        vw[2] = 5
                    elif votes[i] == 'd':
                        vw[3] = 5
                    elif votes[i] == 'e':
                        vw[4] = 5
                elif i == 1:
                    if votes[i] == 'a':
                        vw[0] = 4
                    elif votes[i] == 'b':
                        vw[1] = 4
                    elif votes[i] == 'c':
                        vw[2] = 4
                    elif votes[i] == 'd':
                        vw[3] = 4
                    elif votes[i] == 'e':
                        vw[4] = 4
                elif i == 2:
                    if votes[i] == 'a':
                        vw[0] = 3
                    elif votes[i] == 'b':
                        vw[1] = 3
                    elif votes[i] == 'c':
                        vw[2] = 3
                    elif votes[i] == 'd':
                        vw[3] = 3
                    elif votes[i] == 'e':
                        vw[4] = 3
                elif i == 3:
                    if votes[i] == 'a':
                        vw[0] = 2
                    elif votes[i] == 'b':
                        vw[1] = 2
                    elif votes[i] == 'c':
                        vw[2] = 2
                    elif votes[i] == 'd':
                        vw[3] = 2
                    elif votes[i] == 'e':
                        vw[4] = 2
                elif i == 4:
                    if votes[i] == 'a':
                        vw[0] = 1
                    elif votes[i] == 'b':
                        vw[1] = 1
                    elif votes[i] == 'c':
                        vw[2] = 1
                    elif votes[i] == 'd':
                        vw[3] = 1
                    elif votes[i] == 'e':
                        vw[4] = 1
            votesWorth.append(vw)

        print("\nWorths for Each Voter's votes:")
        print("------------------------------\n")
        print("          a  b  c  d  e ")
        print("         ---------------")
        for j in range(3):
            for i in range(5):
                votesWorthTotal[i] += votesWorth[j][i]
            print(f'Voter {j+1}: {votesWorth[j]}')


        # Get final Candidates' worths
        print()
        print(f'TOTAL:  {votesWorthTotal}')

        # Get winner
        max_value = max(votesWorthTotal)
        max_index = votesWorthTotal.index(max_value)

        if max_index == 0:
            winner = 'a'
        elif max_index == 1:
            winner = 'b'
        elif max_index == 2:
            winner = 'c'
        elif max_index == 3:
            winner = 'd'
        elif max_index == 4:
            winner = 'e'

        print('\n\n***********************')
        print(f' Winner is Candidate {winner}')
        print('***********************')

        # First Plot
        # ------------------------------------------
        # set width of bar
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        
        # Set position of bar on X axis
        br1 = np.arange(len(votesWorth[0]))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        
        # Make the plot
        plt.bar(br1, votesWorth[0], color ='r', width = barWidth,
                edgecolor ='grey', label ='Voter 1')
        plt.bar(br2, votesWorth[1], color ='g', width = barWidth,
                edgecolor ='grey', label ='Voter 2')
        plt.bar(br3, votesWorth[2], color ='b', width = barWidth,
                edgecolor ='grey', label ='Voter 3')

        # Adding Xticks
        plt.xlabel('Candidates', fontweight ='bold', fontsize = 15)
        plt.ylabel('Borda Score Assigned', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(votesWorth[0]))],
                ['a', 'b', 'c', 'd', 'e'])

        # plt.ylim([0.7, 0.92])
        plt.title('Borda Voting Values of 3 Voters on 5 Candidates', fontweight ='bold', fontsize = 20)
        
        plt.legend()
        # plt.savefig('indVotes.png')
        plt.show()

        # Second Plot 
        # create data
        x = ['a', 'b', 'c', 'd', 'e']

        y = [votesWorth[0][i] + votesWorth[1][i] for i in range(len(votesWorth[0]))]
        # plot bars in stack manner
        plt.bar(x, votesWorth[0], color='r')
        plt.bar(x, votesWorth[1], bottom=votesWorth[0], color='g')
        plt.bar(x, votesWorth[2], bottom=y, color='b')
        plt.xlabel("Candidates")
        plt.ylabel("Total Borda Score")
        plt.legend(["Voter 1", "Voter 2", "Voter 3"])
        plt.title("Total Borda Scores for each Candidate")
        # plt.savefig('totVotesBar.png')
        plt.show()

        # Third Plot
        y = np.array(votesWorthTotal)
        mylabels = ["a", "b", "c", "d", "e"]
        if max_index == 0:
            myexplode = [0.2, 0, 0, 0, 0]
        if max_index == 1:
            myexplode = [0, 0.2, 0, 0, 0]
        if max_index == 2:
            myexplode = [0, 0, 0.2, 0, 0]
        if max_index == 3:
            myexplode = [0, 0, 0, 0.2, 0]
        if max_index == 4:
            myexplode = [0, 0, 0, 0, 0.2]

        plt.title("Total Borda Scores for each Candidate")
        plt.pie(y, labels = mylabels, explode = myexplode)
        # plt.savefig('totVotesPie.png')
        plt.show() 

        
    
