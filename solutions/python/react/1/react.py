_all_compute_cells = []

class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value == self._value:
            return
        self._value = new_value
        _stabilize()


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self._value = self._compute()
        _all_compute_cells.append(self)

    def _compute(self):
        return self.compute_function([cell.value for cell in self.inputs])

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)


def _stabilize():
    old_values = {cell: cell._value for cell in _all_compute_cells}
    for cell in _all_compute_cells:
        cell._value = cell._compute()
    for cell in _all_compute_cells:
        if cell._value != old_values[cell]:
            for callback in cell.callbacks:
                callback(cell._value)