## Approach
* The robot state is modelled by position (Point) and a facing Vector.
* Robot actions are translated to the manipulation of Point and the facing Vector. i.e. MOVE command is a translation of Point by the facing Vector. Any turn command is convert to a 90 degree rotation of the facing Vector. This approach can be extend easily in the future if more action are introduced.
* Command parsing is handle by a simple grammar parser. Input validation is handled by the grammar parser. Ivalid command is caught by ParseException and convert to a "Do nothing" action. 
* All command implements common infertace which apply a state (or nothing) to the Robot.
* Robot is bounded by a list of contraints (only one in the case). Each attempt to apply a new state to the robot, the state will be checked against all these contraints.
