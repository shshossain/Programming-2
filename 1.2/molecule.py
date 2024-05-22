from atom import Atom

class Molecule:
    """Represents a molecule composed of atoms."""

    def __init__(self, atoms):
        """
        Initializes a Molecule object with a list of atoms and their counts.

        Args:
            atoms (list): A list of tuples, where each tuple contains an Atom object
                          and its count in the molecule.
        """
        self.atoms = atoms

    def __str__(self):
        """
        Returns the molecule's chemical formula.

        """
        return ''.join(f"{atom.symbol}{count if count > 1 else ''}" for atom, count in self.atoms)
        
    def __add__(self, other):
        """
        Adds two Molecule objects together to create a new Molecule.

        Args:
            other: Another Molecule object to be added.

        Returns:
            Molecule: New Molecule object representing the combination of the two input molecules.
        """
        new_atoms = self.atoms + other.atoms
        return Molecule(new_atoms)

# Example usage:
hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)
nitrogen = Atom('N', 7, 7)
water = Molecule([(hydrogen, 2), (oxygen, 1)])
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
#ammonia = Molecule([(nitrogen, 1), (hydrogen, 3)])
print(water)        # H2O
#print(ammonia) #NH3
print (water + co2) # H2OCO2
