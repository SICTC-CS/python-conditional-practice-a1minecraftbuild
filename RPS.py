import random
cpu = random.randint(0,4)

if cpu == 0:
    cpu = "scissor"
if cpu == 1:
    cpu = "rock"
if cpu == 2:
    cpu = "paper"
if cpu == 3:
    cpu = "lizard"
if cpu == 4:
    cpu = "spock"

ui = int(input("scissor (0), rock (1), paper (2), lizard (3), spock (4) "))
if ui == 0:
    ui = "scissor"
if ui == 1:
    ui = "rock"
if ui == 2:
    ui = "paper"
if ui == 3:
    ui = "lizard"
if ui == 4:
    ui = "spock"


if ui == cpu:
    print("It's a tie!")
elif ui == "scissor" and (cpu == "spock" or cpu == "rock"):
    print(f"CPU wins with {cpu} against your {ui}!")

elif ui == "rock" and (cpu == "paper" or cpu == "spock"):
    print(f"CPU wins with {cpu} against your {ui}!")

elif ui == "paper" and (cpu == "scissor" or cpu == "lizard"):
    print(f"CPU wins with {cpu} against your {ui}!")

elif ui == "lizard" and (cpu == "rock" or cpu == "scissor"):
    print(f"CPU wins with {cpu} against your {ui}!")

elif ui == "spock" and (cpu == "lizard" or cpu == "paper"):
    print(f"CPU wins with {cpu} against your {ui}!")

elif cpu == "scissor" and (ui == "rock" or ui == "spock"):
    print(f"You win with {ui} against {cpu}!")

elif cpu == "rock" and (ui == "paper" or ui == "spock"):
    print(f"You win with {ui} against {cpu}!")

elif cpu == "paper" and (ui == "scissor" or ui == "lizard"):
    print(f"You win with {ui} against {cpu}!")

elif cpu == "lizard" and (ui == "rock" or ui == "scissor"):
    print(f"You win with {ui} against {cpu}!")

elif cpu == "spock" and (ui == "lizard" or ui == "paper"):
    print(f"You win with {ui} against {cpu}!")


else:
    print("DOES NOT COMPUTE")
