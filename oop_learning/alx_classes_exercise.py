from abc import ABC, abstractmethod

# =======================================================
# Encapsulation
# =======================================================

class Ecosystem:
    def __init__(self, name, description, biodiversity_index):
        self.name = name
        self.description = description
        self.biodiversity_index = biodiversity_index
        
    def display_details(self):
        print(f"Ecosystem Name: {self.name}")
        print(f"Description: {self.description}")
        print(F"Biodiversity Index: {self.biodiversity_index}")
        
    def update_description(self, new_description):
        old_description = self.description
        self.description = new_description
        return f"Description updated from {old_description} to {new_description}"
    
# ==========================================================
# Inheritance
# ==========================================================

class Forest(Ecosystem):
    def __init__(self, name, description, biodiversity_index, carbon_sequestration_rate):
        super().__init__(name, description, biodiversity_index)
        self.carbon_sequestration_rate = carbon_sequestration_rate
        self.tree_species = []
        
    def add_tree_species(self, new_species):
        self.tree_species.append(new_species)
        
    def display_tree_species(self):
        return f"Tree species in {self.name}: {', '.join(self.tree_species)}"
        
# ==========================================================
# Polymorphism
# ==========================================================

class Wildlife:
    def habitat(self):
        return "Wildlife lives in various environments such as dense rainforests, oceans, land, and other planets haha"
        
class Mammal(Wildlife):
    def habitat(self):
        return "Mammals live in habitats such as forests, oceans, deserts etc"
    
class Bird(Wildlife):
    def habitat(self):
        return "Bird inhabit various environments such as forests, wetlands, and urban areas"
    
# ==========================================================
# Abstraction
# ==========================================================

class ConservationEfforts(ABC):
    
    @abstractmethod
    def implement_effort(self):
        pass
    
class Reforestation(ConservationEfforts):
    def implement_effort(self):
        return "Reforestation involves replanting trees in a deforested zone for forest continuity"

class WildlifeProtection(ConservationEfforts):
    def implement_effort(self):
        return "Wildlife protection involves obtaining stray wild animals and rehabilitating them, avoiding extinction of rare organisms, and so on"
        
# ==========================================================
# Execution Block (Tests)
# ==========================================================

if __name__ == "__main__":
    print("--- Testing Ecosystem & Inheritance ---")
    amazon = Forest("Amazon", "Dense Rainforest", 0.9, 12000)
    amazon.add_tree_species("Mahogany")
    amazon.add_tree_species("Rubber Tree")
    amazon.add_tree_species("Oak")
    amazon.add_tree_species("Mango Tree")
    amazon.display_details()
    print()
    print(amazon.update_description("Vast biodiverse jungle"))
    print()
    print(amazon.display_tree_species())
    amazon.display_details()
    
    
    print("\n--- Testing polymorphism ---")
    animals = [Wildlife(), Mammal(), Bird()]
    for animal in animals:
        print(animal.habitat())
        
        
    print("\n--- Testing Abstraction ---")
    reforestation_effort = Reforestation()
    wildlife_effort = WildlifeProtection()
    print(reforestation_effort.implement_effort())
    print(wildlife_effort.implement_effort())