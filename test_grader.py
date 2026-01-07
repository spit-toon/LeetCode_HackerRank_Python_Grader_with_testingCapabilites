
#print("I hate everything")

#final version with testing capabilities







# =================================================
# STUDENT SUBMISSION (PASTE CODE HERE)
# =================================================

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1









# =================================================
# TEST CASES
# =================================================

TESTS = [
    {
        "inputs": ([0], 5),
        "expected": -1
    },
    {
        "inputs": ([1, 10, 10], 10),
        "expected": 1
    },
    {
        "inputs": ([1, 2, 3, 4, 5], 3),
        "expected": 2
    },
    
]











#*******************DO NOT MODIFY THIS FILE***********************#

# =================================================
# GRADER
# =================================================

print("\nAUTOGRADER RESULTS\n")

all_passed = True

for i, test in enumerate(TESTS, start=1):
    inputs = test["inputs"]
    expected = test["expected"]

    try:
        if not isinstance(inputs, tuple):
            inputs = (inputs,)

        result = binarySearch(*inputs)

        status = "PASS" if result == expected else "FAIL"

    except Exception as e:
        result = f"ERROR ({e})"
        status = "FAIL"

    print(f"Test #{i}")
    print(f"Inputs: {inputs}")
    print(f"Expected: {expected}")
    print(f"Got: {result} [{status}]")
    print("-" * 40)

    if status == "FAIL":
        all_passed = False

print("\nALL TESTS PASSED ✅" if all_passed else "\nSOME TESTS FAILED ❌")


#still testing this code for functionality, will update as i progress..  
# =================================================


