
from amazon_locker import Strategy


class FirstAvailableStrategy(Strategy):
    def assign_locker(self, package, lockers):
        for locker in lockers:
            if locker.is_available and locker.size.value >= package.size.value:
                locker.store_package(package)
                return
        print(f"No available locker for package {package.id}")