# return hh:mm:ss
def sec_to_time(sec):
    h = str(sec // 3600)
    m = str((sec-int(h)*3600) // 60)
    s = str((sec-int(h)*3600) % 60)
    return (h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2))
