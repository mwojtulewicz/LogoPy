
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightRANDOMleftPLUSMINUSleftTIMESDIVIDEleftPOWERrightUMINUSBACK CLEAN COLON COMMA DIVIDE EQUALS FALSE FLOAT FORWARD GT GTE HIDE HOME IF IFELSE INT LBR LEFT LPAR LT LTE MAKE MINUS NE PENDOWN PENUP PLUS POWER PRINT QUOTE RANDOM RBR REPCOUNT REPEAT RESET RIGHT RPAR SETBC SETH SETPC SETPS SETX SETXY SETY SHOW SPEED STRING TIMES TRUE\n    statement_list : statement_list statement\n                   | statement\n    \n    statement : turtle_instruction\n              | repeat_statement\n              | if_statement\n              | ifelse_statement\n              | variable_declaration\n              | print_statement\n    \n    turtle_instruction : SETXY LBR expression COMMA expression RBR\n                       | FORWARD expression\n                       | BACK expression\n                       | RIGHT expression\n                       | LEFT expression\n                       | SETX expression\n                       | SETY expression\n                       | SETH expression\n                       | SPEED expression\n                       | SETPS expression\n                       | SETPC word\n                       | SETBC word\n                       | PENUP\n                       | PENDOWN\n                       | SHOW\n                       | HIDE\n                       | HOME\n                       | CLEAN\n                       | RESET\n    \n    repeat_statement : REPEAT expression LBR statement_list RBR \n    \n    if_statement : IF condition LBR statement_list RBR\n    \n    ifelse_statement : IFELSE condition LBR statement_list RBR LBR statement_list RBR\n    \n    variable_declaration : MAKE word expression\n    \n    print_statement : PRINT word\n    \n    print_statement : PRINT expression\n    \n    expression : INT\n               | FLOAT\n    \n    expression : name\n    \n    expression : REPCOUNT\n    \n    expression : LPAR expression RPAR\n    \n    expression : MINUS expression %prec UMINUS\n    \n    expression : RANDOM expression\n    \n    expression : expression TIMES expression\n               | expression DIVIDE expression\n               | expression PLUS expression\n               | expression MINUS expression\n               | expression POWER expression\n    \n    condition : TRUE\n              | FALSE\n    \n    condition : expression GT expression\n              | expression LT expression\n              | expression GTE expression\n              | expression LTE expression\n              | expression EQUALS expression\n              | expression NE expression\n    \n    word : QUOTE STRING\n    \n    name : COLON STRING\n    '
    
