#!/usr/bin/python


knowledge_base = {
        'attributes': [
            {'name': 'edible', 'type': 'boolean'},
            {'name': 'price', 'type': 'continuous'},
            {'name': 'color', 'type': 'discrete', 'possible_values', ['yellow', 'white', 'orange']},
            ],
        'data' : [
            {'name': 'chair', 'edible': False, 'price': 50, 'color': 'yellow'},
            {'name': 'bed', 'edible': False, 'price': 250, 'color': 'orange'},
            {'name': 'spoon', 'edible': False, 'price': 0.5, 'color': 'white'},
            {'name': 'cheese', 'edible': True, 'price': 10, 'color': ['yellow', 'white', 'orange']},
            ]}

def pick_best_question():
    # iterate of all attributes
    best_value_for_best_attribute = None
    for attribute in knowledge_base['attributes']:
        best_value_for_any_attribute = None

        if attribute['type'] == 'boolean':
            true_count = 0
            for hypothesis in knowledge_base['data']:
                if (hypothesis[attribute['name']]):
                    true_count += 1
            if true_count >  len(knowledge_base['data']):
                best_value_for_any_attribute = True
            else:
                best_value_for_any_attribute = False

        if attribute['type'] == 'continuous':
            values = [value for value in knowledge_base['data'][attribute['name']]:
            sorted(values)
            best_value_for_any_attribute = values[len(values)/2]

        if attribute['type'] == 'discrete':
            best_count_so_far = 0
            for possible_value in attribute['possible_values']:
                equal_count = 0
                for hypothesis in knowledge_base['data']:
                    if (hypothesis[attribute['name']] == possible_value):
                        equal_count += 1
                if equal_count >  best_count_so_far:
                    best_value_for_any_attribute = possible_value
                    best_count_so_far = equal_count;


if __name__ == "__main__":
    current_hypotheses = knowledge_base['data']

    for i in range(1):
        pick_best_question()
        #result = ask_question()
        #if (result):
            #current_hypotheses = [h for h in current_hypotheses if matches(result
        #else:
