from src.sections import reading, listening, speaking, writing

class IELTSBot:
    def __init__(self):
        self.sections = {
            "Reading": reading,
            "Listening": listening,
            "Speaking": speaking,
            "Writing": writing
        }

    def start(self):
        print("Welcome to the IELTS Bot!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '5':
                print("Thank you for using IELTS Bot. Goodbye!")
                break
            elif choice in ['1', '2', '3', '4']:
                section = list(self.sections.keys())[int(choice) - 1]
                self.practice_section(section)
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\nWhat would you like to practice?")
        for i, section in enumerate(self.sections.keys(), 1):
            print(f"{i}. {section}")
        print("5. Exit")

    def practice_section(self, section):
        print(f"\nPracticing {section}...")
        self.sections[section].practice()