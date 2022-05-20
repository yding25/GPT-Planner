(define
	(problem grasp_plate)
	(:domain dining)
	(:objects rob - robot plate_0 - plate sink_1 - sink table_1 - table kitchen - location dining - location)
	(:init (robot_at rob kitchen) (plate_at plate_0 dining) (sink_at sink_1 kitchen) (table_at table_1 dining))
	(:goal (and (plate_is_placed plate_0)))
)