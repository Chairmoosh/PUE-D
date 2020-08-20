#STEP1: Provides a list-of-lists of the permutations of S1 SF/BD strategies called 'Strategies'.  
#Higher lists include members for each S1 Strategy permutation. 
#Suborfinate lists have the SF:BD decision of S1 at each turn, with 1=SF, and  0=BD. 
#Eg for a three-turn process; Strategies = ((001), (010), (011), (100) ....)
Turns = 10 #Adjust to change number of turns
import itertools
Strategies = [list(i) for i in itertools.product([0, 1], repeat=Turns)]
#Print Strategies one by one
#for SF in Strategies:
#    print(SF)
#STEP2: Uses 'Strategies' to create a list-of-lists, called 'Probability_of_S2_Refuse'. 
#Higher lists include members for each S1 strategy permutation.  
#Sub-lists have members representing the probability of S2 refusing at each turn.
#Strategy is the member of 'Strategies' that is being be considered by the function.
def Payoff_Calculator (Strategy,Strategies):
    Probability_of_S2_Refuse=[]
    def Probability_of_S2_Refuse_Generator(Strategy):
        stepper = 0
        if (Strategy[stepper] == 0):
            Probability_of_S2_Refuse.append(0.90)
        else:
            Probability_of_S2_Refuse.append(0.50)
        def next_step(Strategy,stepper):
            n = Probability_of_S2_Refuse[stepper] 
            stepper=stepper+1
            if (n == 0.1):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.25)
                else:
                    Probability_of_S2_Refuse.append(0.1)
            elif (n == 0.25):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.5)
                else: 
                    Probability_of_S2_Refuse.append(0.1)
            elif (n == 0.5):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.75)
                else: 
                    Probability_of_S2_Refuse.append(0.25)
            elif (n == 0.75):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.9)
                else: 
                    Probability_of_S2_Refuse.append(0.5)
            elif (n == 0.9):
                if (Strategy[stepper]==1):
                    Probability_of_S2_Refuse.append(0.75)
                else:
                    Probability_of_S2_Refuse.append(0.9)
            if (stepper < (Turns-1)):
                next_step(Strategy,stepper)
        if (stepper == 0):
            next_step(Strategy,stepper)
    Probability_of_S2_Refuse_Generator(Strategy)
    #STEP3: Effect (E) Cost Calculation
    Probability_of_Effect=[]
    Probability_of_Effect.append(Probability_of_S2_Refuse[0])
    n=1
    def Probability_of_Effect_add(Probability_of_S2_Refuse,n):
        if (n<Turns-1):
            Probability_of_Effect.append(Probability_of_S2_Refuse[n]*Probability_of_Effect[n-1])
            n=n+1
            Probability_of_Effect_add(Probability_of_S2_Refuse,n)
    if (n == 1):
        Probability_of_Effect_add(Probability_of_S2_Refuse,n)
    E = sum (Probability_of_Effect)
    #STEP4: Lamda Cost Calculation
    List_Lamda=[]
    if (Strategy[0] == 1):
        List_Lamda.append(1)
    else:
        List_Lamda.append(0)
    for x in range(1,(Turns)):
        if (Strategy[x]==1):
            List_Lamda.append(Probability_of_Effect[x-1])
        else:
            List_Lamda.append(0)
    Lamda = sum (List_Lamda)
    print(Lamda) #Output
for Strategy in Strategies:
    Payoff_Calculator(Strategy,Strategies)

