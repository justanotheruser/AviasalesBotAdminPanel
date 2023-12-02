#!/bin/bash
script_name=$0
function usage {
    echo ""
    echo "Starts Aviasales Bot Admin Panel server"
    echo ""
    echo "usage: $script_name admin_panel_root_dir [--host string] [-s] "
    echo ""
    echo "  --host string   ip address to run server"
    echo "                      (example: 127.0.0.1)"
    echo "  -s              Boolean flag to run in background"
    echo "                      using 'screen' command"
    echo ""
}

function die {
    printf "Script failed: %s\n\n" "$1"
    exit 1
}

function check_positional_argument {
  if [[ $2 == "-"* ]]; then
    usage
    die "Missing positional argument $1"
  fi
}


# Parse positional arguments
check_positional_argument "admin_panel_root_dir" "$1"
admin_panel_root_dir=$1
shift

# Parse named arguments and flags
while [ $# -gt 0 ]; do
    echo "loop $1"
    if [[ $1 == "--"* ]]; then
        v="${1/--/}"
        declare "$v"="$2"
        shift
    elif [[ $1 == "-"* ]]; then
        v="${1/-/}"
        declare "$v"=1
    fi
    shift
done

# Defaults
host="${host:-127.0.0.1}"
s="${s:-0}"

if [[ -z $admin_panel_root_dir ]]; then
    usage
    die "Missing argument admin_panel_root_dir"
elif [[ -z $host ]]; then
    usage
    die "Missing argument --host"
fi

# Main
if [ "$s" == "1" ]; then
    if [ -z "$STY" ]; then
        exec screen -dmS air_bot_stage /bin/bash "$script_name" "$admin_panel_root_dir" --host "$host";
    fi
fi
cd "$admin_panel_root_dir" || exit
source ~/.profile
echo "$host"
uvicorn aviasales_bot_admin.main:app --host "$host" --reload
