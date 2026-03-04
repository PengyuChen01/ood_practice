amazon locker

use case:
    1. Delivery man delivery package to locker
    2. locker send message to customer 
    3. customer use code from message to get package

core class:
lockerSize[Enum] : SMALL, MEDIUM, LARGE
package: packageID, size
locker: lockerid, size, isAvailable, package
    store_package(pkg) / retrieve_package()
LockerAssignmentStrategy(Interface): assignLocker(pkg, lockers)
    -bestFitStrategy
    -firstAvailableStrategy
LockerSystem: lockers, strategy, codeMap
    -delivery(pkg) -> pickupCode
    -pickup(code) -> package
NotificationService:
    -notifyCustomer(customerId, pickupCode)

key flow:
delivery man use its own code to open the locker, and store package with propersize
customer use code to open corresponding locker, and get package