(define
	(problem grasp_plate)
	(:domain dining)
	(:objects rob - robot plate - plate sink_1 - sink sink_0 - sink table - table kitchen - location dining - location)
	(:init (robot_at rob kitchen) (plate_at plate dining) (sink_at sink_1 kitchen) (sink_at sink_0 kitchen) (table_at table dining) (plate_is_dropped plate))
	(:goal (and (plate_is_placed plate)))
)