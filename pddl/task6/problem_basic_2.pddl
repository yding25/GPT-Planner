(define
	(problem set_table)
	(:domain dining)
	(:objects rob - robot cupboard - cupboard plate_1 - plate fork_1 - fork plate_2 - plate fork_2 - fork table - table kitchen - location dining - location)
	(:init (plate_at plate_1 kitchen) (plate_at plate_2 kitchen) (fork_at fork_1 kitchen) (fork_at fork_2 kitchen) (table_at table dining) (robot_at rob dining) (hand_empty rob) (cupboard_at cupboard kitchen) (cupboard_is_closed cupboard))
	(:goal (or (and (cupboard_is_closed cupboard) (plate_is_placed plate_1 table) (fork_is_placed fork_1 table)) (and (cupboard_is_closed cupboard) (plate_is_placed plate_2 table) (fork_is_placed fork_2 table))))
	(:goal (and (cupboard_is_closed cupboard) (or (plate_is_placed plate_1 table) (plate_is_placed plate_2 table)) (or (fork_is_placed fork_1 table) (fork_is_placed fork_2 table))))
)