from skcriteria import Data, MAX, MIN
from skcriteria.madm.closeness import TOPSIS


def decide(mtx, alternatives, weights):
    criteria_names = ['control of_corruption', 'political_stability', 'inflation rate', 'gdp_growth',
                      'ease_of_doing_business', 'unemployment_rate',
                      'individuals_using_the_internet']

    _criteria = [MAX, MAX, MIN, MAX, MAX, MIN, MAX]
    data = Data(mtx=mtx, criteria=_criteria, weights=weights,
                anames=alternatives,
                cnames=criteria_names)
    topsis = TOPSIS()

    decision = topsis.decide(data)

    return decision.rank_


class Country:
    def __init__(self, name: str, control_of_corruption: float, political_stability: float, inflation_rate: float,
                 gdp_growth: float,
                 ease_of_doing_business: float, unemployment_rate: float, individuals_using_the_internet: float

                 ):
        self.individuals_using_the_internet = individuals_using_the_internet
        self.unemployment_rate = unemployment_rate
        self.ease_of_doing_business = ease_of_doing_business
        self.gdp_growth = gdp_growth
        self.inflation_rate = inflation_rate
        self.political_stability = political_stability
        self.control_of_corruption = control_of_corruption
        self.name = name

        def __str__(self) -> str:
            return Country.__str__()
