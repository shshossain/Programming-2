from atom import Atom
from molecule import Molecule

class Chloroplast:
    """A class representing a chloroplast, which is responsible for photosynthesis process."""
    
    def __init__(self):

        """Initializes a Chloroplast object with zero water and carbon dioxide molecules."""

        self.water = 0
        self.co2 = 0

    def add_molecule(self, molecule):

        """Add a molecule to the chloroplast and trigger photosynthesis if conditions are met.

        Args:
            molecule: An instance of the Molecule class representing either water or CO2.

        Returns:
            A list containing tuples of the resulting molecules and their counts if photosynthesis occurred, otherwise an empty list.
        """

        if molecule == water:
            self.water += 1
        elif molecule == co2:
            self.co2 += 1
        
        else:
            raise ValueError("Only water or carbon dioxide molecules can be added.")

        if self.co2 >= 6 and self.water >= 12:
            self.co2 -= 6
            self.water -= 12
            sugar = Molecule([(carbon, 6), (hydrogen, 12), (oxygen, 6)])
            oxygen = Molecule([(oxygen, 6)])
            return [(sugar, 1), (oxygen, 6)]

        return []

    def __str__(self):

        """Return a string representation of the chloroplast's molecule counts."""
        
        return f"Water - {self.water} molecules, CO2 - {self.co2} molecules"


# Define molecules
hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)
water = Molecule([(hydrogen, 2), (oxygen, 1)])
co2 = Molecule([(carbon, 1), (oxygen, 2)])

# Demo
demo = Chloroplast()
els = [water, co2]

while True:
    print('\nWhat molecule would you like to add?')
    print('[1] Water')
    print('[2] Carbon dioxide')
    print('[3] Exit program')
    print('Please enter your choice: ', end='')

    

    try:
        choice = input()

        if choice == '3':
            print("Exiting the program.")
            break
        choice = int(choice)
        if choice not in [1, 2]:
            raise ValueError
        res = demo.add_molecule(els[choice - 1])
        if len(res) == 0:
            print(demo)
        else:
            print('\n=== Photosynthesis!')
            for molecule, count in res:
                print(f"{count} molecule(s) of {molecule}")
            print(demo)

    except ValueError:
        print('\n=== That is not a valid choice.')
