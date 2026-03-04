class Locker:
    def __init__(self, size, locker_id, is_available = True):
        self.size = size
        self.id = locker_id
        self.is_available = is_available    
        self.package = None
    def store_package(self, package):
        if self.is_available and package.size.value <= self.size.value:
            self.package = package
            self.is_available = False
            print(f"Package {package.id} stored in locker {self.id}")
        else:
            print(f"Locker {self.id} is not available for package {package.id}")
    def retrieve_package(self):
        if not self.is_available:
            print(f"Package {self.package.id} retrieved from locker {self.id} is not available")
            self.package = None
            self.is_available = True
            return self.package
        else:
            print(f"Locker {self.id} is already available, no package to retrieve")
    