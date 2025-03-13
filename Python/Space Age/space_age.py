class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.planets = {
            "mercury": "0.2408467",
            "venus": "0.61519726",
            "earth": "1.0",
            "mars": "1.8808158",
            "jupiter": "11.862615",
            "saturn": "29.447498",
            "uranus": "84.016846",
            "neptune": "164.79132",
        }
        for planet, ratio in self.planets.items():
            setattr(
                self,
                f"on_{planet}",
                (
                    lambda self, ratio=ratio: round(
                        self.seconds / 31557600 / float(ratio), 2
                    )
                ).__get__(self),
            )
