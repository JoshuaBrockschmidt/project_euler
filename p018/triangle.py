import copy

class Triangle:
    def __init__(self, path=None):
        self._rows = []

        if path is not None:
            with open(path, 'r') as f:
                for line in f.readlines():
                    tokens = line.strip().split(' ')
                    if len(tokens) > 0:
                        nums = list(map(int, tokens))
                        self._rows.append(nums)

                        # Make sure the triangle is shaped correctly.
                        if len(self._rows) == 1:
                            assert len(self._rows[0]) == 1
                        else:
                            assert len(self._rows[-1]) == len(self._rows[-2]) + 1

    def get_next_below(self, ij):
        i, j = ij
        if i < len(self._rows) - 1:
            return ((i + 1, j), (i + 1, j + 1))
        else:
            return None

    def get_val(self, ij):
        i, j = ij
        return self._rows[i][j]

    def set_val(self, ij, val):
        i, j = ij
        self._rows[i][j] = val

    def get_num_rows(self):
        return len(self._rows)

    def get_num_cols(self, i):
        return len(self._rows[i])

    def copy(self):
        new_tri = Triangle()
        new_tri._rows = copy.deepcopy(self._rows)
        return new_tri
