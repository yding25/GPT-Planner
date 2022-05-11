(define
	(problem setup_table)
	(:domain dining_setup_table)
	(:objects rob_1 - robot cupboard_1 - cupboard plate_1 - plate fork_1 - fork plate_2 - plate fork_2 - fork table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 dining) (hand_empty rob_1) (cupboard_at cupboard_1 kitchen) (cupboard_is_closed cupboard_1) (plate_at plate_1 kitchen) (plate_at plate_2 kitchen) (fork_at fork_1 kitchen) (fork_at fork_2 kitchen) (table_at table_1 dining) (fork_not_found fork_1))
	(:goal (or (and (cupboard_is_closed cupboard_1) (plate_is_placed plate_1 table_1) (fork_is_placed fork_1 table_1)) (and (cupboard_is_closed cupboard_1) (plate_is_placed plate_2 table_1) (fork_is_placed fork_2 table_1))))
)