(define
	(problem clean_floor)
	(:domain dining_clean_floor)
	(:objects rob_1 - robot vacuum_1 - vacuum vacuum_2 - vacuum table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 kitchen) (vacuum_at vacuum_1 dining) (vacuum_at vacuum_2 dining) (table_at table_1 dining) (vacuum_is_unplug vacuum_1) (vacuum_is_off vacuum_1) (vacuum_is_unplug vacuum_2) (vacuum_is_off vacuum_2))
	(:goal (and (or (vacuum_is_off vacuum_1) (vacuum_is_off vacuum_2)) (table_is_clean table_1)))
)