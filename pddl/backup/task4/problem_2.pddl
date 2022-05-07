(define
	(problem drink_water)
	(:domain dining_drink_water)
	(:objects
		; following objects are required
		rob1 - robot
		cup1 - cup
		faucet1 - faucet
		table1 - table
		kitchen - location
		dining - location
		
		; following objects are alternative
		cup2 - cup
	)
	(:init 
		(robot_at rob1 dining) 
		(cup_at cup1 kitchen)
		(cup_at cup2 kitchen)
		(faucet_at faucet1 kitchen)
		(table_at table1 dining)
		
		(faucet_is_turned_off faucet1)
		(cup_is_empty cup1)
		(cup_is_empty cup2)
		(hand_empty rob1))

	(:goal (or (and (cup_is_filled cup1) (cup_is_on_table cup1 table1) (faucet_is_turned_off faucet1)) (and (cup_is_filled cup2) (cup_is_on_table cup2 table1) (faucet_is_turned_off faucet1))))
)
