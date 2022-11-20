from rules import rules
from questions import questions

CONDITIONS = 0
RESPONSE = 1


class RETE():

    def __init__(self):
        self.currentKnowledge = []
        self.currentRules = rules

    def reset_state(self):
        self.currentKnowledge = []
        self.currentRules = rules

    def get_next_question(self, condition, conditionIsTrue):

        if(conditionIsTrue):
            self.currentKnowledge.append(condition)

        new_rules = []

        for rule in self.currentRules:

            if(conditionIsTrue and condition in rule[CONDITIONS]):
                new_rules.append(rule)

            if(not conditionIsTrue and not condition in rule[CONDITIONS]):
                new_rules.append(rule)

        self.currentRules = new_rules

        if(len(self.currentRules) == 1):
            return None

        for rule in self.currentRules:
            if(len(rule[CONDITIONS]) > len(self.currentKnowledge)):
                nextCondition = rule[CONDITIONS][len(self.currentRules) + 1]
                return (nextCondition, questions[nextCondition])

    def get_first_question(self, condition):
        self.reset_state()
        self.currentKnowledge.append(condition)

        new_rules = []

        for rule in self.currentRules:
            if(condition in rule[CONDITIONS]):
                new_rules.append(rule)

        self.currentRules = new_rules

        nextCondition = rule[CONDITIONS][0]
        return (nextCondition, questions[nextCondition])

    def get_solution(self):
        if(len(self.currentKnowledge) == 1):
            return self.currentRules[0][RESPONSE]
