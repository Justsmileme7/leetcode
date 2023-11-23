target = 9
nums = [2, 7, 11, 15]
def function (nums, target):
    list_identification = []
    for i in nums:
        compair_target = i
        for i1 in nums:
            compair_target1 = i1
            if compair_target + compair_target1 == target:
                list_identification=[nums.index(i), nums.index(i1)]
                print(list_identification)
    return list_identification
function ([3, 2, 4], 6)