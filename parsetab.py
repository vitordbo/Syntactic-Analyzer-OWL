
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND AT CARDINALITY CLASS COLON COMMA DATA_TYPE DISJOINTCLASSES EQ EQUIVALENTO EXACTLY GT HAS ID INDIVIDUALS IS LBRACE LBRACKET LPAREN LT MAX MIN NOT OF ONLY OR PROPERTY RBRACE RBRACKET RESERVED RPAREN SOME SUBCLASSOF THAT VALUE\n    ontologia : descricao_classes descricao_individuals\n    \n    descricao_classes : CLASS COLON ID subclasso_classes descricao_classes\n                      | CLASS COLON ID\n    \n    subclasso_classes : SUBCLASSOF COLON expressao_classes propriedades descricao_classes\n                      | SUBCLASSOF COLON expressao_classes propriedades\n                      | SUBCLASSOF COLON expressao_classes descricao_classes\n                      | SUBCLASSOF COLON expressao_classes\n                      | DISJOINTCLASSES COLON expressao_classes descricao_classes\n                      | DISJOINTCLASSES COLON expressao_classes\n                      | EQUIVALENTO COLON expressao_classes descricao_classes\n                      | EQUIVALENTO COLON expressao_classes\n                      | empty\n    \n    propriedades : expressao_classes descricao_classes propriedades\n                 | expressao_classes propriedades\n                 | empty\n    \n    descricao_individuals : INDIVIDUALS COLON ID COMMA ID descricao_individuals\n                          | INDIVIDUALS COLON ID\n                          | empty\n    \n    expressao_classes : ID\n                      | ID AND LPAREN expressao_classes COMMA expressao_classes RPAREN\n                      | ID AND LPAREN expressao_classes COMMA ID SOME ID RPAREN\n                      | ID AND LPAREN ID SOME ID RPAREN\n                      | ID AND LPAREN ID COMMA ID SOME ID RPAREN\n    \n    empty :\n    '
    
_lr_action_items = {'CLASS':([0,9,11,15,17,22,23,24,25,27,28,29,30,32,33,34,35,36,38,48,51,54,55,],[3,-3,3,-12,-2,3,-19,3,3,3,3,-6,-15,-8,-10,-24,-14,-4,-13,-22,-20,-23,-21,]),'$end':([1,2,4,6,9,10,17,21,26,],[0,-24,-1,-18,-3,-17,-2,-24,-16,]),'INDIVIDUALS':([2,9,17,21,],[5,-3,-2,5,]),'COLON':([3,5,12,13,14,],[7,8,18,19,20,]),'ID':([7,8,9,16,17,18,19,20,22,23,27,34,37,41,42,43,48,49,50,51,54,55,],[9,10,-3,21,-2,23,23,23,23,-19,23,23,39,44,45,46,-22,52,53,-20,-23,-21,]),'SUBCLASSOF':([9,],[12,]),'DISJOINTCLASSES':([9,],[13,]),'EQUIVALENTO':([9,],[14,]),'COMMA':([10,39,40,48,51,54,55,],[16,42,43,-22,-20,-23,-21,]),'AND':([23,39,46,],[31,31,31,]),'LPAREN':([31,],[37,]),'SOME':([39,45,46,],[41,49,50,]),'RPAREN':([44,46,47,48,51,52,53,54,55,],[48,-19,51,-22,-20,54,55,-23,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ontologia':([0,],[1,]),'descricao_classes':([0,11,22,24,25,27,28,],[2,17,29,32,33,34,36,]),'descricao_individuals':([2,21,],[4,26,]),'empty':([2,9,21,22,27,34,],[6,15,6,30,30,30,]),'subclasso_classes':([9,],[11,]),'expressao_classes':([18,19,20,22,27,34,37,43,],[22,24,25,27,27,27,40,47,]),'propriedades':([22,27,34,],[28,35,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ontologia","S'",1,None,None,None),
  ('ontologia -> descricao_classes descricao_individuals','ontologia',2,'p_ontologia','app.py',173),
  ('descricao_classes -> CLASS COLON ID subclasso_classes descricao_classes','descricao_classes',5,'p_descricao_classes','app.py',178),
  ('descricao_classes -> CLASS COLON ID','descricao_classes',3,'p_descricao_classes','app.py',179),
  ('subclasso_classes -> SUBCLASSOF COLON expressao_classes propriedades descricao_classes','subclasso_classes',5,'p_subclasso_classes','app.py',184),
  ('subclasso_classes -> SUBCLASSOF COLON expressao_classes propriedades','subclasso_classes',4,'p_subclasso_classes','app.py',185),
  ('subclasso_classes -> SUBCLASSOF COLON expressao_classes descricao_classes','subclasso_classes',4,'p_subclasso_classes','app.py',186),
  ('subclasso_classes -> SUBCLASSOF COLON expressao_classes','subclasso_classes',3,'p_subclasso_classes','app.py',187),
  ('subclasso_classes -> DISJOINTCLASSES COLON expressao_classes descricao_classes','subclasso_classes',4,'p_subclasso_classes','app.py',188),
  ('subclasso_classes -> DISJOINTCLASSES COLON expressao_classes','subclasso_classes',3,'p_subclasso_classes','app.py',189),
  ('subclasso_classes -> EQUIVALENTO COLON expressao_classes descricao_classes','subclasso_classes',4,'p_subclasso_classes','app.py',190),
  ('subclasso_classes -> EQUIVALENTO COLON expressao_classes','subclasso_classes',3,'p_subclasso_classes','app.py',191),
  ('subclasso_classes -> empty','subclasso_classes',1,'p_subclasso_classes','app.py',192),
  ('propriedades -> expressao_classes descricao_classes propriedades','propriedades',3,'p_properties','app.py',197),
  ('propriedades -> expressao_classes propriedades','propriedades',2,'p_properties','app.py',198),
  ('propriedades -> empty','propriedades',1,'p_properties','app.py',199),
  ('descricao_individuals -> INDIVIDUALS COLON ID COMMA ID descricao_individuals','descricao_individuals',6,'p_descricao_individuals','app.py',206),
  ('descricao_individuals -> INDIVIDUALS COLON ID','descricao_individuals',3,'p_descricao_individuals','app.py',207),
  ('descricao_individuals -> empty','descricao_individuals',1,'p_descricao_individuals','app.py',208),
  ('expressao_classes -> ID','expressao_classes',1,'p_expressao_classes','app.py',214),
  ('expressao_classes -> ID AND LPAREN expressao_classes COMMA expressao_classes RPAREN','expressao_classes',7,'p_expressao_classes','app.py',215),
  ('expressao_classes -> ID AND LPAREN expressao_classes COMMA ID SOME ID RPAREN','expressao_classes',9,'p_expressao_classes','app.py',216),
  ('expressao_classes -> ID AND LPAREN ID SOME ID RPAREN','expressao_classes',7,'p_expressao_classes','app.py',217),
  ('expressao_classes -> ID AND LPAREN ID COMMA ID SOME ID RPAREN','expressao_classes',9,'p_expressao_classes','app.py',218),
  ('empty -> <empty>','empty',0,'p_empty','app.py',229),
]
