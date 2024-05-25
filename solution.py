import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1527061415 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
               
    p_control = x_success / x_cnt
    p_test = y_success / y_cnt
    
    se = np.sqrt(p_control*(1-p_control)/x_cnt + p_test*(1-p_test)/y_cnt)
    
    # Z-статистика
    z = (p_control - p_test) / se
    
    # Критическое значение Z для уровня значимости 0.02
    critical_value = stats.norm.ppf(0.99) 
               
    return z > critical_value
