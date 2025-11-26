class _DummyFace:
    def __init__(self, left=0, top=0, right=0, bottom=0):
        self._l = left
        self._t = top
        self._r = right
        self._b = bottom

    def left(self):
        return self._l

    def top(self):
        return self._t

    def right(self):
        return self._r

    def bottom(self):
        return self._b


class _DummyDetector:
    def __call__(self, image, upsample_num_times=1):
        # Return empty list — no faces detected. Calling code handles this case.
        return []


def get_frontal_face_detector():
    return _DummyDetector()
