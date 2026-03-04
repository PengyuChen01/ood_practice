'''
deliver man deliver package to locker
customer pick up package from locker
'''
class LockSystem:
    def __init__(self,lockers, strategy):
        self.lockers = lockers
        self.strategy = strategy
        self.codeMap = {}
    
    def deliver_package(self, package):
        locker = self.strategy.assign_locker(package, self.lockers)
        if locker:
            locker.store_package(package)
            code = self.generate_code(package)
            self.codeMap[code] = locker
            return code
        return None
        
    def pickup_package(self, code):
        if code in self.codeMap:
            locker = self.codeMap[code]
            package = locker.retrieve_package()
            del self.codeMap[code]
            return package
        return None
    def generate_code(self, package):
        return f"CODE-{package.id}"