from SensorData import CPU
# openSensorPanel Configuration File
# Developed by Hunter LaFaille, created for the community.

# MAIN CONFIGURATION
MAIN = dict(VERSION="rc-1",
            DEVELOPER="Hunter LaFaille",
            REFRESH_RATE="1",
            WINDOW_TITLE=CPU.name(),
            )

# UI CONFIGURATION
BACKGROUND = dict(color="",
                  )
# UI ELEMENTS
UI_TITLE = dict(enabled=True,
                size="24",
                text="My PC",
                color="",
                location="top.left",
                )

UI_CPU_TEMP = dict(enabled=True,
              size="24",
              color="",
              location="top.left")

UI_CPU_LOAD = dict(enabled=True,
              size="24",
              color="",
              location="top.center")