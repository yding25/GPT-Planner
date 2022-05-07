(define
	(problem drink_water)
	(:domain dining_drink_water)
	(:objects
		rob1 - robot
		cup1 - cup
		faucet1 - faucet
		table1 - table
		kitchen - location
		dining - location
	)
	(:init 
		(robot_at rob1 dining) 
		(cup_at cup1 kitchen)
		(faucet_at faucet1 kitchen)
		(table_at table1 dining)
		
		(faucet_is_turned_off faucet1)
		(cup_is_empty cup1)
		(hand_empty rob1))

	(:goal (and (cup_is_filled cup1) (cup_is_on_table cup1 table1) (faucet_is_turned_off faucet1)))
)