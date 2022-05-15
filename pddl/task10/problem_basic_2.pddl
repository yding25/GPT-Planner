(define
	(problem drink_soda)
	(:domain dining)
	(:objects rob - robot glass_1 - glass soda_1 - soda glass_0 - glass soda_0 - soda table - table kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (glass_at glass_1 kitchen) (soda_at soda_1 kitchen) (glass_at glass_0 kitchen) (soda_at soda_0 kitchen) (table_at table dining))
	(:goal (or (glass_is_filled glass_0) (glass_is_filled glass_1)))
)