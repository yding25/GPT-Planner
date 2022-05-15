(define
	(problem drink_soda)
	(:domain dining)
	(:objects rob - robot glass_1 - glass soda_1 - soda table - table kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (glass_at glass_1 kitchen) (soda_at soda_1 kitchen) (table_at table dining) (bottle_of_soda_is_missing soda_1))
	(:goal (and (glass_is_filled glass_1)))
)