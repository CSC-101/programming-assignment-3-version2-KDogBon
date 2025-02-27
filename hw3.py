import county_demographics
from data import CountyDemographics


#part 1
def population_total(lst:list[CountyDemographics]) ->int: #I need to get a list of county demographics and return a int
    totalPop = 0

    for x in lst: # i need to iteratate through the list of county
        totalPop += x.population["2014 Population"] #i need to make sure I only get the 2014 population
    return totalPop





#part 2
def filter_by_state(lst: list[CountyDemographics], word:str) -> list[CountyDemographics]: #I need to get a list of county demographics and a state, then return a list of that county demographics of that state
     finalList = []
     for x in lst:
         if x.state == word: #check to see if it is that state
             finalList.append(x) #add that state

     return finalList







#part 3


def population_by_education(lst:list[CountyDemographics], word:str) -> float: #I need to get a list of county demographics and the education type, then return the total number of people in that have that education
    number = 0.0
    for x in lst:
       number += x.population["2014 Population"]*(x.education[word]/100) #calculate the total by taking the population and multiplying it by the percentage that are educated

    return number


def population_by_ethnicity(lst:list[CountyDemographics], word:str) -> float: #I need to get a list of county demographics and the ethnicity type, then return the total number of people in that have that ethnicity
    number = 0.0
    for x in lst:

        number += x.population["2014 Population"] * (x.ethnicities[word]/100) #calculate the total by taking the population and multiplying it by the percentage that are that ethnicity

    return number

def population_below_poverty_level(lst:list[CountyDemographics]) -> float: #I need to get a list of county demographics, then return the total number of people in that have that are below the poverty level
    number = 0.0
    for x in lst:

        number += x.population["2014 Population"] * (x.income["Persons Below Poverty Level"]/100) #calculate the total by taking the population and multiplying it by the percentage that are below the poverty level

    return number



#part 4

def percent_by_education(lst:list[CountyDemographics], word:str) -> float: #I need to get a list of county demographics and the education type, then return the percent  of people in that have that education compared to the total population
    educationNumber = population_by_education(lst, word) # i need to find the population of educated people
    populationNumber = population_total(lst) # I need to find the total population
    return (educationNumber/populationNumber)*100


def percent_by_ethnicity(lst:list[CountyDemographics], word:str) -> float: #I need to get a list of county demographics and the ethnicity type, then return the percent of people in that have that ethnicity compared to the total population
    ethnicityNumber = population_by_ethnicity(lst, word) # I need to find the population of people of that ethnicity
    populationNumber = population_total(lst) # I need to find the total population
    return (ethnicityNumber/populationNumber)*100

def percent_below_poverty_level(lst:list[CountyDemographics]) -> float: #I need to get a list of county demographics, then return the percent of people in that have that are below the poverty line compared to the total population
    belowPovertyLineNumber = population_below_poverty_level(lst) # I need to find the population of people below the poverty line
    populationNumber = population_total(lst) # I need to find the total population
    return (belowPovertyLineNumber/populationNumber)*100



#part 5

def education_greater_than(lst:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]: #I need to get a list of county demographics and the education type and a percentage value, then return an array of counties above that percentage
    finalList = []
    for x in lst:
        if percent_by_education([x], word) > percent: # ill need to check if a county is above the percentage
            finalList.append(x)
    return finalList


def education_less_than(lst:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]:
    finalList = []
    for x in lst:
        if percent_by_education([x], word) < percent: # ill need to write something similar to above but swap the sign
            finalList.append(x)
    return finalList


def ethnicity_greater_than(lst:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]: #I need to get a list of county demographics and the ethnicity type and a percentage value, then return an array of counties above that percentage
    finalList = []
    for x in lst:
        if percent_by_ethnicity([x], word) > percent: # ill need to check if a county is above the percentage
            finalList.append(x)
    return finalList



def ethnicity_less_than(lst:list[CountyDemographics], word:str, percent:float) -> list[CountyDemographics]:
    finalList = []
    for x in lst:
        if percent_by_ethnicity([x], word) < percent: # ill need to write something similar to above but swap the sign
            finalList.append(x)
    return finalList

def below_poverty_level_greater_than(lst:list[CountyDemographics], percent:float) -> list[CountyDemographics]: #I need to get a list of county demographics and percentage value, then return an array of counties above that percentage with respect to poverty level
    finalList = []
    for x in lst:
        if percent_below_poverty_level([x]) > percent: # ill need to check if a county is above the percentage
            finalList.append(x)
    return finalList


def below_poverty_level_less_than(lst:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    finalList = []
    for x in lst:
        if percent_below_poverty_level([x]) < percent: # ill need to write something similar to above but swap the sign
            finalList.append(x)
    return finalList
