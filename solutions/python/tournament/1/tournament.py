def tally(rows):
    teams = {}
    result = ["Team                           | MP |  W |  D |  L |  P"]
    for row in rows:
      
        team1, team2, outcome = row.split(";")
        
        teams.setdefault(team1, {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
        teams[team1]["MP"] += 1
        teams.setdefault(team2, {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
        teams[team2]["MP"] += 1
        
        if outcome == "win":
            teams[team1]["W"] += 1
            teams[team2]["L"] += 1
            
        elif outcome == "draw":
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            
        else:
            teams[team1]["L"] += 1
            teams[team2]["W"] += 1

        teams[team1]["P"] = teams[team1]["W"] * 3 + teams[team1]["D"]
        teams[team2]["P"] = teams[team2]["W"] * 3 + teams[team2]["D"]

    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0]))
        
    for name, stats in sorted_teams:
        result.append(f"{name:<31}| {stats['MP']:2} | {stats['W']:2} | {stats['D']:2} | {stats['L']:2} | {stats['P']:2}")
    return result







        