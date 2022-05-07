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
		; added
		bowl1 - cup
		bowl1 - bowl
	)
	(:init 
		(robot_at rob1 dining) 
		(cup_at cup1 kitchen)
		; added
		(cup_at bowl1 kitchen)
		(bowl_at bowl1 kitchen)
		(faucet_at faucet1 kitchen)
		(table_at table1 dining)
	
		(faucet_is_turned_off faucet1)
		(cup_is_empty cup1)
		; added
		(cup_is_empty bowl1)
		(bowl_is_empty bowl1)
		(hand_empty rob1)

		; added constraint: (cup_is_broken cup1)
		(cup_is_broken cup1)
	)

	; (:goal (and (cup_is_filled cup1) (cup_is_on_table cup1 table1) (faucet_is_turned_off faucet1)))
	(:goal (or (and (cup_is_filled cup1) (cup_is_on_table cup1 table1) (faucet_is_turned_off faucet1)) (and (cup_is_filled bowl1) (cup_is_on_table bowl1 table1) (faucet_is_turned_off faucet1)) ))
)
