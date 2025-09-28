# Rules

1. High request rate: An IP address attempts >=30 requests within a minute only. This is a high serverity and indicates a Denial of Service attack.
2. High login attemot rateL A user with the same IP address attempts to login >=20 times within 60 seconds. This is a high serverity, and indicates brute-force attack and attempting to have unauthorised access.
3. Suspicious User Agents: Requests of using tools such as "sqlmap", "python-requests", "Go-http-client", "curl/" or "nikto". Can be treated as a medium severity, high if it links back to rules 1 or 2. Indicates a user wants to exploit these tools, could be an inside actor.