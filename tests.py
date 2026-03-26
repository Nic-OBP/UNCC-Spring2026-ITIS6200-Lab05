from lab05 import BLPModel

def get_initialized_system():
    blp = BLPModel()
    # subjects: name, max, start
    blp.add_subject("Alice", "S", "U")
    blp.add_subject("Bob", "C", "C")
    blp.add_subject("Eve", "U", "U")
    # objects: name, level
    blp.add_object("pub.txt", "U")
    blp.add_object("emails.txt", "C")
    blp.add_object("username.txt", "S")
    blp.add_object("password.txt", "TS")
    return blp

def execute_scenario(case_num, actions):
    blp = get_initialized_system()
    print(f"{'='*20} SCENARIO {case_num} {'='*20}")
    
    for action in actions:
        subj, act_type, target = action
        if act_type == "read":
            success, msg = blp.read(subj, target)
        elif act_type == "write":
            success, msg = blp.write(subj, target)
        elif act_type == "set":
            success, msg = blp.set_level(subj, target)
        
        status = "ALLOWED" if success else "DENIED"
        print(f"Action: {subj} attempts to {act_type} {target}")
        print(f"Result: {status} - {msg}")
        print("-" * 55)
    blp.display_system_state(case_num)
    print("\n")

# tests
scenarios = {
    1:  [("Alice", "read", "emails.txt")],
    2:  [("Alice", "read", "password.txt")],
    3:  [("Eve", "read", "pub.txt")],
    4:  [("Eve", "read", "emails.txt")],
    5:  [("Bob", "read", "password.txt")],
    6:  [("Alice", "read", "emails.txt"), ("Alice", "write", "pub.txt")],
    7:  [("Alice", "read", "emails.txt"), ("Alice", "write", "password.txt")],
    8:  [("Alice", "read", "emails.txt"), ("Alice", "write", "emails.txt"), 
         ("Alice", "read", "username.txt"), ("Alice", "write", "emails.txt")],
    9:  [("Alice", "read", "username.txt"), ("Alice", "write", "emails.txt"), 
         ("Alice", "read", "password.txt"), ("Alice", "write", "password.txt")],
    10: [("Alice", "read", "pub.txt"), ("Alice", "write", "emails.txt"), ("Bob", "read", "emails.txt")],
    11: [("Alice", "read", "pub.txt"), ("Alice", "write", "username.txt"), ("Bob", "read", "username.txt")],
    12: [("Alice", "read", "pub.txt"), ("Alice", "write", "password.txt"), ("Bob", "read", "password.txt")],
    13: [("Alice", "read", "pub.txt"), ("Alice", "write", "emails.txt"), ("Eve", "read", "emails.txt")],
    14: [("Alice", "read", "emails.txt"), ("Alice", "write", "pub.txt"), ("Eve", "read", "pub.txt")],
    15: [("Alice", "set", "S"), ("Alice", "read", "username.txt")],
    16: [("Alice", "read", "emails.txt"), ("Alice", "set", "U"), ("Alice", "write", "pub.txt"), ("Eve", "read", "pub.txt")],
    17: [("Alice", "read", "username.txt"), ("Alice", "set", "C"), ("Alice", "write", "emails.txt"), ("Eve", "read", "emails.txt")],
    18: [("Eve", "read", "pub.txt"), ("Eve", "read", "emails.txt")]
}

if __name__ == "__main__":
    for case_num, actions in scenarios.items():
        execute_scenario(case_num, actions)