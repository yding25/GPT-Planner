(define
	(problem drink_coke)
	(:domain dining)
	(:objects rob - robot glass_1 - glass coke_1 - coke glass_2 - glass coke_2 - coke table_0 - table kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (glass_at glass_1 kitchen) (coke_at coke_1 kitchen) (glass_at glass_2 kitchen) (coke_at coke_2 kitchen) (table_at table_0 dining))
	(:goal (and (or (glass_is_filled glass_2) (glass_is_filled glass_1))))
)