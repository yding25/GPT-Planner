(define
	(problem pickup_plate)
	(:domain dining_pickup_plate)
	(:objects rob_1 - robot plate_1 - plate sink_1 - sink table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 kitchen) (plate_at plate_1 dining) (sink_at sink_1 kitchen) (table_at table_1 dining))
	(:goal (and (plate_is_placed plate_1)))
)