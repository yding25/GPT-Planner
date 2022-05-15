(define
	(domain dining)
	(:requirements :strips :typing)
	(:types robot vacuum table outlet location food utensil beverage furniture other appliance)
	(:predicates (robot_at ?r - robot ?l - location) (vacuum_at ?v - vacuum ?l - location) (table_at ?t - table ?l - location) (table_is_found ?t - table) (outlet_at ?o - outlet ?l - location) (vacuum_is_takenout ?v - vacuum) (vacuum_is_plugged ?v - vacuum) (vacuum_is_unplugged ?v - vacuum) (vacuum_is_on ?v - vacuum) (vacuum_is_off ?v - vacuum) (table_is_clean ?t - table) (appliance_at ?a - appliance ?l - location))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1))
		:effect (and (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

    (:action grasp_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (robot_at ?r ?l) (vacuum_at ?v ?l))
		:effect (and (vacuum_is_takenout ?v))
	)

	(:action find_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (table_is_found ?t))
	)

	(:action plug_vacuum
		:parameters (?r - robot ?v - vacuum ?o - outlet ?l - location)
		:precondition (and (vacuum_is_takenout ?v) (outlet_at ?o ?l) (robot_at ?r ?l) (vacuum_is_unplugged ?v))
		:effect (and (vacuum_is_plugged ?v) (not (vacuum_is_unplugged ?v)))
	)

	(:action turnon_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (vacuum_is_plugged ?v) (vacuum_is_off ?v))
		:effect (and (vacuum_is_on ?v) (not (vacuum_is_off ?v)))
	)

	(:action clean_area
		:parameters (?r - robot ?v - vacuum ?t - table ?l - location)
		:precondition (and (vacuum_is_on ?v) (table_is_found ?t) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (table_is_clean ?t))
	)

	(:action turnoff_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (vacuum_is_on ?v))
		:effect (and (vacuum_is_off ?v) (not (vacuum_is_on ?v)))
	)

	(:action unplug_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (vacuum_is_off ?v) (vacuum_is_plugged ?v))
		:effect (and (vacuum_is_unplugged ?v) (not (vacuum_is_plugged ?v)))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)