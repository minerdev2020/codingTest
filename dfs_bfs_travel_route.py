from copy import deepcopy

def dfs(route : list, tickets : list, final_route :list):
    if not tickets:
        final_route.append(route)
        return
    
    for ticket in tickets:
        if route[-1] == ticket[0]:
            rest_tickets = deepcopy(tickets)
            rest_tickets.remove(ticket)
            new_route = route.copy()
            new_route.append(ticket[1])
            dfs(new_route, rest_tickets, final_route)
            
            if final_route:
                return
    
def solution(tickets : list):
    tickets.sort()
    final_route = []
    dfs(['ICN'], tickets, final_route)
    return final_route[0]

print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))