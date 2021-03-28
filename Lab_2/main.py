from impl import AlgorithmsImpl 
def main():
    rows = [
        [23, 37, 33, 84, 17, 12, 31, 17, 9, 65, 56, 8, 69, 45, 95, 22, 71, 95, 69, 59],
        [1, 76, 52, 71, 40, 25, 43, 72, 91, 89, 27, 66, 78, 12, 50, 96, 24, 33, 13, 86],
        [99, 70, 94, 68, 15, 41, 42, 39, 37, 63, 98, 90, 39, 2, 13, 31, 28, 57, 4, 71] 
    ] 
    all_rows = rows[0] + rows[1] + rows[2]
    appImpl = AlgorithmsImpl()
    currentArray = all_rows

    print('Min containers num for row #1: ', appImpl.theoreticalContainers(rows[0]), '( ' + str(appImpl.getCargosSum(rows[0])) + ' / ' + str(appImpl.containerCapacity) + ')') 
    print('Min containers num for row #2: ', appImpl.theoreticalContainers(rows[1]),'( ' + str(appImpl.getCargosSum(rows[1])) + ' / ' + str(appImpl.containerCapacity) + ')') 
    print('Min containers num for row #3: ', appImpl.theoreticalContainers(rows[2]),'( ' + str(appImpl.getCargosSum(rows[2])) + ' / ' + str(appImpl.containerCapacity) + ')') 
    print('Min containers num for all rows: ', appImpl.theoreticalContainers(all_rows),'( ' + str(appImpl.getCargosSum(all_rows)) + ' / ' + str(appImpl.containerCapacity) + ')') 
    
    appImpl.NFA(currentArray, False)
    appImpl.NFA(currentArray, True, False)
    appImpl.NFA(currentArray, True, True)

    appImpl.FFA(currentArray, False)
    appImpl.FFA(currentArray, True, False) 
    appImpl.FFA(currentArray, True, True)

    appImpl.WFA(currentArray, False)
    appImpl.WFA(currentArray, True, False) 
    appImpl.WFA(currentArray, True, True) 

    appImpl.BFA(currentArray, False)
    appImpl.BFA(currentArray, True, False) 
    appImpl.BFA(currentArray, True, True) 

if __name__ == '__main__': 
    main() 