(define
	(problem clean_area)
	(:domain dining)
	(:objects vacuum_1 - vacuum vacuum_2 - vacuum outlet_1 - outlet outlet_2 - outlet rob - robot table_0 - table kitchen - location dining - location)
	(:init (vacuum_at vacuum_1 dining) (vacuum_is_unplugged vacuum_1) (vacuum_is_off vacuum_1) (vacuum_at vacuum_2 dining) (vacuum_is_unplugged vacuum_2) (vacuum_is_off vacuum_2) (outlet_at outlet_1 dining) (outlet_at outlet_2 dining) (robot_at rob kitchen) (table_at table_0 dining))
	(:goal (and (vacuum_is_unplugged vacuum_1) (vacuum_is_unplugged vacuum_2) (table_is_clean table_0)))
)