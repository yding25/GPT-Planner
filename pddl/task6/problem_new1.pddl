(define
	(problem setup_table)
	(:domain dining_setup_table)
	(:objects rob_1 - robot cupboard_1 - cupboard plate_1 - plate fork_1 - fork table_1 - table kitchen - location dining - location mug_1 - plate)
	(:init (robot_at rob_1 dining) (hand_empty rob_1) (cupboard_at cupboard_1 kitchen) (cupboard_is_closed cupboard_1) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (table_at table_1 dining) (plate_not_found plate_1) (plate_at mug_1 kitchen))
	(:goal (or (and (cupboard_is_closed cupboard_1) (plate_is_placed plate_1 table_1) (fork_is_placed fork_1 table_1)) (and (cupboard_is_closed cupboard_1) (plate_is_placed mug_1 table_1) (fork_is_placed fork_1 table_1))))
)