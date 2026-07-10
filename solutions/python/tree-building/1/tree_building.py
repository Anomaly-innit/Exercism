class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda r: r.record_id)
    nodes = []

    for index, record in enumerate(records):
        # VALIDATION — is this record broken?
        if record.record_id != index:
            raise ValueError("Record id is invalid or out of order.")
        if record.record_id == 0:
            if record.parent_id != 0:
                raise ValueError("Node parent_id should be smaller than its record_id.")
        else:
            if record.parent_id == record.record_id:
                raise ValueError("Only root should have equal record and parent id.")
            elif record.parent_id > record.record_id:
                raise ValueError("Node parent_id should be smaller than its record_id.")

        new_node = Node(record.record_id)
        nodes.append(new_node)
        if record.record_id != 0:
            nodes[record.parent_id].children.append(new_node)  

    return nodes[0]
