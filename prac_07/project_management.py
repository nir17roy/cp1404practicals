"""CP1404/CP5632 Practical - Project Management Program."""

from project import Project


FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    """Run the project management program."""
    projects = load_projects(FILENAME)
    print("Welcome to the Project Management System")

    menu = "\n(L)oad projects  (S)ave projects  (D)isplay projects\n(F)ilter by date  (A)dd project  (U)pdate project  (Q)uit"
    choice = input(menu + "\n>>> ").upper()

    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILENAME)
            print("Projects loaded.")
        elif choice == "S":
            save_projects(FILENAME, projects)
            print("Projects saved.")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option")
        choice = input(menu + "\n>>> ").upper()

    print("Thank you for using custom-built project manager!")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save the list of projects to a file."""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            out_file.write(f"{p.name}\t{p.start_date.strftime(DATE_FORMAT)}\t{p.priority}\t"
                           f"{p.cost_estimate}\t{p.completion_percentage}\n")


def display_projects(projects):
    """Display projects grouped by completion status."""
    print("Incomplete projects:")
    for project in sorted(projects):
        if not project.is_complete():
            print(f"  {project}")

    print("Completed projects:")
    for project in sorted(projects):
        if project.is_complete():
            print(f"  {project}")


def filter_projects(projects):
    """Filter and display projects that start after a given date."""
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = Project("", date_input, 0, 0, 0).start_date
        for project in sorted(projects):
            if project.start_date >= filter_date:
                print(project)
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")


def add_project(projects):
    """Add a new project via user input."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)


def update_project(projects):
    """Update a project’s completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_completion = input("New Percentage (leave blank to skip): ")
        if new_completion:
            project.completion_percentage = int(new_completion)

        new_priority = input("New Priority (leave blank to skip): ")
        if new_priority:
            project.priority = int(new_priority)

    except (ValueError, IndexError):
        print("Invalid project selection.")


if __name__ == "__main__":
    main()
