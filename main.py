# main.py
import sys
from energy_tracker import EnergyTracker
from smart_fridge import SmartFridge
from air_conditioner import AirConditioner
from washing_machine import WashingMachine
from ev_charger import EVCharger
from appliance import Appliance

def get_int_input(prompt: str) -> int:
    """Safely prompts the user for an integer, retrying until valid."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")

def get_float_input(prompt: str) -> float:
    """Safely prompts the user for a float, retrying until valid."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("❌ Invalid input. Please enter a valid decimal number.")

def show_menu():
    """Prints the console selection menu."""
    print("\n==================== MENU OPTIONS ====================")
    print("1. Show All Appliances")
    print("2. Turn ON Appliance")
    print("3. Turn OFF Appliance")
    print("4. Set Usage Hours")
    print("5. Update Appliance Settings")
    print("6. Show Energy Report")
    print("7. Estimate Electricity Bill")
    print("8. Show Eco Suggestions")
    print("9. Exit")
    print("======================================================")

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')

    print("=======================================================")
    print("      SMART ECO-HOME ENERGY TRACKER SIMULATOR          ")
    print("=======================================================")
    
    # Initialize tracker and load default appliances
    tracker = EnergyTracker()
    tracker.add_default_appliances()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            tracker.show_all_appliances()
            
        elif choice == '2':
            tracker.show_all_appliances()
            app_id = get_int_input("Enter Appliance ID to turn ON: ")
            tracker.turn_on_appliance(app_id)
            
        elif choice == '3':
            tracker.show_all_appliances()
            app_id = get_int_input("Enter Appliance ID to turn OFF: ")
            tracker.turn_off_appliance(app_id)
            
        elif choice == '4':
            tracker.show_all_appliances()
            app_id = get_int_input("Enter Appliance ID: ")
            app = tracker.get_appliance_by_id(app_id)
            if app:
                hours = get_float_input(f"Enter usage hours for {app.appliance_name}: ")
                tracker.set_appliance_usage_hours(app_id, hours)
            else:
                print("❌ Error: Appliance ID not found.")
                
        elif choice == '5':
            tracker.show_all_appliances()
            app_id = get_int_input("Enter Appliance ID to update settings: ")
            app = tracker.get_appliance_by_id(app_id)
            if not app:
                print("❌ Error: Appliance ID not found.")
                continue
                
            if isinstance(app, SmartFridge):
                new_val = get_float_input(f"Enter new target temperature for {app.appliance_name} (°C): ")
                tracker.update_appliance_settings(app_id, new_val)
                
            elif isinstance(app, AirConditioner):
                new_val = get_float_input(f"Enter new temperature for {app.appliance_name} (°C): ")
                tracker.update_appliance_settings(app_id, new_val)
                
            elif isinstance(app, WashingMachine):
                print("Available modes: Quick, Normal, Heavy")
                new_val = input("Enter new washing mode: ").strip()
                tracker.update_appliance_settings(app_id, new_val)
                
            elif isinstance(app, EVCharger):
                new_val = get_float_input(f"Enter new battery percentage (0-100) for connected EV: ")
                tracker.update_appliance_settings(app_id, new_val)
                
        elif choice == '6':
            tracker.show_energy_report()
            
        elif choice == '7':
            bill = tracker.estimate_electricity_bill()
            total_energy = tracker.calculate_total_energy_usage()
            print(f"\n================ BILL ESTIMATE ================")
            print(f"Total Energy Consumed: {total_energy:.2f} kWh")
            print(f"Electricity Rate:      ₹{tracker.electricity_rate:.2f} / kWh")
            print(f"Estimated Total Bill:  ₹{bill:.2f}")
            print("===============================================")
            
        elif choice == '8':
            tracker.show_eco_suggestions()
            
        elif choice == '9':
            print("\nThank you for using Smart Eco-Home Energy Tracker. Save energy, save Earth! 🌍🌱\n")
            sys.exit(0)
            
        else:
            print("❌ Invalid menu choice. Please select a number from 1 to 9.")

if __name__ == "__main__":
    main()
