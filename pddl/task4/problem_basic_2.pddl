(define
	(problem drink_water)
	(:domain dining)
	(:objects cup_1 - cup cup_2 - cup faucet_0 - faucet rob - robot table_0 - table kitchen - location dining - location)
	(:init (robot_at rob dining) (cup_at cup_1 kitchen) (cup_at cup_2 kitchen) (faucet_at faucet_0 kitchen) (table_at table_0 dining) (faucet_is_off faucet_0) (cup_is_empty cup_1) (cup_is_empty cup_2))
	(:goal (and (or (cup_is_placed cup_1) (cup_is_placed cup_2)) (faucet_is_off faucet_0)))
)