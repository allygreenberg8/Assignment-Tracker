# Import required libraries
from datetime import datetime  # For handling dates
import json  # For saving/loading data to/from JSON file
import os    # For checking if file exists

class AssignmentTracker: #this class creates an object that can be used to track assignments
    def __init__(self, semester=None):
        # Initialize empty list to store assignments
        self.assignments = []
        # Set the filename where assignments will be saved
        self.filename = f"assignments_{semester}.json" if semester else "assignments.json"  # Filename includes semester if provided
        # Load any existing assignments when creating new instance of the object - so for fall semester load in all the assignments 
        self.load_assignments()

    def load_assignments(self):
        # Check if the file exists
        if os.path.exists(self.filename): 
            # Open and read the JSON file
            with open(self.filename, 'r') as file:
                # Convert JSON data back to Python list
                self.assignments = json.load(file)

    def save_assignments(self):
        # Open file in write mode (creates file if it doesn't exist)
        with open(self.filename, 'w') as file:
            # Convert Python list to JSON and save to file
            # indent=4 makes the JSON file human-readable
            json.dump(self.assignments, file, indent=4)

    def add_assignment(self, title, due_date, description=""):
        # Create a dictionary representing a single assignment
        assignment = {
            "title": title,
            "due_date": due_date,
            "description": description,
            "completed": False  # New assignments start as incomplete
        }
        # Add the new assignment to our list
        self.assignments.append(assignment)
        # Save changes to file
        self.save_assignments()

    def view_assignments(self):
        # Check if there are any assignments to display
        if not self.assignments:
            print("No assignments found!")
            return
        
        # Loop through assignments with index numbers starting at 1
        for i, assignment in enumerate(self.assignments, 1):
            # Display the status of the assignment
            status = "completed" if assignment["completed"] else " "
            # Display assignment with its index, status, title, and due date
            print(f"{i}. [{status}] {assignment['title']} - Due: {assignment['due_date']}")
            # Only show description if one exists
            if assignment["description"]:
                print(f"   Description: {assignment['description']}")

    def mark_completed(self, index):
        # Check if the provided index is valid
        if 1 <= index <= len(self.assignments):
            # Mark the assignment as completed (subtract 1 from index since list starts at 0)
            self.assignments[index-1]["completed"] = True
            # Save changes to file
            self.save_assignments()
            print("Assignment marked as completed!")
        else:
            print("Invalid assignment number!")

def main():
    # Create instance of AssignmentTracker with a semester
    tracker = AssignmentTracker("Fall2023")
    
    print("\nNote: You can press Ctrl+C at any time to force exit the program")
    
    # Main program loop
    while True:
        try:
            # Display menu options
            print("\nAssignment Tracker")
            print("1. Add Assignment")
            print("2. View Assignments")
            print("3. Mark Assignment as Completed")
            print("4. Exit")
            print("5. Force Exit")
            
            # Get user's choice
            choice = input("Enter your choice (1-5): ")
            
            if choice == "5":
                print("\nForce exiting program...")
                exit()
            
            # Convert choice to integer and validate
            choice = int(choice)
            if choice < 1 or choice > 5:  # Changed from 4 to 5
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
                
            # Handle user's choice
            if choice == 1:
                # Collect assignment details from user
                title = input("Enter assignment title: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                description = input("Enter description (optional): ")
                # Add the new assignment
                tracker.add_assignment(title, due_date, description)
                print("Assignment added successfully!")
                
            elif choice == 2:
                # Show all assignments
                tracker.view_assignments()
                
            elif choice == 3:
                # Show assignments so user can choose which to mark complete
                tracker.view_assignments()
                # Get assignment number from user and convert to integer
                index = int(input("Enter the number of the assignment to mark as completed: "))
                tracker.mark_completed(index)
                
            elif choice == 4:
                print("Goodbye!")
                break  # Exit the program
                
            else:
                print("Invalid choice! Please try again.")
                
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user (Ctrl+C)")
            exit()
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            choice = input("Enter 'q' to quit or any other key to continue: ")
            if choice.lower() == 'q':
                exit()

if __name__ == "__main__":
    main()