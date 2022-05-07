(define
	(domain dining_drink_water)
	(:requirements :strips :typing)
	(:types robot cup table bowl faucet location)
	(:predicates
		(robot_at ?r - robot ?l - location)
		(cup_at ?c - cup ?l - location)
		(faucet_at ?f - faucet ?l - location)
		(table_at ?t - table ?l - location)
		(bowl_at ?b - bowl ?l - location)
		
		(hand_empty ?r - robot)
		
		(faucet_is_found ?f - faucet)
		(faucet_is_turned_on ?f - faucet)
		(faucet_is_turned_off ?f - faucet)

		(cup_is_found ?c - cup)
		(cup_is_empty ?c - cup)
		(cup_is_holding ?c - cup)
		(cup_is_filled ?c - cup)
		(cup_is_on_table ?c - cup ?t - table)
		
		(bowl_is_empty ?b - bowl)
		
		; added constraint: (cup_is_broken ?c - cup)
		(cup_is_broken ?c - cup)
		
	)

	(:action walk
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?r ?l1) (hand_empty ?r))
		:effect (and (robot_at ?r ?l2) (hand_empty ?r) (not (robot_at ?r ?l1)))
	)

	(:action find_faucet
		:parameters (?r - robot ?f - faucet ?l - location)
		:precondition (and (faucet_at ?f ?l) (robot_at ?r ?l))
		:effect (and (faucet_is_found ?f) (robot_at ?r ?l))
	)

	(:action turn_on_faucet
		:parameters (?r - robot ?f - faucet ?l - location)
		:precondition (and (faucet_at ?f ?l) (faucet_is_found ?f) (faucet_is_turned_off ?f) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (faucet_is_turned_on ?f) (robot_at ?r ?l) (hand_empty ?r) (not (faucet_is_turned_off ?f)))
	)

	(:action find_cup
		:parameters (?r - robot ?c - cup ?l - location)
		; added constraint: (not (cup_is_broken ?c))
		:precondition (and (cup_at ?c ?l) (robot_at ?r ?l) (not (cup_is_broken ?c)))
		:effect (and (cup_is_found ?c) (robot_at ?r ?l))
	)

	(:action hold_cup
		:parameters (?r - robot ?c - cup ?l - location)
		:precondition (and (cup_at ?c ?l) (cup_is_found ?c) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (cup_is_holding ?c) (cup_at ?c ?l) (robot_at ?r ?l) (not (hand_empty ?r)))
	)

	(:action fill_cup_with_water
		:parameters (?r - robot ?c - cup ?f - faucet ?l - location)
		:precondition (and (cup_is_holding ?c) (cup_is_empty ?c) (faucet_is_turned_on ?f) (faucet_at ?f ?l) (robot_at ?r ?l))
		:effect (and (cup_is_filled ?c) (cup_is_holding ?c) (robot_at ?r ?l))
	)

	(:action move_cup
		:parameters (?r - robot ?c - cup ?l1 - location ?l2 - location)
		:precondition (and (cup_is_filled ?c) (cup_is_holding ?c) (robot_at ?r ?l1))
		:effect (and (cup_is_filled ?c) (cup_is_holding ?c) (cup_at ?c ?l2) (robot_at ?r ?l2) (not (robot_at ?r ?l1)))
	)

	(:action put_cup_on_table
		:parameters (?r - robot ?c - cup ?t - table ?l - location)
		:precondition (and (cup_is_filled ?c) (cup_is_holding ?c) (table_at ?t ?l) (robot_at ?r ?l))
		:effect (and (cup_is_filled ?c) (cup_is_on_table ?c ?t) (robot_at ?r ?l) (hand_empty ?r) (not (cup_is_holding ?c)))
	)

	(:action turn_off_faucet
		:parameters (?r - robot ?f - faucet ?l - location)
		:precondition (and (faucet_is_turned_on ?f) (faucet_at ?f ?l) (robot_at ?r ?l) (hand_empty ?r))
		:effect (and (faucet_is_turned_off ?f) (not (faucet_is_turned_on ?f)) (robot_at ?r ?l) (hand_empty ?r))
	)
)
