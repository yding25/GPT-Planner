(define
	(problem drink_soda)
	(:domain dining)
	(:objects rob - robot glass_1 - glass soda_1 - soda table - table kitchen - location dining - location water_1 - soda)
	(:init (robot_at rob dining) (hand_empty rob) (glass_at glass_1 kitchen) (soda_at soda_1 kitchen) (table_at table dining) (bottle_of_soda_is_missing soda_1) (soda_at water_1 kitchen))
	(:goal (or (and (glass_is_filled glass_1)) (and (glass_is_filled glass_1))))
)