_lr_action_items = {'SETXY':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[9,9,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,9,9,9,-31,-41,-42,-43,-44,-45,-38,9,9,9,-28,-29,-9,9,9,-30,]),'FORWARD':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[10,10,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,10,10,10,-31,-41,-42,-43,-44,-45,-38,10,10,10,-28,-29,-9,10,10,-30,]),'BACK':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[11,11,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,11,11,11,-31,-41,-42,-43,-44,-45,-38,11,11,11,-28,-29,-9,11,11,-30,]),'RIGHT':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[12,12,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,12,12,12,-31,-41,-42,-43,-44,-45,-38,12,12,12,-28,-29,-9,12,12,-30,]),'LEFT':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[13,13,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,13,13,13,-31,-41,-42,-43,-44,-45,-38,13,13,13,-28,-29,-9,13,13,-30,]),'SETX':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[14,14,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,14,14,14,-31,-41,-42,-43,-44,-45,-38,14,14,14,-28,-29,-9,14,14,-30,]),'SETY':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[15,15,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,15,15,15,-31,-41,-42,-43,-44,-45,-38,15,15,15,-28,-29,-9,15,15,-30,]),'SETH':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[16,16,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,16,16,16,-31,-41,-42,-43,-44,-45,-38,16,16,16,-28,-29,-9,16,16,-30,]),'SPEED':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[17,17,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,17,17,17,-31,-41,-42,-43,-44,-45,-38,17,17,17,-28,-29,-9,17,17,-30,]),'SETPS':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[18,18,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,18,18,18,-31,-41,-42,-43,-44,-45,-38,18,18,18,-28,-29,-9,18,18,-30,]),'SETPC':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[19,19,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,19,19,19,-31,-41,-42,-43,-44,-45,-38,19,19,19,-28,-29,-9,19,19,-30,]),'SETBC':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[20,20,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,20,20,20,-31,-41,-42,-43,-44,-45,-38,20,20,20,-28,-29,-9,20,20,-30,]),'PENUP':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[21,21,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,21,21,21,-31,-41,-42,-43,-44,-45,-38,21,21,21,-28,-29,-9,21,21,-30,]),'PENDOWN':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[22,22,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,22,22,22,-31,-41,-42,-43,-44,-45,-38,22,22,22,-28,-29,-9,22,22,-30,]),'SHOW':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[23,23,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,23,23,23,-31,-41,-42,-43,-44,-45,-38,23,23,23,-28,-29,-9,23,23,-30,]),'HIDE':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[24,24,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,24,24,24,-31,-41,-42,-43,-44,-45,-38,24,24,24,-28,-29,-9,24,24,-30,]),'HOME':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[25,25,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,25,25,25,-31,-41,-42,-43,-44,-45,-38,25,25,25,-28,-29,-9,25,25,-30,]),'CLEAN':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[26,26,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,26,26,26,-31,-41,-42,-43,-44,-45,-38,26,26,26,-28,-29,-9,26,26,-30,]),'RESET':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[27,27,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,27,27,27,-31,-41,-42,-43,-44,-45,-38,27,27,27,-28,-29,-9,27,27,-30,]),'REPEAT':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[28,28,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,28,28,28,-31,-41,-42,-43,-44,-45,-38,28,28,28,-28,-29,-9,28,28,-30,]),'IF':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[29,29,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,29,29,29,-31,-41,-42,-43,-44,-45,-38,29,29,29,-28,-29,-9,29,29,-30,]),'IFELSE':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[30,30,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,30,30,30,-31,-41,-42,-43,-44,-45,-38,30,30,30,-28,-29,-9,30,30,-30,]),'MAKE':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[31,31,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,31,31,31,-31,-41,-42,-43,-44,-45,-38,31,31,31,-28,-29,-9,31,31,-30,]),'PRINT':([0,1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,75,76,83,84,86,87,88,89,90,91,92,93,100,102,103,105,106,107,108,],[32,32,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,32,32,32,-31,-41,-42,-43,-44,-45,-38,32,32,32,-28,-29,-9,32,32,-30,]),'$end':([1,2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,84,86,87,88,89,90,91,102,103,105,108,],[0,-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,-31,-41,-42,-43,-44,-45,-38,-28,-29,-9,-30,]),'RBR':([2,3,4,5,6,7,8,21,22,23,24,25,26,27,33,35,36,37,38,39,44,45,46,47,48,49,50,51,52,54,62,63,71,72,73,74,84,86,87,88,89,90,91,92,93,100,101,102,103,105,107,108,],[-2,-3,-4,-5,-6,-7,-8,-21,-22,-23,-24,-25,-26,-27,-1,-10,-34,-35,-36,-37,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-32,-33,-39,-40,-55,-54,-31,-41,-42,-43,-44,-45,-38,102,103,104,105,-28,-29,-9,108,-30,]),'LBR':([9,36,37,38,39,55,56,57,58,60,71,72,73,86,87,88,89,90,91,94,95,96,97,98,99,104,],[34,-34,-35,-36,-37,75,76,-46,-47,83,-39,-40,-55,-41,-42,-43,-44,-45,-38,-48,-49,-50,-51,-52,-53,106,]),'INT':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,74,77,78,79,80,81,82,85,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-54,36,36,36,36,36,36,36,]),'FLOAT':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,74,77,78,79,80,81,82,85,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-54,37,37,37,37,37,37,37,]),'REPCOUNT':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,74,77,78,79,80,81,82,85,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-54,39,39,39,39,39,39,39,]),'LPAR':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,74,77,78,79,80,81,82,85,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-54,40,40,40,40,40,40,40,]),'MINUS':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,55,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,80,81,82,84,85,86,87,88,89,90,91,94,95,96,97,98,99,101,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,68,-34,-35,-36,-37,41,41,41,68,68,68,68,68,68,68,68,68,68,41,68,68,41,41,41,41,41,68,-39,68,-55,-54,41,41,41,41,41,41,68,41,-41,-42,-43,-44,-45,-38,68,68,68,68,68,68,68,]),'RANDOM':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,74,77,78,79,80,81,82,85,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-54,42,42,42,42,42,42,42,]),'COLON':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,74,77,78,79,80,81,82,85,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-54,43,43,43,43,43,43,43,]),'QUOTE':([19,20,31,32,],[53,53,53,53,]),'TRUE':([29,30,],[57,57,]),'FALSE':([29,30,],[58,58,]),'TIMES':([35,36,37,38,39,44,45,46,47,48,49,50,51,55,59,63,64,70,71,72,73,84,86,87,88,89,90,91,94,95,96,97,98,99,101,],[65,-34,-35,-36,-37,65,65,65,65,65,65,65,65,65,65,65,65,65,-39,65,-55,65,-41,-42,65,65,-45,-38,65,65,65,65,65,65,65,]),'DIVIDE':([35,36,37,38,39,44,45,46,47,48,49,50,51,55,59,63,64,70,71,72,73,84,86,87,88,89,90,91,94,95,96,97,98,99,101,],[66,-34,-35,-36,-37,66,66,66,66,66,66,66,66,66,66,66,66,66,-39,66,-55,66,-41,-42,66,66,-45,-38,66,66,66,66,66,66,66,]),'PLUS':([35,36,37,38,39,44,45,46,47,48,49,50,51,55,59,63,64,70,71,72,73,84,86,87,88,89,90,91,94,95,96,97,98,99,101,],[67,-34,-35,-36,-37,67,67,67,67,67,67,67,67,67,67,67,67,67,-39,67,-55,67,-41,-42,-43,-44,-45,-38,67,67,67,67,67,67,67,]),'POWER':([35,36,37,38,39,44,45,46,47,48,49,50,51,55,59,63,64,70,71,72,73,84,86,87,88,89,90,91,94,95,96,97,98,99,101,],[69,-34,-35,-36,-37,69,69,69,69,69,69,69,69,69,69,69,69,69,-39,69,-55,69,69,69,69,69,-45,-38,69,69,69,69,69,69,69,]),'GT':([36,37,38,39,59,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,77,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'LT':([36,37,38,39,59,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,78,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'GTE':([36,37,38,39,59,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,79,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'LTE':([36,37,38,39,59,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,80,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'EQUALS':([36,37,38,39,59,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,81,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'NE':([36,37,38,39,59,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,82,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'COMMA':([36,37,38,39,64,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,85,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'RPAR':([36,37,38,39,70,71,72,73,86,87,88,89,90,91,],[-34,-35,-36,-37,91,-39,-40,-55,-41,-42,-43,-44,-45,-38,]),'STRING':([43,53,],[73,74,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,75,76,83,106,],[1,92,93,100,107,]),'statement':([0,1,75,76,83,92,93,100,106,107,],[2,33,2,2,2,33,33,33,2,33,]),'turtle_instruction':([0,1,75,76,83,92,93,100,106,107,],[3,3,3,3,3,3,3,3,3,3,]),'repeat_statement':([0,1,75,76,83,92,93,100,106,107,],[4,4,4,4,4,4,4,4,4,4,]),'if_statement':([0,1,75,76,83,92,93,100,106,107,],[5,5,5,5,5,5,5,5,5,5,]),'ifelse_statement':([0,1,75,76,83,92,93,100,106,107,],[6,6,6,6,6,6,6,6,6,6,]),'variable_declaration':([0,1,75,76,83,92,93,100,106,107,],[7,7,7,7,7,7,7,7,7,7,]),'print_statement':([0,1,75,76,83,92,93,100,106,107,],[8,8,8,8,8,8,8,8,8,8,]),'expression':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,77,78,79,80,81,82,85,],[35,44,45,46,47,48,49,50,51,55,59,59,63,64,70,71,72,84,86,87,88,89,90,94,95,96,97,98,99,101,]),'name':([10,11,12,13,14,15,16,17,18,28,29,30,32,34,40,41,42,61,65,66,67,68,69,77,78,79,80,81,82,85,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'word':([19,20,31,32,],[52,54,61,62,]),'condition':([29,30,],[56,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','logo.py',125),
  ('statement_list -> statement','statement_list',1,'p_statement_list','logo.py',126),
  ('statement -> turtle_instruction','statement',1,'p_statement','logo.py',136),
  ('statement -> repeat_statement','statement',1,'p_statement','logo.py',137),
  ('statement -> if_statement','statement',1,'p_statement','logo.py',138),
  ('statement -> ifelse_statement','statement',1,'p_statement','logo.py',139),
  ('statement -> variable_declaration','statement',1,'p_statement','logo.py',140),
  ('statement -> print_statement','statement',1,'p_statement','logo.py',141),
  ('turtle_instruction -> SETXY LBR expression COMMA expression RBR','turtle_instruction',6,'p_turtle_instruction','logo.py',147),
  ('turtle_instruction -> FORWARD expression','turtle_instruction',2,'p_turtle_instruction','logo.py',148),
  ('turtle_instruction -> BACK expression','turtle_instruction',2,'p_turtle_instruction','logo.py',149),
  ('turtle_instruction -> RIGHT expression','turtle_instruction',2,'p_turtle_instruction','logo.py',150),
  ('turtle_instruction -> LEFT expression','turtle_instruction',2,'p_turtle_instruction','logo.py',151),
  ('turtle_instruction -> SETX expression','turtle_instruction',2,'p_turtle_instruction','logo.py',152),
  ('turtle_instruction -> SETY expression','turtle_instruction',2,'p_turtle_instruction','logo.py',153),
  ('turtle_instruction -> SETH expression','turtle_instruction',2,'p_turtle_instruction','logo.py',154),
  ('turtle_instruction -> SPEED expression','turtle_instruction',2,'p_turtle_instruction','logo.py',155),
  ('turtle_instruction -> SETPS expression','turtle_instruction',2,'p_turtle_instruction','logo.py',156),
  ('turtle_instruction -> SETPC word','turtle_instruction',2,'p_turtle_instruction','logo.py',157),
  ('turtle_instruction -> SETBC word','turtle_instruction',2,'p_turtle_instruction','logo.py',158),
  ('turtle_instruction -> PENUP','turtle_instruction',1,'p_turtle_instruction','logo.py',159),
  ('turtle_instruction -> PENDOWN','turtle_instruction',1,'p_turtle_instruction','logo.py',160),
  ('turtle_instruction -> SHOW','turtle_instruction',1,'p_turtle_instruction','logo.py',161),
  ('turtle_instruction -> HIDE','turtle_instruction',1,'p_turtle_instruction','logo.py',162),
  ('turtle_instruction -> HOME','turtle_instruction',1,'p_turtle_instruction','logo.py',163),
  ('turtle_instruction -> CLEAN','turtle_instruction',1,'p_turtle_instruction','logo.py',164),
  ('turtle_instruction -> RESET','turtle_instruction',1,'p_turtle_instruction','logo.py',165),
  ('repeat_statement -> REPEAT expression LBR statement_list RBR','repeat_statement',5,'p_repeat_statement','logo.py',177),
  ('if_statement -> IF condition LBR statement_list RBR','if_statement',5,'p_if_statement','logo.py',183),
  ('ifelse_statement -> IFELSE condition LBR statement_list RBR LBR statement_list RBR','ifelse_statement',8,'p_ifelse_statement','logo.py',189),
  ('variable_declaration -> MAKE word expression','variable_declaration',3,'p_variable_declaration','logo.py',195),
  ('print_statement -> PRINT word','print_statement',2,'p_print_statement_word','logo.py',201),
  ('print_statement -> PRINT expression','print_statement',2,'p_print_statement_expression','logo.py',207),
  ('expression -> INT','expression',1,'p_expression_int_float','logo.py',213),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','logo.py',214),
  ('expression -> name','expression',1,'p_expression_var','logo.py',220),
  ('expression -> REPCOUNT','expression',1,'p_expression_repcount','logo.py',226),
  ('expression -> LPAR expression RPAR','expression',3,'p_expression_group','logo.py',232),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','logo.py',238),
  ('expression -> RANDOM expression','expression',2,'p_expression_random','logo.py',247),
  ('expression -> expression TIMES expression','expression',3,'p_expression','logo.py',253),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','logo.py',254),
  ('expression -> expression PLUS expression','expression',3,'p_expression','logo.py',255),
  ('expression -> expression MINUS expression','expression',3,'p_expression','logo.py',256),
  ('expression -> expression POWER expression','expression',3,'p_expression','logo.py',257),
  ('condition -> TRUE','condition',1,'p_condition_true_false','logo.py',263),
  ('condition -> FALSE','condition',1,'p_condition_true_false','logo.py',264),
  ('condition -> expression GT expression','condition',3,'p_condition','logo.py',270),
  ('condition -> expression LT expression','condition',3,'p_condition','logo.py',271),
  ('condition -> expression GTE expression','condition',3,'p_condition','logo.py',272),
  ('condition -> expression LTE expression','condition',3,'p_condition','logo.py',273),
  ('condition -> expression EQUALS expression','condition',3,'p_condition','logo.py',274),
  ('condition -> expression NE expression','condition',3,'p_condition','logo.py',275),
  ('word -> QUOTE STRING','word',2,'p_word','logo.py',281),
  ('name -> COLON STRING','name',2,'p_name','logo.py',287),
]
