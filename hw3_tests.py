import data
import build_data
import unittest
import hw3


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]


# i made this a list so it could be processed by the functions that we are using
slo_data = [data.CountyDemographics(
    # age
    {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
    # county
    'San Luis Obispo County',
    # education
    {"Bachelor's Degree or Higher": 31.5,
               'High School or Higher': 89.6},
    # ethnicities
    {'American Indian and Alaska Native Alone': 1.4,
                 'Asian Alone': 3.8,
                 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4,
                 'White Alone': 89.0,
                 'White Alone, not Hispanic or Latino': 69.5},
    # income
    {'Median Household Income': 58697,
            'Per Capita Income': 29954,
            'Persons Below Poverty Level': 14.3},
    # population
    {'2010 Population': 269637,
                '2014 Population': 279083,
                'Population Percent Change': 3.5,
                'Population per Square Mile': 81.7},
    # state
    'CA'
)]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total(self):
        input_demographics = full_data
        expected = 318857056
        actual = hw3.population_total(input_demographics)
        self.assertEqual(expected, actual)

    def test_population_total_reduced(self):
        input_demographics = reduced_data
        expected = 655813
        actual = hw3.population_total(input_demographics)
        self.assertEqual(expected, actual)

    # Part 2
    # test filter_by_state

    # to test filter by state, we are told that there are 58 counties in the full set of data that should be in CA,
    # so, to verify that the function works, we will be checking the length of
    def test_filter_by_state(self):
        input_demographics = full_data
        expected = 58
        actual = len(hw3.filter_by_state(input_demographics, 'CA'))
        self.assertEqual(expected, actual)


    # we are also told in the description that the counties would have a total population of 38802500 so we will use the
    # population total function to find the total population of the counties returned by this function.
    def test_filter_by_state2_population(self):
        input_demographics = full_data
        expected = 38802500
        actual = hw3.population_total(hw3.filter_by_state(input_demographics, 'CA'))
        self.assertEqual(expected, actual)

    # Part 3


    # test population_by_education
    # since we wer provided that 87911.145 people in slo county have a bachelors degree or higher we will use this
    # information as a testing point.

    def test_population_by_education(self):
        input_demographics = slo_data
        expected = 87911.145 # number based off of data, can not have .145 people
        actual = hw3.population_by_education(input_demographics, 'Bachelor\'s Degree or Higher')
        self.assertEqual(expected, actual)

    # test case when the input education is not a valid level of education
    def test_population_by_education2(self):
        input_demographics = slo_data
        expected = 0
        actual = hw3.population_by_education(input_demographics, '1st Degree Burn')
        self.assertEqual(expected, actual)


    # test population_by_ethnicity using slo_data
    # ethnicity is in ethnicities
    def test_population_by_ethnicity(self):
        input_demographics = slo_data
        expected = 10605.154
        actual = hw3.population_by_ethnicity(input_demographics, 'Asian Alone')
        self.assertEqual(expected, actual)
    # ethnicity not in ethnicities
    def test_population_by_ethnicity2(self):
        input_demographics = slo_data
        expected = 0
        actual = hw3.population_by_ethnicity(input_demographics, 'Hippo')
        self.assertEqual(expected, actual)

    # test population_below_poverty_level
    def test_population_below_poverty_level1(self):
        input_demographics = slo_data
        expected = 39908.869
        actual = hw3.population_below_poverty_level(input_demographics)
        self.assertAlmostEqual(expected, actual)

    # test with reduced data
    def test_population_below_poverty_level(self):
        input_demographics = reduced_data
        expected = 107711.714
        actual = hw3.population_below_poverty_level(input_demographics)
        self.assertAlmostEqual(expected, actual)


    # Part 4
    # test percent_by_education
    def test_percent_by_education(self):
        input_demographics = slo_data
        education = "Bachelor's Degree or Higher"
        expected = 31.5
        actual = hw3.percent_by_education(input_demographics,education)
        self.assertEqual(expected, actual)

    def test_percent_by_education2(self):
        input_demographics = reduced_data
        education = "Bachelor's Degree or Higher"
        expected = 20.9
        actual = hw3.percent_by_education(input_demographics,education)
        self.assertAlmostEqual(expected, actual)

    def test_percent_by_education3(self):
        input_demographics = full_data
        education = "Bachelor's Degree or Higher"
        expected = 20.9
        actual = hw3.percent_by_education(input_demographics,education)
        self.assertAlmostEqual(expected, actual)



    # test percent_by_ethnicity

    def test_percent_by_ethnicity(self):
        input_demographics = slo_data
        ethnicity = 'Asian Alone'
        expected = 3.8
        actual = hw3.percent_by_ethnicity(input_demographics,ethnicity)
        self.assertEqual(expected, actual)

    def test_percent_by_ethnicity2(self):
        input_demographics = full_data
        ethnicity = 'Asian Alone'
        expected = 1.1
        actual = hw3.percent_by_ethnicity(input_demographics,ethnicity)
        self.assertAlmostEqual(expected, actual)


    # test percent_below_poverty_level
    def test_percent_below_poverty_level(self):
        input_demographics = slo_data
        expected = 14.3
        actual = hw3.percent_below_poverty_level(input_demographics)
        self.assertEqual(expected, actual)

    def test_percent_below_poverty_level2(self):
        input_demographics = reduced_data
        expected = 16.42
        actual = hw3.percent_below_poverty_level(input_demographics)
        self.assertAlmostEqual(expected, actual, places=2)

    # Part 5

    # test education_greater_than
    def test_education_greater_than(self):
        counties = slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 7
        expected = ['San Luis Obispo County']
        actual = hw3.county_list_names(hw3.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    def test_education_greater_than2(self):
        counties = slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 50
        expected = []
        actual = hw3.county_list_names(hw3.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    # test education_less_than
    def test_education_less_than(self):
        counties = slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 50
        expected = ['San Luis Obispo County']
        actual = hw3.county_list_names(hw3.education_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    def test_education_less_than2(self):
        counties = slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 7
        expected = []
        actual = hw3.county_list_names(hw3.education_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    # test education greater than with a full set of data, since both are essentially the same function, no need to do
    # this twice

    # all reduced data counties should be in this range
    def test_education_greater_than3(self):
        counties = reduced_data
        key = "Bachelor's Degree or Higher"
        threshold = 9
        expected = ['Autauga County','Crawford County', 'San Luis Obispo County','Yolo County','Butte County',
                    'Pettis County','Weston County']
        actual = hw3.county_list_names(hw3.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    # some reduced data counties will not be in this range

    def test_education_greater_than4(self):
        counties = reduced_data
        key = "Bachelor's Degree or Higher"
        threshold = 17
        expected = ['Autauga County','San Luis Obispo County','Yolo County', 'Butte County', 'Weston County']
        actual = hw3.county_list_names(hw3.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        counties = slo_data
        key = "Asian Alone"
        threshold = 2.1
        expected = ['San Luis Obispo County']
        actual = hw3.county_list_names(hw3.ethnicity_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    def test_ethnicity_greater_than2(self):
        counties = slo_data
        key = "Asian Alone"
        threshold = 4
        expected = []
        actual = hw3.county_list_names(hw3.ethnicity_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    # test ethnicity_less_than
    def test_ethnicity_less_than(self):
        counties = slo_data
        key = "Asian Alone"
        threshold = 4
        expected = ['San Luis Obispo County']
        actual = hw3.county_list_names(hw3.ethnicity_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    def test_ethnicity_less_than2(self):
        counties = slo_data
        key = 'Asian Alone'
        threshold = 1.1
        expected = []
        actual = hw3.county_list_names(hw3.ethnicity_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)



    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        counties = slo_data
        threshold = 13
        expected = ['San Luis Obispo County']
        actual = hw3.county_list_names(hw3.below_poverty_level_greater_than(counties, threshold))
        self.assertEqual(expected, actual)

    def test_below_poverty_level_greater_than2(self):
        counties = slo_data
        threshold = 20
        expected =[]
        actual = hw3.county_list_names(hw3.below_poverty_level_greater_than(counties, threshold))
        self.assertEqual(expected, actual)

    # test below_poverty_level_less_than

    def test_below_poverty_level_less_than(self):
        counties = slo_data
        threshold = 13
        expected = []
        actual = hw3.county_list_names(hw3.below_poverty_level_less_than(counties, threshold))
        self.assertEqual(expected, actual)

    def test_below_poverty_level_less_than2(self):
        counties = slo_data
        threshold = 20
        expected =['San Luis Obispo County']
        actual = hw3.county_list_names(hw3.below_poverty_level_less_than(counties, threshold))
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
