"LeetCode/HackerRank - PYTHON GRADER"

Python script for testing LeetCode and HackerRank solutions- prior to submitting 

please use a side by side comparision of each example; if needing a visual example..

INSTRUCTIONS ON HOW TO USE:
read instructions for either site. write your code that you think will work.. 

STEP 1:
****PASTE YOUR CODE****
the code you wrote; you will paste under the "#STUDENT SUBMMISSION" section. (see example)
********very important to add "  _  " to the begining of your function*******

“example_2_test_grader.py”
# =================================================
# STUDENT SUBMISSION (PASTE CODE HERE)
# =================================================


def _maximizeNonOverlappingMeetings(meetings):
    if not meetings:
        return 0

    # Sort meetings by end time
    meetings.sort(key=lambda x: x[1])

    count = 0
    last_end = -1

    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end

    return count
****************************************************************
****************************************************************

example 1

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

____________________________________________________________________________________________________________
_____________________________________________________________________________________________________________

STEP 2:
**do not forget this part or your code will not work***** **
****** REMOVE THE "  _  " IN FRONT OF YOUR FUNCTION; LOCATED IN THE "CHANGE SECTION"*****

“example_2_test_grader.py”
__________________________

#******CHANGE SECTION***************
#**************************************************
#REPLACE THE FUNCTION BELOW WITH THE FUNCTION FROM ABOVE, 
#BUT REMOVE THE " _  " FROM THE FUNCTION NAME
# OR THIS WILL NOT WORK
#ONLY REPLACE THE FUNCTION NAME.....
#**************************************************
def maximizeNonOverlappingMeetings(*args):
    """
    Universal adapter version.
    Supports:
    - maximizeNonOverlappingMeetings(meetings)
    - maximizeNonOverlappingMeetings(rows, cols, meetings)

*****************************************************************
*****************************************************************

example 1

#******CHANGE SECTION***************
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

________________________________________________________________________________________________________
________________________________________________________________________________________________________

STEP 3:

replace your inputs and expected outputs with what is currently listed. what is currently listed is only to make
sure that there is not a bug when you use the code. so you can run the code and it should work without bugs.


__________________________________________________________________________________________________________
__________________________________________________________________________________________________________

STEP4:
******FOR CODE TO FUNCTION THIS MUST BE DONE********
in the ("*******************DO NOT MODIFY THIS FILE***************"), section
you do need to make one modification..
you need to modify the result statement, as showen in the examples; to match your function.
left commented out, so when making the change you, can use as a reference to see exactly what changes are needed.

“example_2_test_grader.py”
__________________________
********************
try:
        if not isinstance(inputs, tuple):
            inputs = (inputs,)

        result = maximizeNonOverlappingMeetings(*inputs)
        #result = findFirstOccurrence(*inputs)

*******************
*******************

example 1


    try:
        if not isinstance(inputs, tuple):
            inputs = (inputs,)

        #result = maximizeNonOverlappingMeetings(*inputs)
        result = findFirstOccurrence(*inputs)



______________________________________________________________________________________________________
______________________________________________________________________________________________________
expected output:
if ran correctly, the output should look something like this....

AUTOGRADER RESULTS

Test #1
Inputs: ([], 5)
Expected: -1
Got: -1 [PASS]
----------------------------------------
Test #2
Inputs: (1, 2, [(5, 10)])
Expected: 1
Got: 1 [PASS]
----------------------------------------
Test #3
Inputs: ([1, 2, 3, 4, 5], 3)
Expected: -1
Got: -1 [PASS]
----------------------------------------
Test #4
Inputs: (3, 2, [(1, 2), (2, 3), (3, 4)])
Expected: 3
Got: 3 [PASS]
----------------------------------------

ALL TESTS PASSED ✅







