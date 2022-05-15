(define
	(problem set_table)
	(:domain dining)
	(:objects rob - robot cupboard - cupboard plate_1 - plate fork_1 - fork table - table kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (cupboard_at cupboard kitchen) (cupboard_is_closed cupboard) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (table_at table dining) (fork_is_dirty fork_1))
	(:goal (and (cupboard_is_closed cupboard) (plate_is_placed plate_1 table) (fork_is_placed fork_1 table)))
)