#!/bin/bash

python script.py <<EOF
[
  {
   "Organisation":"coreos",
   "Repository":"hyperkube",
   "Tag":"v1.10.4_coreos.0"
  },
  {
   "Organisation":"coreos",
   "Repository":"dnsmasq",
   "Tag":"v0.5.0"
  },
]
EOF
