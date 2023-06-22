import math

def simple_model(dopamine):
    return 0.5 * dopamine

def complex_model(dopamine, sensitivity):
    return sensitivity * math.sqrt(dopamine)

def complex_model_with_stimulus(dopamine, sensitivity, stimulus):
    return sensitivity * math.sqrt(dopamine + stimulus)

def complex_model_with_tolerance(dopamine, sensitivity, stimulus, tolerance):
    return sensitivity * math.sqrt(dopamine + stimulus) / tolerance

def complex_model_with_serotonin(dopamine, sensitivity, stimulus, tolerance, serotonin):
    return sensitivity * math.sqrt(dopamine + stimulus) / tolerance + 0.3 * serotonin

# Test the models
dopamine = 50
sensitivity = 1
stimulus = 20
tolerance = 1.5
serotonin = 50

print("Simple model happiness:", simple_model(dopamine))
print("Complex model happiness:", complex_model(dopamine, sensitivity))
print("Complex model with stimulus happiness:", complex_model_with_stimulus(dopamine, sensitivity, stimulus))
print("Complex model with tolerance happiness:", complex_model_with_tolerance(dopamine, sensitivity, stimulus, tolerance))
print("Complex model with serotonin happiness:", complex_model_with_serotonin(dopamine, sensitivity, stimulus, tolerance, serotonin))
