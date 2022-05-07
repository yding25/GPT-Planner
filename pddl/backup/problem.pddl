(define
	(problem prepare_tableware)
	(:domain prepare_tableware_for_burger)
	(:objects
		rob - robot
		
		burger - food
		
		fork - tableware
		knife - tableware
		plate - tableware
		napkins - tableware
		
		kitchen - location
		dining - location
	)
	(:init (tableware_at knife kitchen) (tableware_is_free knife) (tableware_at napkins kitchen) (tableware_is_free napkins) (tableware_at fork kitchen) (tableware_is_free fork) (tableware_at plate kitchen) (tableware_is_free plate) (tableware_for_food plate) (food_at burger kitchen) (food_is_free burger) (robot_at dining) (hand_empty rob))
	(:goal (and (food_is_placed burger plate) (tableware_at knife dining) (tableware_at napkins dining) (tableware_at fork dining) (tableware_at plate dining)))
)
