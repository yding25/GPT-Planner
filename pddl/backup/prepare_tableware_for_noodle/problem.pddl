(define
	(problem prepare_tableware)
	(:domain prepare_tableware_for_noodles)
	(:objects
		rob - robot
		
		noodles - food
		
		fork - tableware
		plate - tableware
		napkins - tableware
		
		kitchen - location
		dining - location
	)
	(:init (tableware_at napkins kitchen) (tableware_is_free napkins) (tableware_at fork kitchen) (tableware_is_free fork) (tableware_at plate kitchen) (tableware_is_free plate) (tableware_for_food plate) (food_at noodles kitchen) (food_is_free noodles) (robot_at dining) (hand_empty rob))
	(:goal (and (food_is_placed noodles plate) (tableware_at napkins dining) (tableware_at fork dining) (tableware_at plate dining)))
)
