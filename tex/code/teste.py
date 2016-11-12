from collections import Counter
from csv import DictReader

from pprint import pprint


def tabulate_business_types():
    '''
    Read the Licenses.csv file and try yo count the different kinds of businesses in Chicago.
    Print them out and
    '''
    count = Counter()
    with open('Licenses.csv', 'r') as _file:
        csvfile = DictReader(_file)
        for row in csvfile:
            license_code = row['LICENSE CODE']
            description = row['LICENSE DESCRIPTION']
            count[license_code, description] += 1
    return count.most_common()


def read_daycares():
    daycares = []
    with open('Licenses.csv', 'r') as _file:
        csvfile = DictReader(_file)
        for row in csvfile:
            license_code = row['LICENSE CODE']
            if license_code == '1023':
                daycares.append(row)
    return daycares


def find_food_inpections(daycares):
    daycare_licenses = set()
    for daycare in daycares:
        daycare_licenses.add(daycare['LICENSE NUMBER'])
    with_licenses = set()
    with open('Food_Inspections.csv') as _file:
        csvfile = DictReader(_file)
        for row in csvfile:
            license_no = row['License #']
            if license_no in daycare_licenses:
                with_licenses.add(license_no)
    return with_licenses


def find_food_inpections_in_2014(daycares):
    daycare_licenses = set()
    for daycare in daycares:
        daycare_licenses.add(daycare['LICENSE NUMBER'])
    with_licenses = set()
    with open('Food_Inspections.csv') as _file:
        csvfile = DictReader(_file)
        for row in csvfile:
            license_no = row['License #']
            inspection_date = row['Inspection Date']
            if license_no in daycare_licenses and '2014' in inspection_date:
                with_licenses.add(license_no)
    return with_licenses


def find_repeat_inpections_in_2014(daycares):
    daycare_licenses = set()
    for daycare in daycares:
        daycare_licenses.add(daycare['LICENSE NUMBER'])
    with_licenses = set()
    with open('Food_Inspections.csv') as _file:
        csvfile = DictReader(_file)
        for row in csvfile:
            license_no = row['License #']
            inspection_date = row['Inspection Date']
            if license_no in daycare_licenses and '2014' in inspection_date:
                with_licenses.add(license_no)
    return with_licenses


if __name__ == '__main__':
    types = tabulate_business_types()
    # daycares = read_daycares()
    # with_kitchens = find_food_inpections(daycares)
    # inspected_in_2014 = find_food_inpections_in_2014(daycares)
    # print(len(inspected_in_2014))
