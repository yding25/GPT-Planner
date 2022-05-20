(define
	(problem drink_water)
	(:domain dining)
	(:objects rob - robot cup_1 - cup faucet_0 - faucet table_0 - table kitchen - location dining - location)
	(:init (robot_at rob dining) (cup_at cup_1 kitchen) (faucet_at faucet_0 kitchen) (table_at table_0 dining) (faucet_is_off faucet_0) (cup_is_empty cup_1))
	(:goal (and (cup_is_placed cup_1) (faucet_is_off faucet_0)))
)