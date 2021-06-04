
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftPOWERrightUMINUSBACK COLON DIVIDE EQUALS FALSE FLOAT FORWARD GT GTE IF INT LBR LEFT LPAR LT LTE MAKE MINUS NE PENDOWN PENUP PLUS POWER PRINT QUOTE RBR REPEAT RIGHT RPAR STRING TIMES TRUE\n    statement_list : statement_list statement\n                   | statement\n    \n    statement : turtle_instruction\n              | repeat_statement\n              | if_statement\n              | variable_declaration\n              | print_statement\n    \n    turtle_instruction : FORWARD expression\n                       | BACK expression\n                       | RIGHT expression\n                       | LEFT expression\n                       | PENUP\n                       | PENDOWN\n    \n    repeat_statement : REPEAT expression LBR statement_list RBR \n    \n    if_statement : IF condition LBR statement_list RBR\n    \n    variable_declaration : MAKE word expression\n    \n    print_statement : PRINT word\n    \n    print_statement : PRINT expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : name\n    \n    expression : LPAR expression RPAR\n    \n    expression : MINUS expression %prec UMINUS\n    \n    expression : expression TIMES expression\n               | expression DIVIDE expression\n               | expression PLUS expression\n               | expression MINUS expression\n               | expression POWER expression\n    \n    condition : TRUE\n              | FALSE\n    \n    condition : expression GT expression\n              | expression LT expression\n              | expression GTE expression\n              | expression LTE expression\n              | expression EQUALS expression\n              | expression NE expression\n    \n    word : QUOTE STRING\n    \n    name : COLON STRING\n    '
    
