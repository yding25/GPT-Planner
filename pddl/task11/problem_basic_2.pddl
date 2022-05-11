(define
	(problem eat_dinner)
	(:domain dining_eat_dinner)
	(:objects rob_1 - robot table_1 - table chair_1 - chair burger_1 - burger plate_1 - plate fork_1 - fork chair_2 - chair burger_2 - burger plate_2 - plate fork_2 - fork kitchen - location dining - location)
	(:init (robot_at rob_1 dining) (table_at table_1 dining) (chair_at chair_1 dining) (burger_at burger_1 kitchen) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (chair_at chair_2 dining) (burger_at burger_2 kitchen) (plate_at plate_2 kitchen) (fork_at fork_2 kitchen))
	(:goal (or (and (fork_is_placed fork_1) (plate_is_placed plate_1) (chair_is_pulled chair_1) (burger_is_placed burger_1)) (and (fork_is_placed fork_2) (plate_is_placed plate_2) (chair_is_pulled chair_2) (burger_is_placed burger_1))))
)