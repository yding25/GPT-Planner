(define
	(problem clean_area)
	(:domain dining)
	(:objects vacuum_0 - vacuum vacuum_1 - vacuum outlet_0 - outlet outlet_1 - outlet rob - robot table - table kitchen - location dining - location)
	(:init (vacuum_at vacuum_1 dining) (vacuum_is_unplugged vacuum_1) (vacuum_is_off vacuum_1) (vacuum_at vacuum_0 dining) (vacuum_is_unplugged vacuum_0) (vacuum_is_off vacuum_0) (outlet_at outlet_0 dining) (outlet_at outlet_1 dining) (robot_at rob kitchen) (table_at table dining))
	(:goal (and (vacuum_is_unplugged vacuum_0) (vacuum_is_unplugged vacuum_1) (table_is_clean table)))
)