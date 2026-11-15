# Ahmet Olkun - Assignment 4

def check_session(idle_minutes, max_idle=30):
    if idle_minutes >= max_idle:
        return "SESSION_EXPIRED"
    return "SESSION_ACTIVE"
