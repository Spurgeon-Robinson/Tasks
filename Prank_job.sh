# This scirpt plays a prank on the user by retarting
# their computer every hour on friday the 13th.
sudo shutdown -r +60 "Your computer will restart in 60 minutes. Please save your work."
# It is intended to be run as a cron job.
# To set up the cron job, you can add the following line to your crontab:
# 0 * * * 5 [ "$(date +\%d)" -eq 13 ] && /path/to/Prank_job.sh
# Make sure to give execute permissions to the script:
# chmod +x /path/to/Prank_job.sh
