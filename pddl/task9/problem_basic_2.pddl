(define
	(problem grasp_plate)
	(:domain dining)
	(:objects rob - robot plate_0 - plate sink_1 - sink sink_2 - sink table_0 - table kitchen - location dining - location)
	(:init (robot_at rob kitchen) (plate_at plate_0 dining) (sink_at sink_1 kitchen) (sink_at sink_2 kitchen) (table_at table_0 dining))
	(:goal (and (plate_is_placed plate_0)))
)