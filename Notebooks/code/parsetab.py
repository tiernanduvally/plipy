
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'E616A9CB0699353382FC4D58D9998368'
    
_lr_action_items = {'PRINT':([0,3,17,25,],[5,5,-4,-5,]),'STORE':([0,3,17,25,],[6,6,-4,-5,]),'$end':([0,1,2,3,4,7,17,25,],[-13,0,-1,-13,-3,-2,-4,-5,]),'+':([5,9,10,11,12,13,14,15,16,18,19,22,23,24,],[9,9,9,9,-9,-10,-11,-12,9,9,9,-6,-7,-8,]),'-':([5,9,10,11,12,13,14,15,16,18,19,22,23,24,],[10,10,10,10,-9,-10,-11,-12,10,10,10,-6,-7,-8,]),'(':([5,9,10,11,12,13,14,15,16,18,19,22,23,24,],[11,11,11,11,-9,-10,-11,-12,11,11,11,-6,-7,-8,]),'NAME':([5,6,9,10,11,12,13,14,15,16,18,19,22,23,24,],[14,16,14,14,14,-9,-10,-11,-12,14,14,14,-6,-7,-8,]),'NUMBER':([5,9,10,11,12,13,14,15,16,18,19,22,23,24,],[15,15,15,15,-9,-10,-11,-12,15,15,15,-6,-7,-8,]),';':([8,12,13,14,15,21,22,23,24,],[17,-9,-10,-11,-12,25,-6,-7,-8,]),')':([12,13,14,15,20,22,23,24,],[-9,-10,-11,-12,24,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'stmt_list':([0,3,],[2,7,]),'stmt':([0,3,],[3,3,]),'empty':([0,3,],[4,4,]),'exp':([5,9,10,11,16,18,19,],[8,18,19,20,21,22,23,]),'var':([5,9,10,11,16,18,19,],[12,12,12,12,12,12,12,]),'num':([5,9,10,11,16,18,19,],[13,13,13,13,13,13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> stmt_list','prog',1,'p_prog','exp1_interp_gram.py',7),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','exp1_interp_gram.py',12),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','exp1_interp_gram.py',13),
  ('stmt -> PRINT exp ;','stmt',3,'p_print_stmt','exp1_interp_gram.py',18),
  ('stmt -> STORE NAME exp ;','stmt',4,'p_store_stmt','exp1_interp_gram.py',22),
  ('exp -> + exp exp','exp',3,'p_arith_exp','exp1_interp_gram.py',27),
  ('exp -> - exp exp','exp',3,'p_arith_exp','exp1_interp_gram.py',28),
  ('exp -> ( exp )','exp',3,'p_arith_exp','exp1_interp_gram.py',29),
  ('exp -> var','exp',1,'p_var_exp','exp1_interp_gram.py',39),
  ('exp -> num','exp',1,'p_num_exp','exp1_interp_gram.py',43),
  ('var -> NAME','var',1,'p_var','exp1_interp_gram.py',47),
  ('num -> NUMBER','num',1,'p_num','exp1_interp_gram.py',51),
  ('empty -> <empty>','empty',0,'p_empty','exp1_interp_gram.py',55),
]
