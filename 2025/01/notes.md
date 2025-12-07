MIN_VALUE = 0
MAX_VALUE = 99

So, 100 numbers on the dial total
RESET_VALUE = (MAX_VALUE - MIN_VALUE + 1)

If the value (current dial value + distance) is 99,
then the dial value is 99

If the value (current dial value + distance) is 100,
then the dial value is 0 

If the value (current dial value + distance) is 537,
then the dial value is:
 - after traveling over distance = 500, dial value is back to 0
 - should be 37


If the value (current dial value + distance) is -1,
then the dial value is 99

If the value (current dial value + distance) is -100,
then the dial value is 99