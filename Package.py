from datetime import timedelta

class Package:
    
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        """
        Initialize a Package object with its details.
        """
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        """
        Return a string representation of the package's current state.
        """
        return f'ID: {self.package_id}; Address: {self.address}, {self.city}, {self.state}, {self.zip_code}; Deadline: {self.deadline}; Weight: {self.weight}, {self.status} at {self.delivery_time}.'

    def update_status(self, current_time):
        """
        Update the package's status and address based on the current time.
        """
        if self.delivery_time and self.delivery_time < current_time:
            self.status = "Delivered"
        elif self.departure_time and self.departure_time <= current_time:
            self.status = "En Route"
        else:
            self.status = "At The Hub"
         
        # Update the address for package ID 9 if the time is after 10:20 am 
        if self.package_id == 9 and current_time >= timedelta(hours=10, minutes=20):
            self.address = "410 S State St"