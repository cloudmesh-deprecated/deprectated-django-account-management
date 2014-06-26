"""
Usage:
program (--opt=OPT ...)

Options:
  --opt=OPT    An option that can be specified multiple times to form a list
"""

import docopt

arguments = docopt.docopt(__doc__)
print docopt.docopt(__doc__)

print arguments['--opt'][0]
