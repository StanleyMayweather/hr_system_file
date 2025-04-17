with open("hr_system.txt") as file:
    # The file has now been opened and stored in a variable "file"

    # Read each line, one by one, into a variable: current_line
    for line in file:
        # Split the current line into its parts based on a space " " as the separator
        parts = line.split(" ")

        # Save the parts we need into variables
        name = parts[0]
        title = parts[2]

        # Output the name and title as desired
        print(f"Name: {name}, Title: {title}")