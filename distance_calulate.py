t_server = 0
t_client = 0

t_client_send = t_client+291
t_client_rec = t_client + 238

t_server_send = t_server+362
t_server_rec = t_server+ 416
c = 34300

d = c/2*(t_server_rec-t_server_send+t_client_rec-t_client_send)/1000
print(d)
