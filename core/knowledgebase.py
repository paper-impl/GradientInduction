from __future__ import print_function, division, absolute_import
import numpy as np

class KnowledgeBase():
    def __init__(self, constants=["a","b"]):
        self.__constant = constants
        self.__extension = []

class ILP():
    '''
    a Inductive logic programming problem
    predicates are defined as strings, so as the constants
    '''
    def __init__(self, language_frame,background, positive, negative):
        '''
        :param language_frame
        :param background: list of atoms, the background knowledge
        :param positive: list of atoms, positive instances
        :param negative: list of atoms, negative instances
        '''
        self.__language_frame = language_frame
        self.__background = background
        self.__positive = positive
        self.__negative = negative

class LanguageFrame():
    def __init__(self, target, extension, constants):
        '''
        :param target: string, target predicate
        :param extension: list of atoms, extensional predicates
        :param constants: list of strings, constants
        '''
        self.target = target
        self.__extension = extension
        self.__constants = constants


class RuleTemplate():
    def __init__(self, variables_n, allow_intensional):
        '''
        :param variables_n: integer, number of
        existentially quantified variables allowed in the clause
        :param allow_intensional: boolean, whether the atoms in the body
         of the clause can use intensional predicates
        '''
        self.variables_n = variables_n
        self.allow_intensional = allow_intensional

class ProgramTemplate():
    def __init__(self, auxiliary, rules, forward_n):
        '''
        :param auxiliary: list of strings, set of auxiliary intensional predicates
        :param rules: dictionary of strings to tuples of rule templates,
        map from each intensional predicate to a pair of rule templates
        :param forward_n: integer4, max number of steps of forward chaining
        '''
        self.__auxiliary = auxiliary
        self.__rules = rules
        self.__forward_n = forward_n

