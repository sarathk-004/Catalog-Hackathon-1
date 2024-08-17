from collections import deque

class EWasteMonitoringSystem:
    collection_queue = deque()
    required_queue = deque()
    recycling_queue = deque()

    def __init__(self):
        self.device_info = {
            "Printer": {"Quantity": 1, "Quality": "Good", "Condition": "Required"},
            "Disk Drive": {"Quantity": 1, "Quality": "Average", "Condition": "Required"},
            "Earphones": {"Quantity": 1, "Quality": "Good", "Condition": "Required"},
            "Phone": {"Quantity": 1, "Quality": "Poor", "Condition": "Required"},
            "Laptop": {"Quantity": 1, "Quality": "Good", "Condition": "Required"},
            "Canon Camera": {"Quantity": 1, "Quality": "Average", "Condition": "Required"},
            "Wireless Mouse": {"Quantity": 1, "Quality": "Good", "Condition": "Required"},
            "External Hard Drive": {"Quantity": 1, "Quality": "Average", "Condition": "Required"},
            "Tablet": {"Quantity": 1, "Quality": "Good", "Condition": "Required"},
            "Webcam": {"Quantity": 1, "Quality": "Poor", "Condition": "Required"}
        }

    def add_to_collection_queue(self, item):
        self.collection_queue.append(item)
        print(f"Item '{item}' added to collection queue.")

    def add_to_required_queue(self):
        for it in self.collection_queue:
            if len(self.required_queue) < 5:
                self.required_queue.append(it)
                self.device_info[it]['Condition'] = "Required"
                print(f"Item '{it}' added to the required queue.")
            elif len(self.required_queue) >= 5:
                popItem = self.required_queue.popleft()
                self.device_info[popItem]['Condition'] = "Recycling"
                self.recycling_queue.append(popItem)
                self.device_info[it]['Condition'] = "Required"
                self.required_queue.append(it)
                print(f"Item '{popItem}' removed from required queue and added to recycling queue.")
                print(f"Item '{it}' added to the required queue.")

    def monitor(self, userInput):
        if userInput in self.device_info:
            status = self.device_info[userInput]['Condition']
            print(f"Item '{userInput}' is {'in the required queue and used in our industry' if status == 'Required' else 'in the recycle phase'}.")
        else:
            print(f"Item '{userInput}' is not a valid item name.")

    def generate_report(self):
        print("\n\nE-Waste Report:")
        print(f"{'Device':<25} {'Quantity':<10} {'Quality':<10} {'Condition':<10}")
        print("="*55)
        for device, info in self.device_info.items():
            print(f"{device:<25} {info['Quantity']:<10} {info['Quality']:<10} {info['Condition']:<10}")
        print("="*55)

    def lifeCycle(self):
        self.add_to_required_queue()
        self.generate_report()
        self.monitor("Printer")
        self.monitor("Wrong name")
        self.monitor("External Hard Drive")
        self.monitor("Canon Camera")
        print("=================================================")

system = EWasteMonitoringSystem()

print("=================================================")
print("Adding items to the collection queue")
system.add_to_collection_queue("Printer")
system.add_to_collection_queue("Disk Drive")
system.add_to_collection_queue("Earphones")
system.add_to_collection_queue("Phone")
system.add_to_collection_queue("Laptop")
system.add_to_collection_queue("Canon Camera")
system.add_to_collection_queue("Wireless Mouse")
system.add_to_collection_queue("External Hard Drive")
system.add_to_collection_queue("Tablet")
system.add_to_collection_queue("Webcam")

print("=================================================")
system.lifeCycle()
