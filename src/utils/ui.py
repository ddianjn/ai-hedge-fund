from typing import Dict

def interactive_choice(options: list[Dict]):
  """
  Displays a list of options and waits for user input.

  Args:
    options (list): A list of options, must have "display_name" field.

  Returns:
    Dict: The user's selected option.
  """

  print("Please select an option:")
  for i, option in enumerate(options):
    print(f"{i + 1}. {option['display_name']}")

  while True:
    try:
      choice = int(input("Enter the number of your choice: "))
      if 1 <= choice <= len(options):
        return options[choice - 1]
      else:
        print("Invalid choice. Please enter a valid number.")
    except ValueError:
      print("Invalid input. Please enter a number.")
      
def interactive_multiple_choice(options: list[Dict]):
    """
    Displays a list of options and allows for multiple selections.

    Args:
        options (list): A list of options, must have "display_name" field.

    Returns:
        list: A list of selected options.
    """

    print("Please select options (enter numbers separated by spaces):")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option['display_name']}")

    while True:
        try:
            choices = input("Enter the numbers of your choices (e.g., 1 3): ").split()
            selected_indices = [int(choice) - 1 for choice in choices]  # Convert to 0-based index
            valid_indices = all(0 <= index < len(options) for index in selected_indices)

            if valid_indices:
                return [options[index] for index in selected_indices]
            else:
                print("Invalid choice(s). Please enter valid numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")
