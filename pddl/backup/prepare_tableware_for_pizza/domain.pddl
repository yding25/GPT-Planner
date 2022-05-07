(define
	(domain prepare_tableware_for_pizza)
	(:requirements :strips :typing)
	(:types robot food tableware location)
	(:predicates
		(robot_at ?l - location)
		(tableware_at ?t - tableware ?l - location)
		(food_at ?f - food ?l - location)

        (tableware_is_free ?t - tableware)
        (tableware_is_holding ?t - tableware)
        (tableware_is_placed ?t - tableware ?l - location)

        (tableware_for_food ?t - tableware)

        (food_is_free ?f - food)
        (food_is_holding ?f - food)
		(food_is_placed ?f - food ?t - tableware)

		(hand_empty ?r - robot)
	)

	(:action navigate
		:parameters (?r - robot ?l1 - location ?l2 - location)
		:precondition (and (robot_at ?l1) (hand_empty ?r))
		:effect (and (robot_at ?l2) (hand_empty ?r))
	)

	(:action pickup_tableware
		:parameters (?r - robot ?t - tableware ?l - location)
		:precondition (and (tableware_at ?t ?l) (tableware_is_free ?t) (robot_at ?l) (hand_empty ?r))
		:effect (and (tableware_is_holding ?t) (tableware_at ?t ?l) (not (tableware_is_free ?t)) (robot_at ?l) (not (hand_empty ?r)))
	)

	(:action move_tableware
		:parameters (?r - robot ?t - tableware ?l1 - location ?l2 - location)
		:precondition (and (tableware_is_holding ?t) (robot_at ?l1))
		:effect (and (tableware_is_holding ?t) (tableware_at ?t ?l2) (robot_at ?l2)  (not (hand_empty ?r)))
	)

	(:action putdown_tablware
		:parameters (?r - robot ?t - tableware ?l - location)
		:precondition (and (tableware_is_holding ?t) (robot_at ?l))
		:effect (and (tableware_is_placed ?t ?l) (tableware_is_free ?t) (robot_at ?l) (hand_empty ?r))
	)

	(:action pickup_food
		:parameters (?r - robot ?f - food ?l - location)
		:precondition (and (food_at ?f ?l) (food_is_free ?f) (robot_at ?l) (hand_empty ?r))
		:effect (and (food_is_holding ?f) (food_at ?f ?l) (robot_at ?l) (not (hand_empty ?r)))
	)

	(:action move_food
		:parameters (?r - robot ?f - food ?l1 - location ?l2 - location)
		:precondition (and (food_is_holding ?f) (robot_at ?l1))
		:effect (and (food_is_holding ?f) (food_at ?f ?l2) (robot_at ?l2) (not (hand_empty ?r)))
	)

	(:action putdown_food
		:parameters (?r - robot ?f - food ?t - tableware ?l - location)
		:precondition (and (food_is_holding ?f) (robot_at ?l) (tableware_is_placed ?t ?l) (tableware_for_food ?t))
		:effect (and (food_is_placed ?f ?t) (robot_at ?l) (hand_empty ?r))
	)
)
