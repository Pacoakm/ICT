import time
import ha

# Create HomeAssistant() object
HA = ha.HomeAssistant()

# Wait until it is up and running
HA.wait_for_startup(1)

# Get the entities
entities = HA.get_entities()
