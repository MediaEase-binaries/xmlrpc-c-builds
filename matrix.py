#!/usr/bin/env python3

"""
Build matrix configuration for xmlrpc-c.

Sources are exported from SourceForge Subversion:
  https://svn.code.sf.net/p/xmlrpc-c/code/release_number/<version>

Optional svn_revision pins the export to a known revision (see release commits on SF).
"""

import yaml

# svn_revision: optional pin (None = HEAD of that release path)
RELEASES = [
    {"version": "1.59.04", "svn_revision": "3253"},
    {"version": "1.64.02", "svn_revision": None},
    {"version": "1.66.01", "svn_revision": "3332"},
]


def generate_matrix():
    matrix = []
    for rel in RELEASES:
        row = {
            "version": rel["version"],
            "os": "debian-13",
            "codename": "trixie",
            "svn_revision": rel["svn_revision"],
        }
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    print(yaml.safe_dump({"include": generate_matrix()}, sort_keys=False))
