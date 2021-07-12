from SensorData import CPU
# openSensorPanel Configuration File
# Developed by Hunter LaFaille, created for the community.

# MAIN CONFIGURATION
MAIN = dict(VERSION="rc-1",
            DEVELOPER="Hunter LaFaille",
            REFRESH_RATE="1",
            WINDOW_TITLE=CPU.name(),
            MAIN_DRIVE="/dev/nvme0n1p2",
            )

# NETWORK CONFIGURATION
# !!! Time is handled in seconds.
NETWORK = dict(SPEEDTEST_REFRESH = 10,
               )