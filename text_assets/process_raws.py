__author__ = 'charlie'

import glob
import json

RAW_GLOB = "./raws/*.txt"

def gen_verb(verb_parts):
    return {
        "base": verb_parts[0],
        "past": verb_parts[1].split("/"),
        "past_participle": verb_parts[2].split("/"),
        "3rd_person_singular": verb_parts[3].split("/"),
        "gerund": verb_parts[4].split("/"),
    }


def main():

    for filename in glob.iglob(RAW_GLOB):
        with open(filename, "r") as f:
            verbs = [gen_verb(v.strip().split("\t")) for v in f.readlines()]

        print json.dumps(verbs, indent=4)

if __name__ == "__main__":
    main()