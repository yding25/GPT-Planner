(define
	(domain dining)
	(:requirements :strips :typing)
	(:types robot soda glass table location food utensil beverage furniture other appliance)
	(:predicates (robot_at ?r - robot ?l - location) (hand_empty ?r - robot) (soda_at ?s - soda ?l - location) (glass_at ?g - glass ?l - location) (table_at ?t - table ?l - location) (soda_is_found ?s - soda) (soda_is_grasped ?s - soda) (glass_is_found ?g - glass) (glass_is_grasped ?g - glass)  (glass_is_filled ?g - glass) (glass_is_placed ?g - glass) (appliance_at ?a - appliance ?l))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1))
		:effect (and (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

    (:action find_glass
		:parameters (?r - robot ?g - glass ?l - location)
		:precondition (and (glass_at ?g ?l) (robot_at ?r ?l))
		:effect (and (glass_is_found ?g))
	)

	(:action grasp_glass
		:parameters (?r - robot ?g - glass ?l - location)
		:precondition (and (glass_is_found ?g) (glass_at ?g ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (glass_is_grasped ?g) (not (hand_empty ?r)))
	)

	(:action move_glass
		:parameters (?r - robot ?g - glass ?l1 - location ?t - table ?l2 - location)
		:precondition (and (glass_is_grasped ?g) (glass_at ?g ?l1) (table_at ?t ?l2) (robot_at ?r ?l1))
		:effect (and (glass_at ?g ?l2) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action place_glass
		:parameters (?r - robot ?g - glass ?t - table ?l - location)
		:precondition (and (glass_is_grasped ?g) (glass_at ?g ?l) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (glass_is_placed ?g) (not (glass_is_grasped ?g)) (hand_empty ?r))
	)

    (:action find_soda
		:parameters (?r - robot ?s - soda ?l - location)
		:precondition (and (soda_at ?s ?l) (robot_at ?r ?l))
		:effect (and (soda_is_found ?s))
	)

	(:action grasp_soda
		:parameters (?r - robot ?s - soda ?l - location)
		:precondition (and (soda_is_found ?s) (soda_at ?s ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (soda_is_grasped ?s) (not (hand_empty ?r)))
	)

	(:action move_soda
		:parameters (?r - robot ?s - soda ?g - glass ?l1 - location ?l2 - location)
		:precondition (and (soda_is_grasped ?s) (soda_at ?s ?l1) (glass_is_placed ?g) (glass_at ?g ?l2) (robot_at ?r ?l1))
		:effect (and (soda_at ?s ?l2) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action pour_soda
		:parameters (?r - robot ?s - soda ?g - glass ?l - location)
		:precondition (and (glass_is_placed ?g) (soda_is_grasped ?s) (soda_at ?s ?l) (glass_at ?g ?l) (robot_at ?r ?l))
		:effect (and (glass_is_filled ?g) (hand_empty ?r))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)