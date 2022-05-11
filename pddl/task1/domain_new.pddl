(define
	(domain dining_clean_floor)
	(:requirements :strips :typing)
	(:types robot vacuum table location food utensil beverage furniture other appliance)
	(:predicates (robot_at ?r - robot ?l - location) (vacuum_at ?v - vacuum ?l - location) (table_at ?t - table ?l - location) (table_is_clean ?t - table) (table_is_found ?t - table) (vacuum_is_takeout ?v - vacuum) (vacuum_is_on ?v - vacuum) (vacuum_is_off ?v - vacuum) (vacuum_is_plug ?v - vacuum) (vacuum_is_unplug ?v - vacuum) (appliance_at ?a - appliance ?l - location) (robot_cannot_reach_the_vacuum ?r - robot))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1))
		:effect (and (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action takeout_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (robot_at ?r ?l) (vacuum_at ?v ?l) (not (robot_cannot_reach_the_vacuum ?r)))
		:effect (and (vacuum_is_takeout ?v) (robot_at ?r ?l))
	)

	(:action find_table
		:parameters (?r - robot ?t - table ?l - location)
		:precondition (and (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (table_is_found ?t) (robot_at ?r ?l))
	)

	(:action plug_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (vacuum_is_takeout ?v) (robot_at ?r ?l) (vacuum_is_unplug ?v))
		:effect (and (vacuum_is_plug ?v) (not (vacuum_is_unplug ?v)) (vacuum_is_takeout ?v) (robot_at ?r ?l))
	)

	(:action turnon_vacuum
		:parameters (?r - robot ?v - vacuum ?l - location)
		:precondition (and (vacuum_is_plug ?v) (vacuum_is_takeout ?v) (vacuum_is_off ?v))
		:effect (and (vacuum_is_on ?v) (not (vacuum_is_off ?v)) (vacuum_is_takeout ?v) (robot_at ?r ?l))
	)

	(:action clean_table
		:parameters (?r - robot ?v - vacuum ?t - table ?l - location)
		:precondition (and (vacuum_is_on ?v) (table_is_found ?t) (table_at ?t ?l) (vacuum_is_takeout ?v) (robot_at ?r ?l))
		:effect (and (table_is_clean ?t) (vacuum_is_on ?v) (table_is_found ?t) (table_at ?t ?l) (vacuum_is_takeout ?v) (robot_at ?r ?l))
	)

	(:action turnoff_vacuum
		:parameters (?r - robot ?v - vacuum ?t - table ?l - location)
		:precondition (and (table_is_clean ?t) (vacuum_is_on ?v))
		:effect (and (vacuum_is_off ?v) (not (vacuum_is_on ?v)) (table_is_clean ?t))
	)

	(:action unplug_vacuum
		:parameters (?r - robot ?v - vacuum ?t - table ?l - location)
		:precondition (and (vacuum_is_off ?v) (not (vacuum_is_on ?v)) (table_is_clean ?t) (vacuum_is_plug ?v))
		:effect (and (vacuum_is_unplug ?v) (vacuum_is_off ?v))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)