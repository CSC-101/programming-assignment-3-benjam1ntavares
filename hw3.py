import build_data
import data
from data import CountyDemographics

# Part 1: population_total
########################################################################################################################
# input : list_county demographics
# output : int (total population of input demographics) in this case, for the total 2014 population

# in this case we use thin input of full_data, which is a list of CountyDemographics objects.
# to return the total population we will:
#   - iterate through each CountyDemographics object
#   - for each object, find its population, then use the get() method for dictionaries to acess the '2014 Population'
#   - append the population for each county to a list
#   - return a sum of all county populations in the list

def population_total(demographics: list[CountyDemographics]) -> int:
    county_populations = []
    for county in range(len(demographics)):
        county_populations.append(demographics[county].population.get('2014 Population'))
    return sum(county_populations)

# Part 2:  filter_by_state
########################################################################################################################
# input: demographics: list[CountyDemographics], state_ab: str
# output: list[CountyDemographics] (reduced or filtered)

# the filter_by_state function will take the input list of county demographics, and it will filter the data to only
# return the county demographics from a specific state specified by the state abbreviation i.e CA
def filter_by_state(demographics: list[CountyDemographics], state_ab: str) -> list[CountyDemographics]:
    filtered_demogrphics = []
    for county in demographics:
        if county.state == state_ab.upper():
            filtered_demogrphics.append(county)
    return filtered_demogrphics

# Part 3
########################################################################################################################
# population_by_education
########################################################################################################################
# input: demographics: list[CountyDemographics],str
# output: int (Population of people with a certain degree of education)

# the population by education function will take the input list of county demographics, and it will use the percentage
# of people with a certain degree of eduction, alongside the total population to calculate the population of people in a
# given county that have said level of education

# note that the percent educated value is the percentage out of every 100 people so we must divide this number by 100
# before we multiply  it by the total population

def population_by_education(counties: list[CountyDemographics], education_level: str) -> int:
    for county in counties:
        if f'{education_level}' in county.education:
            percent_educated = county.education.get(education_level)
            return (percent_educated * 10**-2) * population_total(counties)
        else:
            return 0


# population_by_ethnicity
########################################################################################################################
# inputs: list[CountyDemographics],str
# outputs: float

# similar functionality to population_by_education

def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> int:
    for county in counties:
        if f'{ethnicity}' in county.ethnicities:
            ethnicity_percentage = county.ethnicities.get(ethnicity)
            return (ethnicity_percentage * 10**-2) * population_total(counties)
        else:
            return 0


# population_below_poverty
########################################################################################################################
# inputs: list[CountyDemographics]
# outputs: int
# (1) iterate through each county (2)access the percentage of people below the poverty level (3) multiply 2014 population
# by percentage below poverty level. (4) add this number to accumulator (5) Return accumulated value

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    pop_below = 0
    for county in counties:
        percent_below = county.income.get('Persons Below Poverty Level')/100
        pop_below += percent_below * county.population.get('2014 Population')
    return pop_below








