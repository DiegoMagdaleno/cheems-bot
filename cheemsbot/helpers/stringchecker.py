import re


class StringChecker:
    def __init__(self, string: str) -> None:
        self.string = string

    def is_unicode(self) -> bool:
        try:
            self.string.encode("ascii")
            return True
        except UnicodeEncodeError:
            return False

    def contains_racism(self) -> bool:
        self.possible_matches = [
            "pike?(ys?|ies)",
            "pakis?",
            "(ph|f)agg?s?([e0aio]ts?|oted|otry)",
            "nigg?s?",
            "nigg?[aeoi]s?",
            "(ph|f)[@a]gs?",
            "n[i!j1e]+gg?(rs?|ett?e?s?|lets?|ress?e?s?|r[a0oe]s?|[ie@ao0!]rs?|r[o0]ids?|ab[o0]s?|erest)",
            "j[!i]gg?[aer]+(boo?s?|b00?s?)",
            "jigg?[aer]+(b[0o]ing)",
            "p[0o]rch\\s*-?m[0o]nke?(ys?|ies?)",
            "g(ooks?|00ks?)",
            "k[iy]+kes?",
            "b[ea]ne[ry]s?",
            "(towel|rag)\\s*heads?",
            "wet\\s*backs?",
            "dark(e?y|ies?)",
            "(shit|mud)\\s*-?skins?",
            "tarbab(ys?|ies?)",
            "ape\\s*-?frcans?",
            "lesbos?",
            "coons?(y|i?e?s?|er)",
            "trann(ys?|ies?)",
            "mignorants?",
            "lady\\s*-?boys?",
            "spics?",
            "/?r?/?coon\\s*town",
            "/?r?/?ni?1?ggers?",
            "you\\s*('?re|r)gay",
            "shit\\s*lords?",
            "Homos?",
            "groids?",
            "chimpires?",
            "mud\\s*childr?e?n?",
            "n[1!i]gs?-?",
            "gays?(est|ly|er)",
            "dune\\s*coone?r?s?",
            "high\\s*yellows?",
            "shee?\\s*boons?",
            "cock\\s*suckers?",
            "tards?",
            "retards?",
            "retard\\*s?(ed|edly)",
            "cunts?y?",
            "dot\\s*heads?",
            "china\\s*m[ae]n",
            "queer\\s*bags?",
            "NAMBLA",
            "fucking\\s*(whores?)",
            "puss(y|ies?)",
            "ghey",
            "whore\\s*mouth",
            "fuck\\s*boys?",
            "fat\\s*fucks?",
            "obeasts?",
            "fuck\\s*(wits?|tards?)",
            "beetusbehemoths?",
            "book\\s*fags?",
            "shit\\s*(bags?|dicks?)",
            "twats?",
            "fupas?",
            "holo\\s*hoaxe?s?",
            "Muslimes?",
            "dind[ous]",
            "boot\\s*lips?",
            "jig\\s*apes?",
            "nig\\s*town",
            "suspooks?",
        ]

        self.positive_match = False
        for regex in self.possible_matches:
            matcher = re.search(regex, self.string)
            if matcher:
                self.positive_match = True
                break
        return self.positive_match
