(define
	(problem eat_dinner)
	(:domain dining)
	(:objects rob - robot table - table chair_1 - chair burger_1 - burger plate_1 - plate fork_1 - fork kitchen - location dining - location)
	(:init (robot_at rob dining) (hand_empty rob) (table_at table dining) (chair_at chair_1 dining) (burger_at burger_1 kitchen) (plate_at plate_1 kitchen) (fork_at fork_1 kitchen) (chair_is_broken chair_1))
	(:goal (and (chair_is_pulled chair_1) (fork_is_placed fork_1) (plate_is_placed plate_1) (burger_is_placed burger_1)))
)