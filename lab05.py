class BLPModel:
    LEVELS = {'U': 0, 'C': 1, 'S': 2, 'TS': 3}

    def __init__(self):
        self.subjects = {}
        self.objects = {}

    def add_subject(self, name, max_lvl, start_lvl):
        if self.LEVELS[start_lvl] > self.LEVELS[max_lvl]:
            return False
        self.subjects[name] = {'max': max_lvl, 'curr': start_lvl}
        return True

    def add_object(self, name, level):
        self.objects[name] = level

    def set_level(self, subj_name, new_lvl):
        subj = self.subjects[subj_name]
        # no lower below current, no raise above max
        if self.LEVELS[new_lvl] < self.LEVELS[subj['curr']]:
            return False, f"Cannot lower level to {new_lvl} from {subj['curr']}."
        if self.LEVELS[new_lvl] > self.LEVELS[subj['max']]:
            return False, f"Level {new_lvl} exceeds {subj_name}'s max level {subj['max']}."
        
        subj['curr'] = new_lvl
        return True, f"{subj_name} level set to {new_lvl}."

    def read(self, subj_name, obj_name):
        subj = self.subjects[subj_name]
        obj_lvl = self.objects[obj_name]
        
        # no read up (dynamic)
        if self.LEVELS[obj_lvl] > self.LEVELS[subj['max']]:
            return False, f"Access denied: {obj_name}'s level, {obj_lvl}, is above {subj_name}'s max level {subj['max']}."
        
        if self.LEVELS[obj_lvl] > self.LEVELS[subj['curr']]:
            subj['curr'] = obj_lvl 
            return True, f"Read allowed ({subj_name}'s level raised to {obj_lvl})."
        
        return True, "Read allowed."

    def write(self, subj_name, obj_name):
        subj = self.subjects[subj_name]
        obj_lvl = self.objects[obj_name]
        
        # no write down
        if self.LEVELS[subj['curr']] <= self.LEVELS[obj_lvl]:
            return True, "Write allowed."
        else:
            return False, f"Access denied: {subj_name} cannot write down to {obj_lvl} from {subj['curr']}."

    def display_system_state(self, scenario_label="Current State"):
        print(f"\n{'='*20} BLP State {scenario_label} {'='*20}")
        
        # subj
        print(f"{'TYPE':<10} | {'NAME':<12} | {'MAX LEVEL':<10} | {'CURR LEVEL':<10}")
        print("-" * 55)
        for name, attrs in self.subjects.items():
            print(f"{'Subject':<10} | {name:<12} | {attrs['max']:<10} | {attrs['curr']:<10}")
        
        print("\n" + "-" * 55)
        
        # obj
        print(f"{'TYPE':<10} | {'NAME':<12} | {'SECURITY LEVEL':<23}")
        print("-" * 55)
        for name, level in self.objects.items():
            print(f"{'Object':<10} | {name:<12} | {level:<23}")
        
        print(f"{'='*55}\n")