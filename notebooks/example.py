import random
import time
from pandasbox import PandasBox


class CatPhoto:
    def __init__(self):
        self.name = random.choice(["Luna", "Willow", "Elvis", "Nacho", "Tiger"])
        self.width = random.choice(range(200, 2000))
        self.height = random.choice(range(200, 2000))
        self.brightness = random.random() * 10
        self.image_data = "Y2Ugbidlc3QgcGFzIHVuZSBjaGF0dGU="


random.seed(42)

# Make a million
photos = [CatPhoto() for _ in range(10 ** 6)]

# Build PandasBox

t0 = time.time()
ri = PandasBox(
    photos,
    on={"height": int, "width": int, "brightness": float, "name": str},
    engine="sqlite",
    table_index=[("width", "height", "brightness")],
)
t_build = time.time() - t0

# Find PandasBox matches
t0 = time.time()
ri_matches = ri.find(
    "name == 'Tiger' and height >= 1900 and width >= 1900 and brightness >= 9.0"
)
t_pandasbox = time.time() - t0
print(t_pandasbox)

# Find list comprehension matches
t0 = time.time()
lc_matches = [
    p
    for p in photos
    if p.name == "Tiger"
    and p.height >= 1900
    and p.width >= 1900
    and p.brightness >= 9.0
]
t_listcomp = time.time() - t0
print(t_listcomp)

print(f"PandasBox found {len(ri_matches)} matches in {round(t_pandasbox, 6)} seconds.")
print(
    f"List comprehension found {len(lc_matches)} matches in {round(t_listcomp, 6)} seconds."
)
print(f"Speedup: {round(t_listcomp / t_pandasbox)}x")
