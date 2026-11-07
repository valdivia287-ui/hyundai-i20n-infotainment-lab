#!/bin/bash
# Development profile only. Original PAS service and original default package;
# fresh virtual data storage, no synthetic RCT/config and no updater invocation.
set -euo pipefail
[[ ${CA_GUEST:-0} == 1 && -f /mnt/ca-tools/PRODUCT_SESSION ]] || exit 2
grep -q 'root=/dev/vda' /proc/cmdline || exit 2
export PATH=/mnt/r6/support/bin:/usr/bin/qt5:/usr/bin:/usr/sbin:/bin:/sbin
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/run/r4/system-bus
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/r4/session-bus
out=/mnt/ca-output
printf '%s  %s\n' 9339feb536f50081a92edca7f6fa37cdb9079db580065ad44501c67d604de036 /usr/bin/pers_admin_svc d16879b383744f8247993f4c225f81c7a8f81e679770975e5772a77f979bf41a /app/share/hkmc.tar.gz | sha256sum -c - > "$out/pas-original-integrity.txt"
[[ ! -L /Data/mnt-c && ! -L /Data/mnt-wt ]] || exit 3
if ! mountpoint -q /Data/mnt-wt;then
 # OEM fstab mounts partition12 at both names; preserve that alias inside overlay.
 # The recovered base contains only this nested legacy symlink. A bind hides
 # it without deleting it. Reject every other entry rather than hiding data.
 ls -la /Data/mnt-wt > "$out/pas-before-alias.txt"
 for entry in /Data/mnt-wt/* /Data/mnt-wt/.[!.]* /Data/mnt-wt/..?*;do
  [[ -e "$entry" || -L "$entry" ]] || continue
  [[ "$entry" == /Data/mnt-wt/mnt-wt && -L "$entry" && $(readlink "$entry") == /rw_data/mnt-wt ]] || exit 3
 done
 mount --bind /Data/mnt-c /Data/mnt-wt
fi
stat -c '%d:%i %n' /Data/mnt-c /Data/mnt-wt > "$out/pas-data-alias.txt"
[[ $(stat -c '%d:%i' /Data/mnt-c) == $(stat -c '%d:%i' /Data/mnt-wt) ]] || exit 3
cat /etc/installConfig.cfg > "$out/pas-install-config-path.txt"
[[ $(cat /etc/installConfig.cfg) == /app/share/hkmc.tar.gz ]] || exit 3
existing=$(pidof pers_admin_svc 2>/dev/null || true)
if [[ -n "$existing" ]];then
 [[ "$existing" =~ ^[0-9]+$ && $(readlink /proc/$existing/exe) == /usr/bin/pers_admin_svc ]] || exit 3
 printf "CA_PAS_REUSED pid=%s\n" "$existing"
 exit 0
fi
timeout -s TERM -k 3 1200 /usr/bin/pers_admin_svc > "$out/pas-original.txt" 2>&1 &
echo "$!" > "$out/pas-runner.pid"
sleep 5
pidof pers_admin_svc > "$out/pas-original.pid" || true
find /Data/mnt-c -maxdepth 4 -name 'resource-table*' -o -name 'GroupContent.json' > "$out/pas-generated-files.txt"
ls -ld /Data/mnt-wt/Settings/shared_public >> "$out/pas-generated-files.txt" 2>&1 || true
printf 'CA_PAS_PREPARED original_service_original_package_virtual_data_alias\n'
