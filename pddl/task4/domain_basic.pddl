(define
	(domain dining)
	(:requirements :strips :typing)
	(:types robot cup table faucet location food utensil beverage furniture other appliance)
	(:predicates (robot_at ?r - robot ?l - location) (cup_at ?c - cup ?l - location) (faucet_at ?f - faucet ?l - location) (table_at ?t - table ?l - location) (faucet_is_found ?f - faucet) (faucet_is_on ?f - faucet) (faucet_is_off ?f - faucet) (cup_is_found ?c - cup) (cup_is_empty ?c - cup) (cup_is_held ?c - cup) (cup_is_filled ?c - cup) (cup_is_placed ?c - cup) (appliance_at ?a - appliance ?l - location))

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1))
		:effect (and (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action find_faucet
		:parameters (?r - robot ?f - faucet ?l - location)
		:precondition (and (faucet_at ?f ?l) (robot_at ?r ?l))
		:effect (and (faucet_is_found ?f))
	)

	(:action turnon_faucet
		:parameters (?r - robot ?f - faucet ?l - location)
		:precondition (and (faucet_is_found ?f) (faucet_is_off ?f) (faucet_at ?f ?l) (robot_at ?r ?l))
		:effect (and (faucet_is_on ?f) (not (faucet_is_off ?f)))
	)

	(:action find_cup
		:parameters (?r - robot ?c - cup ?l - location)
		:precondition (and (cup_at ?c ?l) (robot_at ?r ?l))
		:effect (and (cup_is_found ?c))
	)

	(:action hold_cup
		:parameters (?r - robot ?c - cup ?l - location)
		:precondition (and (cup_is_found ?c) (cup_at ?c ?l) (robot_at ?r ?l))
		:effect (and (cup_is_held ?c))
	)

	(:action fill_cup
		:parameters (?r - robot ?c - cup ?f - faucet ?l - location)
		:precondition (and (cup_is_held ?c) (cup_is_empty ?c) (faucet_is_on ?f) (faucet_at ?f ?l) (robot_at ?r ?l))
		:effect (and (cup_is_filled ?c))
	)

	(:action move_cup
		:parameters (?r - robot ?c - cup ?l1 - location ?l2 - location)
		:precondition (and (cup_is_held ?c) (robot_at ?r ?l1))
		:effect (and (cup_at ?c ?l2) (robot_at ?r ?l2) (not (cup_at ?c ?l1)) (not (robot_at ?r ?l1)))
	)

	(:action place_cup
		:parameters (?r - robot ?c - cup ?t - table ?l - location)
		:precondition (and (cup_is_filled ?c) (cup_is_held ?c) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (cup_is_placed ?c) (not (cup_is_held ?c)))
	)

	(:action turnoff_faucet
		:parameters (?r - robot ?f - faucet ?l - location)
		:precondition (and (faucet_is_on ?f) (faucet_at ?f ?l) (robot_at ?r ?l))
		:effect (and (faucet_is_off ?f) (not (faucet_is_on ?f)))
	)

	(:action operate
		:parameters (?r - robot ?a - appliance ?l1 - location ?l2 - location)
		:precondition (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
		:effect (and (appliance_at ?a ?l1) (robot_at ?r ?l1))
	)
)