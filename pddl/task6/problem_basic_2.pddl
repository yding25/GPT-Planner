(define
	(problem set_table)
	(:domain dining)
	(:objects rob - robot cupboard_0 - cupboard plate_1 - plate fork_1 - fork plate_2 - plate fork_2 - fork table_0 - table kitchen - location dining - location)
	(:init (plate_at plate_1 kitchen) (plate_at plate_2 kitchen) (fork_at fork_1 kitchen) (fork_at fork_2 kitchen) (table_at table_0 dining) (robot_at rob dining) (hand_empty rob) (cupboard_at cupboard_0 kitchen) (cupboard_is_closed cupboard_0))
	(:goal (and (cupboard_is_closed cupboard_0) (or (plate_is_placed plate_1 table_0) (plate_is_placed plate_2 table_0)) (or (fork_is_placed fork_1 table_0) (fork_is_placed fork_2 table_0))))
)