#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def relationship_status(from_member, to_member, social_graph):

    if str(to_member) in list(dict(social_graph)[str(from_member)]["following"]):
        if str(from_member) in list(dict(social_graph)[str(to_member)]["following"]):
            return "friends"
        else:
            return "follower"
    else:
        if str(from_member) in list(dict(social_graph)[str(to_member)]["following"]):
            return "followed by"
        else:
            return "no relationship"


def tic_tac_toe(board):

    side_length=len(board)
    horizontal_win=[]
    for i in range(side_length):
        horizontal_win.append([])
    vertical_win=[]
    for i in range(side_length):
        vertical_win.append([])
    diagonal1_win=[]
    diagonal2_win=[]
    x=0
    
    for i in range(side_length):
        for j in range(side_length):    
            if board[i][j]=="":
                x+=1
                board[i][j]=str(x)
  
    try:
        for i in range(side_length):
            for j in range(side_length):
                horizontal_win[i]+=board[i][j]
                      
        for j in range(side_length):
            for i in range(side_length):
                vertical_win[j]+=board[i][j]
        
        for i in range(side_length):
            diagonal1_win+=board[i][i]
            diagonal2_win+=board[i][side_length-i-1]
        
        for i in range(side_length):
            if([horizontal_win[i][0]]*len(horizontal_win[i]) == horizontal_win[i]):
                return horizontal_win[i][0]
            elif([vertical_win[i][0]]*len(vertical_win[i]) == vertical_win[i]):
                return vertical_win[i][0]           
        if([diagonal1_win[0]]*len(diagonal1_win) == diagonal1_win):
            return diagonal1_win[0][0]
        if([diagonal2_win[0]]*len(diagonal2_win) == diagonal2_win):
            return diagonal2_win[0][0]
        else:
            return "NO WINNER"
    except:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):

    new_route=[]
    route_time=0
    j=0
    k=0
    
    for i in range(len(route_map)):
        new_route.append(list(route_map.keys())[i][0])

    if new_route.index(second_stop)-new_route.index(first_stop)<0:
        stops=len(new_route)+(new_route.index(second_stop)-new_route.index(first_stop))
    else:
        stops=(new_route.index(second_stop)-new_route.index(first_stop))

    
    for i in range(stops):

        pos_first=new_route.index(first_stop)+i
        pos_second=new_route.index(first_stop)+i+1
        if pos_second>=len(new_route):
            pos_second=0+j
            j+=1
        if pos_first>=len(new_route):
            pos_first=0+k
            k+=1
        route_time+=route_map[(new_route[pos_first],new_route[pos_second])]["travel_time_mins"]

    return route_time


# In[ ]:




