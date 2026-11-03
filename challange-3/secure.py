#Faulty code
login_logs = [
    {"user": "admin", "ip": "192.168.1.10", "status": "failed"},
    {"user": "rahul", "ip": "192.168.1.11", "status": "success"},
    {"user": "admin", "ip": "192.168.1.10", "status": "failed"},
    {"user": "admin", "ip": "192.168.1.12", "status": "failed"},
    {"user": "meera", "ip": "192.168.1.13", "status": "success"},
    {"user": "admin", "ip": "192.168.1.10", "status": "success"}
]


def analyze_security(logs):

    failed_users = []

    suspicious_ips = []

    successful_users = []

    for log in logs:

        user = log["user"]

        ip = log["ip"]

        status = log["status"]

        if status == "Failed":
            failed_users.append(user)
            suspicious_ips.append(ip)

        else:
            successful_users.append(user)

    alerts = []

    for user in failed_users:

        if failed_users.count(user) >= 3:
            alerts.append(user)

    unique_ips = len(suspicious_ips)

    return {
        "alerts": alerts,
        "suspicious_ips": unique_ips,
        "successful_users": successful_users
    }


result = analyze_security(login_logs)

print(result)


#Debugged version 
def analyze_security(logs):

    failed_users = []
    suspicious_ips = []
    successful_users = []

    for log in logs:

        user = log["user"]
        ip = log["ip"]
        status = log["status"]

        if status == "failed":
            failed_users.append(user)
            suspicious_ips.append(ip)
        else:
            successful_users.append(user)

    alerts = set()

    for user in failed_users:
        if failed_users.count(user) >= 3:
            alerts.add(user)

    unique_ips = len(set(suspicious_ips))

    return {
        "alerts": list(alerts),
        "suspicious_ips": unique_ips,
        "successful_users": successful_users
    }

