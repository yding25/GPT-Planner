(define
	(problem clean_floor)
	(:domain dining_clean_floor)
	(:objects rob_1 - robot vacuum_1 - vacuum table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 kitchen) (vacuum_at vacuum_1 dining) (table_at table_1 dining) (vacuum_is_unplug vacuum_1) (vacuum_is_off vacuum_1) (robot_cannot_reach_the_vacuum rob_1))
	(:goal (and (vacuum_is_off vacuum_1) (table_is_clean table_1)))
)