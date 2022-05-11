(define
	(domain dining_pickup_plate)
	(:requirements :strips :typing)
	(:types robot table plate sink location food utensil beverage furniture other appliance)
	(:predicates (robot_at ?r - robot ?l - location) (table_at ?t - table ?l - location) (plate_at ?p - plate ?l - location) (sink_at ?s - sink ?l - location) (robot_near_table ?r - robot) (robot_near_sink ?r - robot) (table_is_found ?t - table) (plate_is_grasped ?p - plate) (plate_is_placed ?p - plate) (appliance_at ?a - appliance ?l) (sink_is_full ?s - sink))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1))
		:effect (and (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action find_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (table_is_found ?t) (robot_at ?r ?l))
	)

	(:action walk_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_at ?t ?l) (table_is_found ?t) (robot_at ?r ?l))
		:effect (and (robot_near_table ?r) (table_at ?t ?l) (table_is_found ?t) (robot_at ?r ?l))
	)

	(:action grasp_plate
		:parameters (?r - robot ?p - plate ?l - location)
		:precondition (and (robot_near_table ?r) (plate_at ?p ?l))
		:effect (and (plate_is_grasped ?p))
	)

	(:action walk_sink
		:parameters (?r - robot ?s - sink ?p - plate ?l - location)
		:precondition (and (plate_is_grasped ?p) (robot_at ?r ?l) (sink_at ?s ?l) (not (sink_is_full ?s)))
		:effect (and (robot_near_sink ?r) (plate_is_grasped ?p))
	)

	(:action place_plate
		:parameters (?r - robot ?p - plate ?l - location)
		:precondition (and (robot_near_sink ?r))
		:effect (and (plate_is_placed ?p) (not (plate_is_grasped ?p)))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)