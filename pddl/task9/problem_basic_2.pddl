(define
	(problem pickup_plate)
	(:domain dining_pickup_plate)
	(:objects rob_1 - robot plate_1 - plate plate_2 - plate sink_1 - sink table_1 - table kitchen - location dining - location)
	(:init (robot_at rob_1 kitchen) (plate_at plate_1 dining) (plate_at plate_2 dining) (sink_at sink_1 kitchen) (table_at table_1 dining))
	(:goal (or (and (plate_is_placed plate_1)) (and (plate_is_placed plate_2))))
)