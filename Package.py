from datetime import timedelta

class Package:
    
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        """
        Initialize a Package object with its details.
        """
        self.package_id = package_id
        self.original_address = address  # Keep the original address immutable
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def update_status(self, current_time):
        """
        Return a string representation of the package's status at a given time.
        This method does not modify the package object itself.
        """
        # Determine if we should use the corrected address
        address_to_use = self.original_address
        if self.package_id == 9 and current_time >= timedelta(hours=10, minutes=20):
            address_to_use = "410 S State St"

        # Determine the status and construct the status string
        if self.delivery_time and self.delivery_time < current_time:
            status = f"Delivered at {self.delivery_time}."
        elif self.departure_time and self.departure_time <= current_time:
            status = f"En Route at {current_time}."
        else:
            status = f"At The Hub at {current_time}."

        # Return the formatted package details
        return f'ID: {self.package_id}; Address: {address_to_use}, {self.city}, {self.state}, {self.zip_code}; Deadline: {self.deadline}; Weight: {self.weight}; {status}'

    def __str__(self):
        """
        Return a string representation of the package's current state.
        """
        return f'ID: {self.package_id}; Address: {self.address}, {self.city}, {self.state}, {self.zip_code}; Deadline: {self.deadline}; Weight: {self.weight}, {self.status} at {self.delivery_time}.'