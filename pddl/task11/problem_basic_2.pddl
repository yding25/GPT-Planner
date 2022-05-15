(define
	(problem eat_dinner)
	(:domain dining)
	(:objects chair_1 - chair burger_1 - burger plate_1 - plate fork_1 - fork chair_0 - chair burger_0 - burger plate_0 - plate fork_0 - fork rob - robot table - table kitchen - location dining - location)
	(:init (chair_at chair_1 dining) (burger_at burger_1 kitchen) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (chair_at chair_0 dining) (burger_at burger_0 kitchen) (plate_at plate_0 kitchen) (fork_at fork_0 kitchen) (robot_at rob dining) (hand_empty rob) (table_at table dining))
	(:goal (and (or (fork_is_placed fork_1) (fork_is_placed fork_0)) (or (plate_is_placed plate_1) (plate_is_placed plate_0)) (or (burger_is_placed burger_1) (burger_is_placed burger_0)) (or (chair_is_pulled chair_1) (chair_is_pulled chair_0))))
)