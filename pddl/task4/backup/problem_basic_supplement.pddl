(define
	(problem drink_water)
	(:domain dining_drink_water)
	(:objects rob_1 - robot cup_1 - cup faucet_1 - faucet table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 dining) (cup_at cup_1 kitchen) (faucet_at faucet_1 kitchen) (table_at table_1 dining) (faucet_is_off faucet_1) (cup_is_empty cup_1) (hand_empty rob_1))
	(:goal (and (cup_is_filled cup_1) (cup_is_placed cup_1) (faucet_is_off faucet_1)))
)