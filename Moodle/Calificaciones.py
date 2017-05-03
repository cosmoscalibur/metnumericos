#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Quiz 1 con bonificación de mínimo flotante
Q1 = '([[Q1]]+[[B1]]/10)'
Q2 = '[[Q2]]'
Q3 = '[[Q3]]'
# Quiz 4 con bonificación de deducción de Taylor
Q4 = '([[Q4]]+[[B4]]/10)'
T1 = '[[T1]]'
T2 = '[[T2]]'
# Monitores de Semillero de monitores
MM = '[[MM]]'
# Semillero acádemico
SA = '[[SA]]'
# Semillero de monitores
SM = '[[SM]]'
# Equivalente de quiz 1 y 2 con escala de 0 a 10 (40% de seguimiento)
Q12_op1 = '(' + '+'.join([Q1, Q2]) + ')'
Q12_op2 = '(' + '+'.join([Q1, T1]) + ')'
Q12_op3 = '(' + '+'.join([Q2, T1]) + ')'
Q12_ops = [Q12_op1, Q12_op2, Q12_op3]
Q12 = 'max(' + ';'.join(Q12_ops) + ')'
# Equivalente de taller 1 y 2 con escala de 0 a 5 (20% seguimiento)
T12 = 'max(' + ';'.join([T1, T2]) + ')'
# Equivalente de Quiz 3 y 4 con escala de 0 a 10 (40% de seguimiento)
Q34_op1 = '(' + '+'.join([Q3, Q4]) + ')'
Q34_op2 = '(' + '+'.join([Q3, T12]) + ')'
Q34_op3 = '(' + '+'.join([Q4, T12]) + ')'
Q34_ops = [Q34_op1, Q34_op2, Q34_op3]
Q34 = 'max(' + ';'.join(Q34_ops) + ')'
# Seguimiento original (escala de 0 a 5)
SO = '(0,2*' + Q12 + '+0,2*' + Q34 + '+0,2*' \
    + T12 + ')'
# Seguimiento aprobado (escala de 0 a 5 con 3)
AS = 'floor('+SO+'/3)'
# Seguimiento con monitores y semillero academico (MM realmente es con 3,5)
MS = 'min(' + SO + '+' + AS + '*(' + MM \
    + '+' + SA + ');5)'
# Seguimiento con semillero de monitores
S50_ponderacion = '(0,9*' + MS + '+0,1*5*' \
    + AS + '*' + SM + ')'
S50_escala = '(0,9+0,1*' + AS + '*' + SM + ')'
S50 = S50_ponderacion + '/' + S50_escala
print('='+S50)

''' Formula Moodle Usada
=(0,9*min((0,2*max((([[Q1]]+[[B1]]/10)+[[Q2]]);(([[Q1]]+[[B1]]/10)+[[T1]]);([[Q2]]+[[T1]]))+0,2*max(([[Q3]]+([[Q4]]+[[B4]]/10));([[Q3]]+max([[T1]];[[T2]]));(([[Q4]]+[[B4]]/10)+max([[T1]];[[T2]])))+0,2*max([[T1]];[[T2]]))+floor((0,2*max((([[Q1]]+[[B1]]/10)+[[Q2]]);(([[Q1]]+[[B1]]/10)+[[T1]]);([[Q2]]+[[T1]]))+0,2*max(([[Q3]]+([[Q4]]+[[B4]]/10));([[Q3]]+max([[T1]];[[T2]]));(([[Q4]]+[[B4]]/10)+max([[T1]];[[T2]])))+0,2*max([[T1]];[[T2]]))/3)*([[MM]]+[[SA]]);5)+0,1*5*floor((0,2*max((([[Q1]]+[[B1]]/10)+[[Q2]]);(([[Q1]]+[[B1]]/10)+[[T1]]);([[Q2]]+[[T1]]))+0,2*max(([[Q3]]+([[Q4]]+[[B4]]/10));([[Q3]]+max([[T1]];[[T2]]));(([[Q4]]+[[B4]]/10)+max([[T1]];[[T2]])))+0,2*max([[T1]];[[T2]]))/3)*[[SM]])/(0,9+0,1*floor((0,2*max((([[Q1]]+[[B1]]/10)+[[Q2]]);(([[Q1]]+[[B1]]/10)+[[T1]]);([[Q2]]+[[T1]]))+0,2*max(([[Q3]]+([[Q4]]+[[B4]]/10));([[Q3]]+max([[T1]];[[T2]]));(([[Q4]]+[[B4]]/10)+max([[T1]];[[T2]])))+0,2*max([[T1]];[[T2]]))/3)*[[SM]])
'''
