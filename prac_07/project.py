"""CP1404/CP5632 Practical - Project class."""

from datetime import datetime


class Project:
    """Represent a project with name, start date, priority, cost, and completion %."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Allow sorting projects by start_date."""
        return self.start_date < other.start_date

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion_percentage >= 100
