class Pest:
    """Class representing a pest in the garden.

    Attributes
    --------------
    name : str
        The name of the pest.
    affected_plant : str
        The type of plant affected by the pest (either "FruitTree" or "Vegetable").
    week_detected : int
        The week number when the pest was detected.
    """
    def __init__(self, pest_name:str, affected_plant:str, week_detected:int):
        """Constructor for Pest class.

        Parameters
        ----------
        pest_name : str
            The name of the pest.
        affected_plant : str
            The type of plant affected by the pest (either "FruitTree" or "Vegetable").
        week_detected : int
            The week number when the pest was detected.

        Attributes
        ----------
        name : str
            The name of the pest.
        affected_plant : str
            The type of plant affected by the pest (either "FruitTree" or "Vegetable").
        week_detected : int
            The week number when the pest was detected.
        """
        self.name = pest_name
        try:
            affected_plant = affected_plant.lower().strip()
            if not isinstance(affected_plant, str) or not affected_plant in ["fruittree", "vegetable"]:
                raise ValueError("affected_plant must be a non-empty string and either 'FruitTree' or 'Vegetable'")
            if not isinstance(week_detected, int) or week_detected < 1 or week_detected > 52:
                raise ValueError("week_detected must be an integer between 1 and 52")
        except ValueError as e:
            print(e)
            raise
        self.affected_plant = affected_plant
        self.week_detected = week_detected

    def __str__(self) -> str:
        return f"Pest Name: {self.name}, Affected Plant: {self.affected_plant}, Week Detected: {self.week_detected}"