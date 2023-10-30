import random
import time

# Define SD-WAN parameters with "link up" options
WAN_OPTIONS = ["Internet", "MPLS", "Cellular"]
LINK_STATUS = {link: "down" for link in WAN_OPTIONS}
SLA_THRESHOLDS = {
    "latency_threshold": 50,  # Milliseconds
    "loss_threshold": 0.1,    # 10% loss
    "jitter_threshold": 10,   # Milliseconds
}

class SDWANOptimizer:
    def __init__(self):
        pass

    def monitor_links(self):
        # Simulate link monitoring and update link status (Up or Down) based on random values.
        for link in WAN_OPTIONS:
            if random.random() < 0.2:  # Simulate link instability (20% chance of going down)
                LINK_STATUS[link] = "Down"
            else:
                LINK_STATUS[link] = "Up"

    def conventional_backup(self, primary_link, backup_link):
 
        # Shift the entire load from the primary link to the backup link if the primary link is down.
        if LINK_STATUS[primary_link] == "down":
            print(f"Shifting traffic from {primary_link} to {backup_link}")

    def load_balance(self, application):
        # Load balancing among WAN options for a specific application using Round Robin.
        active_links = [link for link in WAN_OPTIONS if LINK_STATUS[link] == "Up"]
        if not active_links:
            print("No active links available for load balancing.")
        else:
            selected_link = active_links[len(application) % len(active_links)]
            print(f"Balancing traffic for {application} using Round Robin on {selected_link}")

    def shift_application_traffic(self, application):
        # Shift application traffic to another WAN option based on SLA parameters.
        current_link = self.get_current_link(application)
        if current_link:
            sla_metrics = self.generate_sla_metrics()
            if self.sla_violation(current_link, sla_metrics):
                best_link = self.find_best_link(sla_metrics)
                if best_link and best_link != current_link:
                    print(f"Shifting traffic for {application} from {current_link} to {best_link} based on SLA")

    def get_current_link(self, application):
        # Simulated logic to determine the current link for an application.
        # In a real-world scenario, you would have a more sophisticated mechanism.
        return random.choice(WAN_OPTIONS)

    def generate_sla_metrics(self):
        # Simulated generation of SLA metrics.
        return {
            "latency": random.randint(0, 100),
            "loss": random.uniform(0, 0.5),
            "jitter": random.randint(0, 50),
        }

    def sla_violation(self, link, sla_metrics):
        # Check if SLA parameters are violated for the given link.
        return (
            sla_metrics["latency"] > SLA_THRESHOLDS["latency_threshold"] or
            sla_metrics["loss"] > SLA_THRESHOLDS["loss_threshold"] or
            sla_metrics["jitter"] > SLA_THRESHOLDS["jitter_threshold"]
        )

    def find_best_link(self, sla_metrics):
        # Simulated logic to find the best link based on SLA metrics.
        # In a real-world scenario, you would measure actual network conditions.
        return random.choice(WAN_OPTIONS)

if __name__ == "__main__":
    optimizer = SDWANOptimizer()

    while True:
        optimizer.monitor_links()

        # Example usage of the SD-WAN features
        optimizer.conventional_backup("MPLS", "Internet")
        optimizer.load_balance("VoIP")
        optimizer.shift_application_traffic("VideoStreaming")

        # Simulate a delay between iterations for monitoring and decision-making.
        time.sleep(5)