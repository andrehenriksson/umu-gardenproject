from pest import Pest
from plant import Plant


class GardenContainer:
    """Class representing a garden container holding plants and pests.

    Attributes
    --------------
    plants : dict of str to Plant
        A dictionary mapping plant names to Plant objects.
    pests : dict of str to Pest
        A dictionary mapping pest names to Pest objects.
    """
    def __init__(self, plants = None):
        """Constructor for GardenContainer class.

        Parameters
        ----------
        plants : dict of str to Plant
            A dictionary mapping plant names to Plant objects.

        Attributes
        ----------
        plants : dict of str to Plant
            A dictionary mapping plant names to Plant objects.
        pests : dict of str to Pest
            A dictionary mapping pest names to Pest objects.
        """
        if plants is None:
            plants = {}
        self.plants = plants
        self.pests = {}

    def add_plant(self, plant: Plant):
        """Adds a plant to the garden.

        Parameters
        ----------
        plant : Plant
            The Plant object to be added to the garden.

        Returns
        ----------
        None
        """
        self.plants[plant.name] = plant

    def add_pest(self, pest: Pest):
        """Adds a pest to the garden.

        Parameters
        ----------
        pest : Pest
            The Pest object to be added to the garden.

        Returns
        ----------
        None
        """
        self.pests[pest.name] = pest


    def care_for_garden(self):
        """Removes all pests from the garden.

        Parameters
        ----------
        None

        Returns
        ----------
        None
        """
        self.pests.clear()
        
    def __str__(self):
        return f'The garden has {len(self.plants)} plants.'
    
    # Garden harvest logic
    def harvest(self, year:int, week:int, traceflag:bool=False) -> float:
        """Harvests plants in the garden for a given year and week.

        Parameters
        ----------
        year : int
            The year of the harvest.
        week : int
            The week number of the harvest.
        traceflag : bool, optional
            If True, prints detailed trace information during harvest (default is False).

        Returns
        ----------
        total_yield : float
            The total yield from all plants in the garden for the specified week.
        """
        active_pests = [p for p in self.pests.values() if p.week_detected == week]
        total_yield = 0
        for plant in self.plants.values():
            yield_amount = plant.calculate_yield(year, week, active_pests, traceflag=traceflag)
            if traceflag:
                print(f'Harvested {yield_amount} from {plant.name} in week {week} of year {year}.')
            total_yield += yield_amount
        return total_yield