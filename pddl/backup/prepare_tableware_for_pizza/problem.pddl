(define
	(problem prepare_tableware)
	(:domain prepare_tableware_for_pizza)
	(:objects
		rob - robot
		
		pizza - food
		
		pizza_cutter - tableware
		fork - tableware
		plate - tableware
		
		kitchen - location
		dining - location
	)
	(:init (tableware_at pizza_cutter kitchen) (tableware_is_free pizza_cutter) (tableware_at fork kitchen) (tableware_is_free fork) (tableware_at plate kitchen) (tableware_is_free plate) (tableware_for_food plate) (food_at pizza kitchen) (food_is_free pizza) (robot_at dining) (hand_empty rob))
	(:goal (and (food_is_placed pizza plate) (tableware_at pizza_cutter dining) (tableware_at fork dining) (tableware_at plate dining)))
)
