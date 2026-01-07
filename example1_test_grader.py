







#print("I hate everything")

# final version with testing capabilities


# =================================================
# STUDENT SUBMISSION (PASTE WHOLE CODE HERE)
# =================================================




def _findFirstOccurrence(nums, target):
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid          # record the index
            high = mid - 1        # continue searching left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


    return result







#******CHANGE***************
#**************************************************
#REPLACE THE FUNCTION BELOW WITH THE FUNCTION FROM ABOVE, 
#BUT REMOVE THE " _  " FROM THE FUNCTION NAME
# OR THIS WILL NOT WORK
#ONLY REPLACE THE FUNCTION NAME.....
#**************************************************
def findFirstOccurrence(*args):
    """
    Universal adapter version.
    Supports:
    - maximizeNonOverlappingMeetings(meetings)
    - maximizeNonOverlappingMeetings(rows, cols, meetings)
    """

    # -----------------------------
    # Normalize inputs
    # -----------------------------
    if len(args) == 1:
        meetings = args[0]

    elif len(args) == 3:
        meetings = args[2]

    else:
        return -1

    # Validate meetings format
    if not meetings:
        return 0

    # Convert tuples to lists if needed
    meetings = [list(m) for m in meetings if isinstance(m, (list, tuple)) and len(m) == 2]

    # -----------------------------
    # Core logic (unchanged)
    # -----------------------------
    meetings.sort(key=lambda x: x[1])

    count = 0
    last_end = -1

    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end

    return count


# =================================================
# TEST CASES
# =================================================

TESTS = [
    {
        "inputs": ([], 5),
        "expected": -1
    },
    {
        "inputs": (1, 2, [(5, 10)]),
        "expected": 1
    },
    {
        "inputs": ([1, 2, 3, 4, 5], 3),
        "expected": -1
    },
    {
        "inputs": (3, 2, [(1, 2), (2, 3), (3, 4)]),
        "expected": 3
    }
]


#*******************DO NOT MODIFY THIS FILE***********************#
#**ONLY MODIFY "RESULT" STATEMENT*******
#***TO FUNCTION ABOVE***********************
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

        #result = maximizeNonOverlappingMeetings(*inputs)
        result = findFirstOccurrence(*inputs)


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


# still testing this code for functionality, will update as i progress..
# =================================================



