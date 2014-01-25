#!/usr/bin/env python

import os

deltimer = " | "


statstics = {}
for line in os.popen("svn log --quiet"):
  ## not revision information skip
  if not line.startswith("r"):
    continue

  revision, author, timestamp = line.strip().split(deltimer)
  #print "%s commit %s at %s" % (author, revision, timestamp)

  if author not in statstics:
    statstics[author] = 1
  else:
    statstics[author] += 1

if len(statstics.keys()) != 0:
  print "%15s|%10s" % ("Author".center(15), "Commits".center(10))
  print "-" * 15 + "|" + "-" * 10
  for author in statstics.keys():
    print "%15s|%10d" % (author, statstics[author])

