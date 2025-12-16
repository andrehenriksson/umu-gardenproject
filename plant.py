import random

from pest import Pest
class Plant:
    """Class representing a plant in the garden.

    Attributes
    --------------
    name : str
        The name of the plant.

    Parameters
    ---------
    plant_name : str
        The name of the plant.
    """
    def __init__(self, plant_name: str):
        """Constructor for Plant class.

        Parameters
        ----------
        plant_name : str
            The name of the plant.

        Attributes
        ----------
        name : str
            The name of the plant.
        harvest_weeks : set of int
            The weeks when the plant can be harvested.
        yields_per_week : dict of int to float
            The yield amounts for each harvest week.    
        """
        self.name = plant_name
        self.harvest_weeks = set()
        self.yields_per_week = {}

    def add_harvest_week(self, week: int):
        """Adds a week when the plant can be harvested.

        Parameters
        ----------
        week : int
            The week number when the plant can be harvested.

        Returns
        ----------
        None
        """
        self.harvest_weeks.add(week)

    def add_yield_for_week(self, week: int, yield_amount: float):
        """Adds a yield amount for a specific week.

        Parameters
        ----------
        week : int
            The week number when the plant can be harvested.
        yield_amount : float
            The yield amount for that week.

        Returns
        ----------
        None
        """
        self.yields_per_week[week] = yield_amount
    
    def calculate_yield(self, year:int, week:int, active_pests:list, traceflag:bool=False) -> float:
        """Calculates the yield for a specific week considering active pests.

        Parameters
        ----------
        week : int
            The week number when the plant can be harvested.
        active_pests : list of Pest
            List of active pests affecting the garden.
        traceflag : bool, optional
            If True, prints debug information (default is False).

        Returns
        ----------
        float
            The yield amount for that week, considering pests.
        """
        if traceflag:
            print(f'Calculating yield for {self.name} in week {week} with active pests: {[p.name for p in active_pests]}')
        if week not in self.harvest_weeks:
            return 0
        
        # Check if any pest affects this plant in this week
        for pest in active_pests:
            if self.is_affected_by_pest(pest, week):
                return 0
        
        return self.yields_per_week.get(week, 0)
    
    def is_affected_by_pest(self, pest: Pest, week: int) -> bool:
        """Checks if the plant is affected by a specific pest in a given week.

        Parameters
        ----------
        pest : Pest
            The pest to check against.
        week : int
            The week number when the plant can be harvested.

        Returns
        ----------
        bool
            True if the plant is affected by the pest in the given week, False otherwise.
        """
        plant_type = self.__class__.__name__.lower()
        return pest.affected_plant == plant_type and pest.week_detected == week
    
    def __str__(self):
        """ String representation of the Plant object."""
        return f"Plant Name: {self.name}, Yield: {sum(self.yields_per_week.values()):.2f}, Harvest Weeks: {sorted(self.harvest_weeks)}" 

class Vegetable(Plant):
    "Docstrings for Vegetable class is inherited from Plant class. "
    def __init__(self, plant_name: str):
        super().__init__(plant_name)

        tmp_week = random.randint(1, 52)
        tmp_yield = random.randint(1, 15)
        super().add_harvest_week(tmp_week)
        super().add_yield_for_week(tmp_week, tmp_yield)

class FruitTree(Plant):
    "Docstrings for FruitTree class is inherited from Plant class. "
    def __init__(self, plant_name: str):
        super().__init__(plant_name)

        for i in range(random.randint(1, 5)):
            tmp_week = random.randint(1, 52)
            tmp_yield = random.randint(10, 50)
            super().add_harvest_week(tmp_week)
            super().add_yield_for_week(tmp_week, tmp_yield)
