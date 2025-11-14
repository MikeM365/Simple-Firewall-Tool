"""
Simple Firewall - Learning Project
Final Version
"""
import datetime

class SimpleFirewall:
    def __init__(self):
        self.rules = []
        self.log = []

    def add_rule(self, action, ip=None, port=None):
        """Adds a new rule to the firewall's rule list."""
        rule = {
            'action': action,
            'ip': ip or 'any',
            'port': str(port) or 'any'
        }
        self.rules.append(rule)
        print(f"Rule added: {action} {rule['ip']}:{rule['port']}")
    
    def show_rules(self):
        """Displays all current firewall rules."""
        if not self.rules:
            print("No rules yet!")
            return
        
        print("\n--- Firewall Rules ---")
        print("-" * 40)
        for i, rule in enumerate(self.rules, 1):
            print(f"{i}. Action: {rule['action'].upper()}, IP: {rule['ip']}, Port: {rule['port']}")
        print("-" * 40)

    def evaluate_packet(self, ip, port):
        """Evaluates a packet against the rules and logs the outcome."""
        port_str = str(port)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for i, rule in enumerate(self.rules, 1):
            ip_match = (rule['ip'] == 'any') or (rule['ip'] == ip)
            port_match = (rule['port'] == 'any') or (rule['port'] == port_str)
            
            if ip_match and port_match:
                action = rule['action']
                reason = f"Matched Rule #{i} ({action.upper()} {rule['ip']}:{rule['port']})"
                
                self.log.append({'timestamp': timestamp, 'ip': ip, 'port': port_str, 'action': action, 'reason': reason})
                print(f"  -> {reason}")
                return action
        
        reason = "No rule matched (Default BLOCK policy)"
        self.log.append({'timestamp': timestamp, 'ip': ip, 'port': port_str, 'action': 'block', 'reason': reason})
        print(f"  -> {reason}")
        return 'block'

    def show_log(self):
        """Displays all entries in the firewall log."""
        if not self.log:
            print("Log is empty.")
            return
        
        print("\n--- Firewall Log ---")
        print("-" * 60)
        for entry in self.log:
            print(f"[{entry['timestamp']}] {entry['action'].upper()} packet from {entry['ip']}:{entry['port']}. Reason: {entry['reason']}")
        print("-" * 60)

# --- Main Loop ---
fw = SimpleFirewall()
print("Simple Firewall Initialized (Default policy is BLOCK)")

while True:
    print("\n--- Menu ---")
    print("1. Add Rule")
    print("2. Show Rules")
    print("3. Simulate and Evaluate a Packet")
    print("4. Show Log")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        action = input("Enter action (allow/block): ").lower()
        ip = input("Enter IP (or leave blank for 'any'): ")
        port = input("Enter port (or leave blank for 'any'): ")
        fw.add_rule(action, ip or None, port or None)
        
    elif choice == '2':
        fw.show_rules()
        
    elif choice == '3':
        print("\n--- Simulate an Incoming Packet ---")
        test_ip = input("Enter source IP of packet: ")
        test_port = input("Enter destination port of packet: ")
        
        if not test_ip or not test_port:
            print("Error: IP and Port are required for testing.")
            continue
        
        result = fw.evaluate_packet(test_ip, test_port)
        print(f"\nResult: Packet from {test_ip}:{test_port} is --> {result.upper()} <---")
        
    elif choice == '4':
        fw.show_log()
        
    elif choice == '5':
        print("Exiting firewall.")
        break
        
    else:
        print("Invalid option, please try again.")