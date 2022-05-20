(define
	(problem set_table)
	(:domain dining)
	(:objects rob - robot cupboard_0 - cupboard plate_1 - plate fork_1 - fork table_0 - table kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (cupboard_at cupboard_0 kitchen) (cupboard_is_closed cupboard_0) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (table_at table_0 dining))
	(:goal (and (cupboard_is_closed cupboard_0) (plate_is_placed plate_1 table_0) (fork_is_placed fork_1 table_0)))
)