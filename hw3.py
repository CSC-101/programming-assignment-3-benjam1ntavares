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





