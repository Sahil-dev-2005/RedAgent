from victim import start_victim_chat
from attacker import get_attacker_response

victim_chat = start_victim_chat()

conversation_history=""

MAX_TURNS = 4 #one extra for initial message

for i in range(MAX_TURNS):
    if i==0:
        attack=get_attacker_response("Agent: Hello, TechCorp Support. How can I help you?")
    else:
        attack=get_attacker_response(conversation_history)
    print(f"Attacker: {attack}")
    response=victim_chat.send_message(attack)
    print(f"Agent: {response.text}")
    conversation_history+= f"User: {attack}\n"
    conversation_history+= f"Agent: {response.text}\n"
print("Simulation Complete.")
