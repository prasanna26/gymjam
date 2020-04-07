class LinearSizer:
    def __init__(self, start_size, end_size):
        self.min_size = start_size
        self.range = end_size-start_size

    def get_size(self, portion_done):
        size = int((portion_done+1e-9)*self.range) + self.min_size
        return min(size, self.min_size+self.range)

class ExponentialSizer:
    def __init__(self, start_size, end_size):
        self.min_size = start_size
        self.max_size = end_size

    def get_size(self, portion_done):
        cur_size = self.max_size
        while portion_done < 0.5 and cur_size > self.min_size:
            cur_size //= 2
            portion_done *= 2

        return cur_size
