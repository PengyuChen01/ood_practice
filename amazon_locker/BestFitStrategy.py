
from amazon_locker import Strategy


class BestFitStrategy(Strategy):
    def assign_locker(self, package, lockers):
        avilable_lockers = [locker for locker in lockers if locker.is_available and locker.size.value >= package.size.value
                            ]
        if not avilable_lockers:
            print(f"No available locker for package {package.id}")
            return
        best_locker  = avilable_lockers[0]
        for locker in avilable_lockers:
            if locker.size.value < best_locker.size.value:
                best_locker = locker
        return best_locker
