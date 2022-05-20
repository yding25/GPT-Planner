(define
	(domain dining)
	(:requirements :strips :typing)
	(:types robot table chair burger plate fork location food utensil beverage furniture other appliance)
	(:predicates (robot_at ?r - robot ?l - location) (hand_empty ?r) (table_at ?t - table ?l - location) (robot_near_table ?r) (chair_at ?c - chair ?l - location) (chair_is_found ?c) (table_is_found ?t) (chair_is_pulled ?c) (burger_at ?b - burger ?l - location) (burger_is_found ?b - burger) (burger_is_grasped ?b - burger) (burger_is_placed ?b - burger) (plate_at ?p - plate ?l - location) (plate_is_found ?p - plate) (plate_is_grasped ?p - plate) (plate_is_placed ?p - plate) (fork_at ?f - fork ?l - location) (fork_is_found ?f - fork) (fork_is_grasped ?f - fork) (fork_is_placed ?f - fork) (appliance_at ?a - appliance ?l) (burger_spills ?b - burger))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1))
		:effect (and (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

    (:action find_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (table_is_found ?t))
	)

    (:action walk_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_is_found ?t) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (robot_near_table ?r))
	)

	(:action find_chair
		:parameters (?r - robot ?c - chair ?l - location)
		:precondition (and (robot_near_table ?r) (chair_at ?c ?l) (robot_at ?r ?l))
		:effect (and (chair_is_found ?c))
	)

    (:action pull_chair
		:parameters (?r - robot ?c - chair ?l - location)
		:precondition (and (chair_is_found ?c) (chair_at ?c ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (chair_is_pulled ?c))
	)

	(:action find_plate
		:parameters (?r - robot ?p - plate ?l - location)
		:precondition (and (plate_at ?p ?l) (robot_at ?r ?l))
		:effect (and (plate_is_found ?p))
	)

    (:action grasp_plate
		:parameters (?r - robot ?p - plate ?l - location)
		:precondition (and (plate_is_found ?p) (plate_at ?p ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (plate_is_grasped ?p) (not (hand_empty ?r)))
	)

    (:action move_plate
		:parameters (?r - robot ?p - plate ?l1 - location ?t - table ?l2 - location)
		:precondition (and (plate_is_grasped ?p) (plate_at ?p ?l1) (robot_at ?r ?l1) (table_at ?t ?l2))
		:effect (and (plate_at ?p ?l2) (not (plate_at ?p ?l1)) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action place_plate
		:parameters (?r - robot ?p - plate ?t - table ?l - location ?b - burger)
		:precondition (and (plate_is_grasped ?p) (plate_at ?p ?l) (table_at ?t ?l) (robot_at ?r ?l) (not (burger_spills ?b)))
		:effect (and (plate_is_placed ?p) (hand_empty ?r))
	)

	(:action find_burger
		:parameters (?r - robot ?b - burger ?l - location)
		:precondition (and (burger_at ?b ?l) (robot_at ?r ?l))
		:effect (and (burger_is_found ?b))
	)

	(:action grasp_burger
		:parameters (?r - robot ?b - burger ?l - location)
		:precondition (and (burger_is_found ?b) (burger_at ?b ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (burger_is_grasped ?b) (not (hand_empty ?r)))
	)

    (:action move_burger
		:parameters (?r - robot ?b - burger ?l1 - location ?p - plate ?l2 - location)
		:precondition (and (burger_is_grasped ?b) (burger_at ?b ?l1) (robot_at ?r ?l1) (plate_at ?p ?l2))
		:effect (and (burger_at ?b ?l2) (not (burger_at ?b ?l1)) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action place_burger
		:parameters (?r - robot ?b - burger ?p - plate ?l - location)
		:precondition (and (burger_is_grasped ?b) (burger_at ?b ?l) (plate_at ?p ?l) (plate_is_placed ?p) (robot_at ?r ?l))
		:effect (and (burger_is_placed ?b) (hand_empty ?r))
	)

    (:action find_fork
		:parameters (?r - robot ?f - fork ?l - location)
		:precondition (and (fork_at ?f ?l) (robot_at ?r ?l))
		:effect (and (fork_is_found ?f) (robot_at ?r ?l))
	)

    (:action grasp_fork
		:parameters (?r - robot ?f - fork ?l - location)
		:precondition (and (fork_is_found ?f) (fork_at ?f ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (fork_is_grasped ?f) (not (hand_empty ?r)))
	)

    (:action move_fork
		:parameters (?r - robot ?f - fork ?l1 - location ?p - plate ?l2 - location)
		:precondition (and (fork_is_grasped ?f) (fork_at ?f ?l1) (robot_at ?r ?l1) (plate_at ?p ?l2))
		:effect (and (fork_at ?f ?l2) (not (fork_at ?f ?l1)) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action place_fork
		:parameters (?r - robot ?f - fork ?p - plate ?l - location)
		:precondition (and (fork_is_grasped ?f) (fork_at ?f ?l) (plate_at ?p ?l) (plate_is_placed ?p) (robot_at ?r ?l))
		:effect (and (fork_is_placed ?f) (hand_empty ?r))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)