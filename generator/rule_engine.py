# generator/rule_engine.py

from dataclasses import dataclass
from typing import List, Tuple
import random


@dataclass
class Rule:
    name: str
    underlying_forms: List[str]
    surface_forms: List[str]
    pattern_desc: str

    def generate_examples(self, n: int = 5) -> List[Tuple[str, str]]:
        pairs = list(zip(self.underlying_forms, self.surface_forms))
        return random.sample(pairs, min(n, len(pairs)))

    def generate_unknowns(self, n: int = 3) -> List[str]:
        candidates = [w for w in self.underlying_forms if w not in self.surface_forms]
        return random.sample(candidates, min(n, len(candidates)))

    @classmethod
    def from_word_list(cls, verb_stems: List[str], suffix: str = "ed") -> "Rule":
        surfaces = [stem + suffix for stem in verb_stems]
        desc = f"Add the suffix '{suffix}' to form the past tense."
        return cls(
            name="past_tense_regular",
            underlying_forms=verb_stems,
            surface_forms=surfaces,
            pattern_desc=desc,
        )


if __name__ == "__main__":
    verbs = ["walk", "jump", "play", "talk", "climb"]
    rule = Rule.from_word_list(verbs, suffix="ed")
    print("Rule:", rule.pattern_desc)
    print("Examples:", rule.generate_examples())
    print("Unknowns:", rule.generate_unknowns())

