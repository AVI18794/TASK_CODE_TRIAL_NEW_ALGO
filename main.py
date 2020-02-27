from src.cargo_mapping import CargoMapping
from src.load_data import LoadData
from src.truck import Truck
from src.cargo import Cargo

if __name__ == "__main__":

    cargos = LoadData(Cargo, "files/cargo.csv")
    trucks = LoadData(Truck, "files/trucks.csv")

    print("\n Mapping between cargo and trucks (One Way)")
    CargoMapppings = CargoMapping(cargos.list, trucks.list)

    CargoMapppings.map_cargo_to_trucks()
    CargoMapppings.print_cargo_map()
