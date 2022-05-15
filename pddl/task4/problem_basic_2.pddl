(define
	(problem drink_water)
	(:domain dining)
	(:objects cup_1 - cup cup_0 - cup faucet - faucet rob - robot table - table kitchen - location dining - location)
	(:init (robot_at rob dining) (cup_at cup_1 kitchen) (cup_at cup_0 kitchen) (faucet_at faucet kitchen) (table_at table dining) (faucet_is_off faucet) (cup_is_empty cup_1) (cup_is_empty cup_0))
	(:goal (and (or (cup_is_placed cup_1) (cup_is_placed cup_0)) (faucet_is_off faucet)))
)