(define
	(problem drink_coke)
	(:domain dining_drink_coke)
	(:objects rob_1 - robot glass_1 - glass coke_1 - coke table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 dining) (glass_at glass_1 kitchen) (coke_at coke_1 kitchen) (table_at table_1 dining))
	(:goal (and (glass_is_filled glass_1) (glass_is_placed glass_1)))
)