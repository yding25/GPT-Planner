(define
	(problem clean_area)
	(:domain dining)
	(:objects rob - robot vacuum_1 - vacuum table - table outlet_1 - outlet kitchen - location dining - location)
	(:init (robot_at rob kitchen) (vacuum_at vacuum_1 dining) (table_at table dining) (outlet_at outlet_1 dining) (vacuum_is_unplugged vacuum_1) (vacuum_is_off vacuum_1))
	(:goal (and (vacuum_is_unplugged vacuum_1) (table_is_clean table)))
)