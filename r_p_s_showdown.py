import random
import time
choice = {'3':'🧱','2':'📄','1':'✂️'}
outcome = '1'
while outcome == '1':
	random_choice_list = random.choice(list(choice))
	random_choice = int(random_choice_list)
	a = '---'
	player = (input('Please select your choice!\nFor Scissors press 1\n For Paper press 2\n For Rock press 3\n'))
	while True:
		if not player.isdigit() or int(player) > 3:
			player = (input('Please select your choice!\nFor Scissors press 1\n For Paper press 2\n For Rock press 3\n'))
		else:
			break
	player = int(player)
	for i in range(3,0,-1):
		print(f'{a}>{i}')
		a = a[:-1]
		time.sleep(1)
	print('Press enter now!')
	start_time = time.time()
	input()
	end_time = time.time()
	total_time = end_time - start_time
	first_emoji = str(random_choice)
	second_emoji = str(player)

	if total_time > 5:
		print('You didn\'t make it in time!')
		break
	if player == random_choice:
		print('Draw')
		print(f'Player: {choice[second_emoji]} vs Computer: {choice[first_emoji]}\n')
	elif player == 1 and random_choice == 2 or player == 3 and random_choice == 1 or \
		player == 2 and random_choice == 3:
		print('You are winner\n')
		print(f'Player: {choice[second_emoji]} vs Computer: {choice[first_emoji]}\n')
	else:
		print('You lose! \n')
		print(f'Player: {choice[second_emoji]} vs All mighty Computer: {choice[first_emoji]}\n')

	outcome = input('Wish to continue?\nTo continue press 1,\n To Exit press 2\n')