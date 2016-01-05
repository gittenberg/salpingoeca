#!/bin/bash
cat temp | awk -v RS=">" '{ print $0 > "temp" NR }'