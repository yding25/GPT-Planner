(define
	(problem eat_dinner)
	(:domain dining)
	(:objects chair_1 - chair burger_1 - burger plate_1 - plate fork_1 - fork chair_2 - chair burger_2 - burger plate_2 - plate fork_2 - fork rob - robot table_0 - table kitchen - location dining - location)
	(:init (chair_at chair_1 dining) (burger_at burger_1 kitchen) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (chair_at chair_2 dining) (burger_at burger_2 kitchen) (plate_at plate_2 kitchen) (fork_at fork_2 kitchen) (robot_at rob dining) (hand_empty rob) (table_at table_0 dining) (burger_spills burger_2))
	(:goal (and (or (fork_is_placed fork_1) (fork_is_placed fork_2)) (or (plate_is_placed plate_1) (plate_is_placed plate_2)) (or (burger_is_placed burger_1) (burger_is_placed burger_2)) (or (chair_is_pulled chair_1) (chair_is_pulled chair_2))))
)