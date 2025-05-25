import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

poetic_rhythm = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'poetic_rhythm')
line_breaks = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'line_breaks')
short_length = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'short_length')
rhyme = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'rhyme')
dialogue = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'dialogue')
plot = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'plot')
nature_desc = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'nature_desc')

literary_type = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'literary_type')

for var in [poetic_rhythm, line_breaks, short_length, rhyme, dialogue, plot, nature_desc]:
    var['low'] = fuzz.trimf(var.universe, [0, 0, 0.5])
    var['medium'] = fuzz.trimf(var.universe, [0, 0.5, 1])
    var['high'] = fuzz.trimf(var.universe, [0.5, 1, 1])

literary_type['poem'] = fuzz.trimf(literary_type.universe, [0.7, 0.9, 1.0])
literary_type['story'] = fuzz.trimf(literary_type.universe, [0.7, 0.9, 1.0])
literary_type['novel'] = fuzz.trimf(literary_type.universe, [0.7, 0.9, 1.0])
literary_type['poema'] = fuzz.trimf(literary_type.universe, [0.7, 0.9, 1.0])
literary_type['play'] = fuzz.trimf(literary_type.universe, [0.7, 0.9, 1.0])

# Правила (используем исправленные названия функций принадлежности)
rules = [
    ctrl.Rule(poetic_rhythm['high'] & line_breaks['high'] & short_length['high'], literary_type['poem']),
    ctrl.Rule(poetic_rhythm['high'] & line_breaks['high'] & rhyme['high'], literary_type['poem']),
    ctrl.Rule(poetic_rhythm['high'] & short_length['high'] & dialogue['low'], literary_type['poem']),
    
    ctrl.Rule(poetic_rhythm['low'] & short_length['high'] & plot['high'], literary_type['story']),
    ctrl.Rule(dialogue['high'] & short_length['high'] & line_breaks['low'], literary_type['story']),
    ctrl.Rule(poetic_rhythm['low'] & rhyme['low'] & short_length['high'], literary_type['story']),
    
    ctrl.Rule(short_length['low'] & plot['high'] & dialogue['high'], literary_type['novel']),
    ctrl.Rule(short_length['low'] & nature_desc['high'] & dialogue['high'], literary_type['novel']),
    ctrl.Rule(line_breaks['low'] & plot['high'] & short_length['low'], literary_type['novel']),
    
    ctrl.Rule(poetic_rhythm['high'] & short_length['low'] & rhyme['high'], literary_type['poema']),
    ctrl.Rule(line_breaks['high'] & short_length['low'] & rhyme['high'], literary_type['poema']),
    ctrl.Rule(poetic_rhythm['high'] & short_length['low'] & plot['high'], literary_type['poema']),
    
    ctrl.Rule(dialogue['high'] & line_breaks['high'] & plot['high'], literary_type['play']),
    ctrl.Rule(dialogue['high'] & nature_desc['high'] & plot['high'], literary_type['play']),
    ctrl.Rule(dialogue['high'] & short_length['low'] & plot['high'], literary_type['play'])
]

literary_ctrl = ctrl.ControlSystem(rules)
literary_detection = ctrl.ControlSystemSimulation(literary_ctrl)

literary_detection.input['poetic_rhythm'] = 0.9
literary_detection.input['line_breaks'] = 0.9
literary_detection.input['short_length'] = 0.8
literary_detection.input['rhyme'] = 0.7
literary_detection.input['dialogue'] = 0.1
literary_detection.input['plot'] = 0.3
literary_detection.input['nature_desc'] = 0.6

literary_detection.compute()

print("Результат классификации:", literary_detection.output['literary_type'])
literary_type.view(sim=literary_detection)