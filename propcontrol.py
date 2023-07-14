"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #3 - Proportional Control (propcontrol.py)


Author: Chris Lai

Difficulty Level: 3/10

Prompt: During the line following lab in Lab 2, you used 
proportional control (among the many types of control systems) 
to allow the RACECAR to follow a line of a specific color type. 
In proportional control, a sensor (color camera) and actuator 
(turning servo) work together in order to optimize a target value. 

In the line following lab, you want to ensure that the center of 
the line contour is in the center of the screen. Given the current 
x-axis center of the line contour’s center (stored in the variable 
center) and a tuple representing the screen resolution (stored in 
the variable res as (x, y)), write a function that calculates the 
steering angle (between -1 and 1, left -> right) that must be sent to the RACECAR
in order to allow it to follow the line.

Constraints: The value of “center” is constrained to [res[0] >= center > 0] 
and the resolution indicies “res[0]” and “res[1]” must be constrained 
to [10^5 >= res[0] >= 0], [10^5 >= res[1] >= 0]. Round the output 
answer to 6 decimal places.


Test Cases:
Input: center= 400, tuples (x, y) = (800, 600)  Output: 0.000000

Input: center= 800, tuples(x, y) = (1600, 900)  Output: 0.000000

Input: center= 720, tuples(x, y) = (1440, 900)  Output: 0.000000
"""

def remap_range(
    val: float,
    old_min: float,
    old_max: float,
    new_min: float,
    new_max: float,
) -> float:
    """
    Remaps a value from one range to another range.

    Args:
        val: A number form the old range to be rescaled.
        old_min: The inclusive 'lower' bound of the old range.
        old_max: The inclusive 'upper' bound of the old range.
        new_min: The inclusive 'lower' bound of the new range.
        new_max: The inclusive 'upper' bound of the new range.

    Note:
        min need not be less than max; flipping the direction will cause the sign of
        the mapping to flip.  val does not have to be between old_min and old_max.
    """

    diff = old_max - old_min
    percent = val / diff
    new_val = percent * (new_max - new_min)
    new_val += new_min

    return new_val

class Solution:

    def propcontrol(self, center, res):
            #type center: int
            #type res: tuples of int
            #return type: float
            
            #TODO: Write code below to return a float with the solution to the prompt.
            return remap_range(center, 0, res[0], -1, 1)
        
        

def main():
    center = int(input().strip())
    resx = int(input().strip())
    resy = int(input().strip())
    res = (resx, resy)

    tc1 = Solution()
    ans = tc1.propcontrol(center, res)
    ans=format(ans, ".6f")
    print(ans)

if __name__ and "__main__":
    main()
