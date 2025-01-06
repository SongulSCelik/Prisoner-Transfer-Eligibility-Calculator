#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''This program calculates when a prisoner becomes eligible for transfer to an open prison
based on the type of crime they committed and the sentence length.'''


# In[16]:



firstDegreeCrimes = [
    "murder",
    "terrorism",
    "rape",
    "kidnapping",
    "drug trafficking",
    "organized crime",
    "aggravated robbery",
    "assault leading to death"
]

secondDegreeCrimes = [
    "petty theft",
    "vandalism",
    "fraud",
    "bribery",
    "negligence",
    "involuntary manslaughter",
    "drug possession",
    "battery"
]

# Function to calculate eligibility for transfer to open prison
def transfertoOpenPrisonFirstDegree(yearSentencedbyJudge, crimes='firstdegree'):
    return float(yearSentencedbyJudge) * 0.80

def transfertoOpenPrisonSecondDegree(yearSentencedbyJudge, crimes='seconddegree'):
    return float(yearSentencedbyJudge) * 0.60

# Main function
def eligibilityAndTransferTimeOpenPrison():
    
    print("This program determines when a prisoner becomes eligible for transfer to an open prison or lower-security facility, where they may be granted limited leave privileges to go outside and return within set time limits.")
    print("This calculation applies to first-time offenders. If the offender has served a prior sentence for a different crime, the eligibility for transfer changes, and a different calculation is required.")
    print('\nYou will need to answer the following questions.')   
    print('\n\t\t\t\tTypes of Crimes')
    print(f'\n\tFirst Degree Crimes:{firstDegreeCrimes}')
    print(f'\n\tSecond Degree Crimes:{secondDegreeCrimes}')
    print("\nCommitting a crime during incarceration affects transfer eligibility, but not all behaviors do.")
    print("Consequences depend on the nature and severity of the behavior. This program does not calculate these factors and operates on an ex ante basis.")

    
    
    
    # User input1: Age
    while True:
        
        ageInput=input('\nPlease enter age between 18-90:')
        
        if ageInput.isdigit():
            
            ageInput=int(ageInput)
        
            if ageInput<18 or ageInput>90 :
                print('Inquiries for individuals under 18 should be handled using  \'Juvinele Transfer Calculation\' ')
                print('This programme is only for adults between 18-90.')
                return # exit the programme
            else:
                print('we can contuine , it is a valid input for age.')  
                
            break
                
        else:
            
            print('Please enter a valid number between 18-90:')
    
    # User input2: Years Sentenced
    yearsSentenced = False  # This remains the flag for the loop
    
    while not yearsSentenced:
        yearsInput = input('How many years was the sentence decided by the judge? Please enter a number: ')
        
        # Check if input is a valid number (integer or float)
        if yearsInput.replace('.', '', 1).isdigit() and float(yearsInput) > 0:
            print(f'You entered {yearsInput} as the total time decided by the judge.')
            yearsSentenced = float(yearsInput)  # Convert to float for later use
        else:
            print(f'You entered {yearsInput}, an invalid input. Please enter a valid number.')
    
    # User input3: Crime Name
#####
    while True:
        crimeNameInput= input('What is the name of crime ?').strip().lower()
    
        if crimeNameInput in firstDegreeCrimes:
            #print('The programe is going to calculate required time according to custom function1')
            break
        elif crimeNameInput in secondDegreeCrimes:
            #print('The programe is going to calculate required time according to custom function2')
            break
          
        else:
        
         print('Unidentified crime name. Please try again , refer to the lists above.')
    
    #After getting valid inputs, now we can calculate the required time to stay in closed Prison for the transfer eligiblity 
    
    # First Degree Crimes
    if crimeNameInput in firstDegreeCrimes:
        requiredTimeForClosedPrison = transfertoOpenPrisonFirstDegree(yearsSentenced, crimes='firstdegree')
        timeWillBeSpentInOpenPrison = yearsSentenced - requiredTimeForClosedPrison
        print("\nFor %s, the prisoner must stay in the closed prison facility for %.1f years.\nThen, they can be transferred to the open prison facility for %.1f years, assuming all other factors remain constant." % (crimeNameInput, requiredTimeForClosedPrison, timeWillBeSpentInOpenPrison))
    # Second Degree Crimes
    elif crimeNameInput in secondDegreeCrimes:
        requiredTimeForClosedPrison = transfertoOpenPrisonSecondDegree(yearsSentenced, crimes='seconddegree')
        timeWillBeSpentInOpenPrison = yearsSentenced - requiredTimeForClosedPrison
        print("\nFor %s, the prisoner must stay in the closed prison facility for %.1f years.\nThen, they can be transferred to the open prison facility for %.1f years, assuming all other factors remain constant." % (crimeNameInput, requiredTimeForClosedPrison, timeWillBeSpentInOpenPrison))
        
   ###  adding bad behaviour input for further check.
    
    
    while True:
        
        maxWarning=3
        warningCount=0
        
        warningCount=input('How many times the offender has been given warning? :')
        
        if warningCount.isdigit():
            warningCount=int(warningCount)
            if warningCount<=maxWarning:
                print('Still eligible for transfer.')
                break
            else:
                print('Not eligible for transfer. Excessive warnings  ')
                break
                
    
        else:
           
            print('Not eligible for transfer. Excessive warnings  ')
            

# Test the program
eligibilityAndTransferTimeOpenPrison()


# In[17]:


eligibilityAndTransferTimeOpenPrison()


# In[18]:


eligibilityAndTransferTimeOpenPrison()


# In[ ]:





# In[ ]:





# In[ ]:




