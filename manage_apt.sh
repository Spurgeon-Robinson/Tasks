# This script manages APT packages.
# It uninstalls all unused dependencies.
# It updates the software database.
# It updates the entire system.
# Usage: ./manage_apt.sh
sudo apt autoremove -y
sudo apt update
sudo apt upgrade -y
echo "APT package management tasks completed."
echo "Done."
exit 0
