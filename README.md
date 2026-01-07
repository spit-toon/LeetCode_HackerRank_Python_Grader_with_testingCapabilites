"LeetCode/HackerRank - PYTHON GRADER"

Python script for testing LeetCode and HackerRank solutions- 

INSTRUCTIONS ON HOW TO USE:
step 1:
after you read the instructions; for your coding problem, and create your code. you can copy the code you created to solve the problem 
in the top portion of the program: 

step 2:
after you put your test code in the top; you then can put the inputs in the test cases area. 

step 3:
run the program and in a terminal, you should be given results, if you inputs worked as expected, with the code you created... I will use the current code with examples and a
description below..
_______________________________________________________
******** 
make sure whateve your "def" is called...
you CHANGE that information in the line of code..
EXAMPLE:
(new "def")
def findFirstOccurrence(nums, target):

(change this line, prior to running code):
result = findFirstOccurrence(*inputs)
*******************************************
_______________________________________________________
_______________________________________________________

step 1, example:
PASTE YOUR CODE IN THE STUDENT SUBMISSION AREA, BELOW THE COMMENTED OUT SECTION,... 
(remove the current code and replace with yours)


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



___________________________________________________________________________________________________
STEP 2, example:
PASTE YOUR CODE IN THE "TEST CASES" AREA, BELOW THE COMMENTED OUT SECTION,... 
(remove the current code/"inputs/expected" and replace with yours)



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


___________________________________________________________________________

STEP 3, EXAMPLE:
RUN THE CODE WITH THE NEW INFORMATION IN A TERMINAL; 
(still testing this, with random things for bugs)
if sucessfull should show this result:

AUTOGRADER RESULTS

Test #1
Inputs: ([0], 5)
Expected: -1
Got: -1 [PASS]
----------------------------------------
Test #2
Inputs: ([1, 10, 10], 10)
Expected: 1
Got: 1 [PASS]
----------------------------------------
Test #3
Inputs: ([1, 2, 3, 4, 5], 3)
Expected: 2
Got: 2 [PASS]
----------------------------------------

ALL TESTS PASSED ✅







