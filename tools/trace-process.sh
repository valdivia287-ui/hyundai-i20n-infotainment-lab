#!/usr/bin/env bash
# Original lab diagnostic; traces remain private. Never signals the target PID.
set -euo pipefail
if [[ $# != 3 || ! $1 =~ ^[1-9][0-9]*$ || ! $3 =~ ^([1-9]|[12][0-9]|30)$ ]]; then
  echo 'Usage: trace-process.sh PID NEW_OUTPUT_DIRECTORY SECONDS(1..30)' >&2
  exit 2
fi
pid=$1
out=$2
seconds=$3
kill -0 "$pid"
command -v strace >/dev/null
mkdir -- "$out"
tracer=
cleanup() {
  if [[ -n $tracer ]]; then
    kill -INT "$tracer" 2>/dev/null || true
    wait "$tracer" 2>/dev/null || true
  fi
}
trap cleanup EXIT
trap 'exit 130' INT TERM
strace -f -tt -s 1024 -e trace=sendmsg,recvmsg,sendto,write \
  -p "$pid" -o "$out/process.strace" </dev/null >"$out/stdout" 2>"$out/stderr" &
tracer=$!
sleep "$seconds"
