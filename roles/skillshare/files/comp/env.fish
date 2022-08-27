if not string match $S_SRC_DIR/skillshare/workstation/bin $PATH > /dev/null
  set -x PATH $S_SRC_DIR/skillshare/workstation/bin $PATH
end

ev -q skillshare
