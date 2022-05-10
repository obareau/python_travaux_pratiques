from random import randint


class character():
	

	def __init__(self, **keywargs):
		self.name 	   	 = keywargs['name'] 	           if 'name' in keywargs 	  	else "Hero"
		self.lvl 	   	 = keywargs['lvl'] 	   	   if 'lvl' in keywargs 	  	else 1
		self.xp 	   	 = keywargs['xp'] 	   	   if 'xp' in keywargs 	   	  	else 0
		self.lvl_next  	         = keywargs['lvl_next']            if 'lvl_next' in keywargs  	        else 25
		self.str 	   	 = keywargs['str'] 	   	   if 'str' in keywargs 	  	else 1
		self.dex 	   	 = keywargs['dex']	   	   if 'dex' in keywargs 	  	else 1
		self.int 	   	 = keywargs['int']	   	   if 'int' in keywargs 	  	else 1
		self.hp 	   	 = keywargs['hp'] 	   	   if 'hp' in keywargs 	   	  	else 30
		self.atk	   	 = keywargs['atk'] 	   	   if 'atk' in keywargs 	  	else [5, 12]
		self.xp_reward 	         = keywargs['xp_reward']           if 'xp_reward' in keywargs 	        else 25
		self.loot_reward         = keywargs['loot_reward']         if 'loot_reward' in keywargs         else ("gold", 3)


	def update_level(self):
		
		if self.xp < self.lvl_next:
			return None
		
		new_str, new_dex, new_int = 0, 0, 0
		init_lvl = self.lvl

		# Updated code:
		# Differences in accessing values
		# char is now self
		# Class   vs  Dictionary
		# self.xp vs. char['xp']
		#  V           V
		# 25+         25+
		while self.xp >= self.lvl_next:
			self.lvl 	  += 1
			self.xp 	  = self.xp - self.lvl_next
			self.lvl_next     = round(self.lvl_next * 1.5)
			new_str 	  += 1
			new_dex 	  += 1
			new_int 	  += 1

		print()
		lvl_gained = self.lvl - init_lvl
		
		plural = "level"
		if 1 < lvl_gained:
			plural = "levels"

		print(f"{self.name} has gained {lvl_gained} {plural}!")
		print("====================")
		print(f"{self.name} reached level {self.lvl}!")

		# The assignment as I gave it last lesson:
		# str, dex, and int are now accessed through self
		print(f"STR {self.str} +{new_str}",
			  f"DEX {self.dex} +{new_dex}",
			  f"INT {self.int} +{new_int}"
			 )
		print("====================")
		print()

		self.str += new_str
		self.dex += new_dex
		self.int += new_int


	def attack(self):
		# *atk unppacks the list
		# atk = [5, 12]
		# *atk = 5, 12. the brackets are
		# dropped leaving a sequence of
		# integers instead of a list
		# so instead of randint(attacker.atk[0], attacker.atk[1])
		return randint(*self.atk)
	

	def take_damage(self, damage):
		self.hp = self.hp - damage
		# 0 is immutable so if we type
		# >= instead of = python will
		# give an error instead of
		# silently assigning health to zero
		if 0 >= self.hp:
			print(f"{self.name} has been slain")
			# attacker.xp += self.xp_reward
			# update_level(attacker)
			# input("-Press any Key to quit-")
			return self.xp_reward
		else:
			print(f"{self.name} takes {damage}!")

		return 0


	def is_alive(self):
		return 0 < self.hp


def combat(attacker, defender):
	xp_yield = defender.take_damage(attacker.attack())
	if xp_yield: # 0 is False
		attacker.xp += xp_yield
		attacker.update_level()


def game_loop(player, enemy):
	
	playing = True
	while playing:
		print('--------------------')
		cmd = input("Do you want to attack? yes/no: ").lower()
		if cmd in 'yes':
			combat(player, enemy)
		elif cmd in 'no':
			print(f"{enemy.name} takes the opportunity to attack!")
			combat(enemy, player)
		else:
			pass

		if False == enemy.is_alive():
			playing = False
		if False == player.is_alive():
			playing = False

hero = character(
		name="hero", lvl=1, xp=0, lvl_next=25, str=1, dex=1, int=1, hp=30, atk=[5, 12], xp_reward=25, loot_reward=("gold", 2)
		)
imp = character(
		name="imp", lvl=1, xp=0, lvl_next=25, str=1, dex=1, int=1, hp=30, atk=[5, 12], xp_reward=25, loot_reward=("gold", 6)
	       )

game_loop(hero, imp)