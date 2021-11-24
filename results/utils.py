from datetime import time
from constants import SEXES


def is_junior_competitor(competitor={}):
    return int(competitor["age"]) <= 25


def is_senior_competitor(competitor={}):
    return 25 <= int(competitor["age"]) <= 40


def is_master_competitor(competitor={}):
    return 40 < int(competitor["age"])


def is_male_competitor(competitor={}):
    return competitor["sex"] == SEXES["MALE"]


def is_female_competitor(competitor={}):
    return competitor["sex"] == SEXES["FEMALE"]


def get_competitors_list_per_age_group(competitors=[]):
    juniors = []
    seniors = []
    masters = []

    for competitor in competitors:
        if(is_junior_competitor(competitor)):
            juniors.append(competitor)
        elif(is_senior_competitor(competitor)):
            seniors.append(competitor)
        elif(is_master_competitor(competitor)):
            masters.append(competitor)

    return juniors, seniors, masters


def get_competitors_per_sex(competitors=[]):
    mens = []
    womens = []

    for competitor in competitors:
        if(is_male_competitor(competitor)):
            mens.append(competitor)
        elif(is_female_competitor(competitor)):
            womens.append(competitor)

    return mens, womens


def get_winner(competitors=[]):
    return min(
        competitors,
        key=lambda c: time(
            int(c["hours"]), int(c["minutes"]), int(c["seconds"])
        )
    )
