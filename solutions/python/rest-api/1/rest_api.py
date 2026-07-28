import json

class RestAPI:
    def __init__(self, database=None):
        database = database or {"users": []}
        self.users = {u["name"]: u for u in database["users"]}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                names = json.loads(payload)["users"]
            else:
                names = self.users.keys()
            result = {"users": sorted((self.users[n] for n in names), key=lambda u: u["name"])}
            return json.dumps(result)
            
    def post(self, url, payload=None):
        data = json.loads(payload)
        if url == "/add":
            name = data["user"]
            new_user = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.users[name] = new_user
            return json.dumps(new_user)
        elif url == "/iou":
            lender = data["lender"]
            borrower = data["borrower"]
            amount = data["amount"]
            
            lender_obj = self.users[lender]
            borrower_obj = self.users[borrower]
            
            net = lender_obj["owed_by"].get(borrower, 0) - lender_obj["owes"].get(borrower, 0) + amount
            
            lender_obj["owed_by"].pop(borrower, None)
            lender_obj["owes"].pop(borrower, None)
            borrower_obj["owed_by"].pop(lender, None)
            borrower_obj["owes"].pop(lender, None)
            
            if net > 0:
                lender_obj["owed_by"][borrower] = net
                borrower_obj["owes"][lender] = net
            elif net < 0:
                lender_obj["owes"][borrower] = -net
                borrower_obj["owed_by"][lender] = -net
            
            lender_obj["balance"] = sum(lender_obj["owed_by"].values()) - sum(lender_obj["owes"].values())
            borrower_obj["balance"] = sum(borrower_obj["owed_by"].values()) - sum(borrower_obj["owes"].values())
            
            result = {"users": sorted([lender_obj, borrower_obj], key=lambda u: u["name"])}
            return json.dumps(result)