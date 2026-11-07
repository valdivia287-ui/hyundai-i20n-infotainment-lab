#!/bin/bash
# Pure read-only evidence predicate; caller independently checks live OEM PID identity.
ca_layout_evidence_match() {
 local geometry="$1" view="$2" frame="$3" owner="$4" expected_pid="$5" tick sid
 tick=$(printf '%s\n' "$geometry" | sed -n 's/.*tick=\([0-9]*\).*/\1/p')
 sid=$(printf '%s\n' "$geometry" | sed -n 's/.* id=\([0-9]*\) .*/\1/p')
 [[ "$expected_pid" =~ ^[0-9]+$ && "$sid" =~ ^[0-9]+$ && "$tick" =~ ^[0-9]+$ ]] || return 1
 [[ "$geometry" == *'source=0,0,1920,720 dest=0,0,1280,730 opacity=1.0000'* && "$geometry" == *'layer=102' && "$view" == *"tick=$tick "* && "$view" == *'matrix=0.666667,1.013889,0.000000,'* && "$frame" == *"tick=$tick id=$sid "* && "$frame" == *'layer=102 visible=1 layer_visible=1 buffer=1920x720'* && "$frame" == *'listed=1 output=1'* && "$owner" == *"tick=$tick id=$sid pid=$expected_pid comm=AppHomeScreen" ]] || return 1
}
