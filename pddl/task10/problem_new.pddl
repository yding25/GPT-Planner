(define
	(problem drink_coke)
	(:domain dining)
	(:objects rob - robot glass_1 - glass coke_1 - coke table_0 - table kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (glass_at glass_1 kitchen) (coke_at coke_1 kitchen) (table_at table_0 dining) (coke_is_dropped coke_1))
	(:goal (and (glass_is_filled glass_1)))
)