_lr_action_items = {'FORWARD':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[8,8,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,8,8,-16,-37,-24,-25,-26,-27,-28,-22,8,8,-14,-15,]),'BACK':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[9,9,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,9,9,-16,-37,-24,-25,-26,-27,-28,-22,9,9,-14,-15,]),'RIGHT':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[10,10,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,10,10,-16,-37,-24,-25,-26,-27,-28,-22,10,10,-14,-15,]),'LEFT':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[11,11,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,11,11,-16,-37,-24,-25,-26,-27,-28,-22,11,11,-14,-15,]),'PENUP':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[12,12,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,12,12,-16,-37,-24,-25,-26,-27,-28,-22,12,12,-14,-15,]),'PENDOWN':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[13,13,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,13,13,-16,-37,-24,-25,-26,-27,-28,-22,13,13,-14,-15,]),'REPEAT':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[14,14,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,14,14,-16,-37,-24,-25,-26,-27,-28,-22,14,14,-14,-15,]),'IF':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[15,15,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,15,15,-16,-37,-24,-25,-26,-27,-28,-22,15,15,-14,-15,]),'MAKE':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[16,16,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,16,16,-16,-37,-24,-25,-26,-27,-28,-22,16,16,-14,-15,]),'PRINT':([0,1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,46,47,54,55,56,57,58,59,60,61,62,63,70,71,],[17,17,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,17,17,-16,-37,-24,-25,-26,-27,-28,-22,17,17,-14,-15,]),'$end':([1,2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,54,55,56,57,58,59,60,61,70,71,],[0,-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,-16,-37,-24,-25,-26,-27,-28,-22,-14,-15,]),'RBR':([2,3,4,5,6,7,12,13,18,19,20,21,22,26,27,28,36,37,44,45,54,55,56,57,58,59,60,61,62,63,70,71,],[-2,-3,-4,-5,-6,-7,-12,-13,-1,-8,-19,-20,-21,-9,-10,-11,-17,-18,-23,-38,-16,-37,-24,-25,-26,-27,-28,-22,70,71,-14,-15,]),'INT':([8,9,10,11,14,15,17,23,24,34,38,39,40,41,42,48,49,50,51,52,53,55,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-37,]),'FLOAT':([8,9,10,11,14,15,17,23,24,34,38,39,40,41,42,48,49,50,51,52,53,55,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-37,]),'LPAR':([8,9,10,11,14,15,17,23,24,34,38,39,40,41,42,48,49,50,51,52,53,55,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-37,]),'MINUS':([8,9,10,11,14,15,17,19,20,21,22,23,24,26,27,28,29,33,34,37,38,39,40,41,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,66,67,68,69,],[24,24,24,24,24,24,24,41,-19,-20,-21,24,24,41,41,41,41,41,24,41,24,24,24,24,24,41,-23,-38,24,24,24,24,24,24,41,-37,-24,-25,-26,-27,-28,-22,41,41,41,41,41,41,]),'COLON':([8,9,10,11,14,15,17,23,24,34,38,39,40,41,42,48,49,50,51,52,53,55,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-37,]),'TRUE':([15,],[31,]),'FALSE':([15,],[32,]),'QUOTE':([16,17,],[35,35,]),'TIMES':([19,20,21,22,26,27,28,29,33,37,43,44,45,54,56,57,58,59,60,61,64,65,66,67,68,69,],[38,-19,-20,-21,38,38,38,38,38,38,38,-23,-38,38,-24,-25,38,38,-28,-22,38,38,38,38,38,38,]),'DIVIDE':([19,20,21,22,26,27,28,29,33,37,43,44,45,54,56,57,58,59,60,61,64,65,66,67,68,69,],[39,-19,-20,-21,39,39,39,39,39,39,39,-23,-38,39,-24,-25,39,39,-28,-22,39,39,39,39,39,39,]),'PLUS':([19,20,21,22,26,27,28,29,33,37,43,44,45,54,56,57,58,59,60,61,64,65,66,67,68,69,],[40,-19,-20,-21,40,40,40,40,40,40,40,-23,-38,40,-24,-25,-26,-27,-28,-22,40,40,40,40,40,40,]),'POWER':([19,20,21,22,26,27,28,29,33,37,43,44,45,54,56,57,58,59,60,61,64,65,66,67,68,69,],[42,-19,-20,-21,42,42,42,42,42,42,42,-23,-38,42,42,42,42,42,-28,-22,42,42,42,42,42,42,]),'LBR':([20,21,22,29,30,31,32,44,45,56,57,58,59,60,61,64,65,66,67,68,69,],[-19,-20,-21,46,47,-29,-30,-23,-38,-24,-25,-26,-27,-28,-22,-31,-32,-33,-34,-35,-36,]),'GT':([20,21,22,33,44,45,56,57,58,59,60,61,],[-19,-20,-21,48,-23,-38,-24,-25,-26,-27,-28,-22,]),'LT':([20,21,22,33,44,45,56,57,58,59,60,61,],[-19,-20,-21,49,-23,-38,-24,-25,-26,-27,-28,-22,]),'GTE':([20,21,22,33,44,45,56,57,58,59,60,61,],[-19,-20,-21,50,-23,-38,-24,-25,-26,-27,-28,-22,]),'LTE':([20,21,22,33,44,45,56,57,58,59,60,61,],[-19,-20,-21,51,-23,-38,-24,-25,-26,-27,-28,-22,]),'EQUALS':([20,21,22,33,44,45,56,57,58,59,60,61,],[-19,-20,-21,52,-23,-38,-24,-25,-26,-27,-28,-22,]),'NE':([20,21,22,33,44,45,56,57,58,59,60,61,],[-19,-20,-21,53,-23,-38,-24,-25,-26,-27,-28,-22,]),'RPAR':([20,21,22,43,44,45,56,57,58,59,60,61,],[-19,-20,-21,61,-23,-38,-24,-25,-26,-27,-28,-22,]),'STRING':([25,35,],[45,55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,46,47,],[1,62,63,]),'statement':([0,1,46,47,62,63,],[2,18,2,2,18,18,]),'turtle_instruction':([0,1,46,47,62,63,],[3,3,3,3,3,3,]),'repeat_statement':([0,1,46,47,62,63,],[4,4,4,4,4,4,]),'if_statement':([0,1,46,47,62,63,],[5,5,5,5,5,5,]),'variable_declaration':([0,1,46,47,62,63,],[6,6,6,6,6,6,]),'print_statement':([0,1,46,47,62,63,],[7,7,7,7,7,7,]),'expression':([8,9,10,11,14,15,17,23,24,34,38,39,40,41,42,48,49,50,51,52,53,],[19,26,27,28,29,33,37,43,44,54,56,57,58,59,60,64,65,66,67,68,69,]),'name':([8,9,10,11,14,15,17,23,24,34,38,39,40,41,42,48,49,50,51,52,53,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'condition':([15,],[30,]),'word':([16,17,],[34,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','grammar.py',91),
  ('statement_list -> statement','statement_list',1,'p_statement_list','grammar.py',92),
  ('statement -> turtle_instruction','statement',1,'p_statement','grammar.py',102),
  ('statement -> repeat_statement','statement',1,'p_statement','grammar.py',103),
  ('statement -> if_statement','statement',1,'p_statement','grammar.py',104),
  ('statement -> variable_declaration','statement',1,'p_statement','grammar.py',105),
  ('statement -> print_statement','statement',1,'p_statement','grammar.py',106),
  ('turtle_instruction -> FORWARD expression','turtle_instruction',2,'p_turtle_instruction','grammar.py',112),
  ('turtle_instruction -> BACK expression','turtle_instruction',2,'p_turtle_instruction','grammar.py',113),
  ('turtle_instruction -> RIGHT expression','turtle_instruction',2,'p_turtle_instruction','grammar.py',114),
  ('turtle_instruction -> LEFT expression','turtle_instruction',2,'p_turtle_instruction','grammar.py',115),
  ('turtle_instruction -> PENUP','turtle_instruction',1,'p_turtle_instruction','grammar.py',116),
  ('turtle_instruction -> PENDOWN','turtle_instruction',1,'p_turtle_instruction','grammar.py',117),
  ('repeat_statement -> REPEAT expression LBR statement_list RBR','repeat_statement',5,'p_repeat_statement','grammar.py',126),
  ('if_statement -> IF condition LBR statement_list RBR','if_statement',5,'p_if_statement','grammar.py',132),
  ('variable_declaration -> MAKE word expression','variable_declaration',3,'p_variable_declaration','grammar.py',138),
  ('print_statement -> PRINT word','print_statement',2,'p_print_statement_word','grammar.py',144),
  ('print_statement -> PRINT expression','print_statement',2,'p_print_statement_expression','grammar.py',150),
  ('expression -> INT','expression',1,'p_expression_int_float','grammar.py',156),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','grammar.py',157),
  ('expression -> name','expression',1,'p_expression_var','grammar.py',163),
  ('expression -> LPAR expression RPAR','expression',3,'p_expression_group','grammar.py',169),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','grammar.py',175),
  ('expression -> expression TIMES expression','expression',3,'p_expression','grammar.py',184),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','grammar.py',185),
  ('expression -> expression PLUS expression','expression',3,'p_expression','grammar.py',186),
  ('expression -> expression MINUS expression','expression',3,'p_expression','grammar.py',187),
  ('expression -> expression POWER expression','expression',3,'p_expression','grammar.py',188),
  ('condition -> TRUE','condition',1,'p_condition_true_false','grammar.py',194),
  ('condition -> FALSE','condition',1,'p_condition_true_false','grammar.py',195),
  ('condition -> expression GT expression','condition',3,'p_condition','grammar.py',202),
  ('condition -> expression LT expression','condition',3,'p_condition','grammar.py',203),
  ('condition -> expression GTE expression','condition',3,'p_condition','grammar.py',204),
  ('condition -> expression LTE expression','condition',3,'p_condition','grammar.py',205),
  ('condition -> expression EQUALS expression','condition',3,'p_condition','grammar.py',206),
  ('condition -> expression NE expression','condition',3,'p_condition','grammar.py',207),
  ('word -> QUOTE STRING','word',2,'p_word','grammar.py',213),
  ('name -> COLON STRING','name',2,'p_name','grammar.py',219),
]