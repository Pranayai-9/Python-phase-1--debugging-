#Faulty code
incidents = [
    {
        "id": "I101",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 1200
    },
    {
        "id": "I102",
        "location": "Zone B",
        "type": "Fire",
        "severity": 3,
        "affected": 400
    },
    {
        "id": "I103",
        "location": "Zone A",
        "type": "Flood",
        "severity": 4,
        "affected": 800
    },
    {
        "id": "I104",
        "location": "Zone C",
        "type": "Cyclone",
        "severity": 5,
        "affected": 2500
    }
]


def generate_incident_report(incidents):

    total_affected = 0

    locations = []

    high_priority = []

    disaster_types = []

    for incident in incidents:

        total_affected = incident["affected"]

        locations.append(incident["location"])

        disaster_types.append(incident["type"])

        if incident["severity"] > 3:
            high_priority.append(incident["id"])

    return {
        "total_affected": total_affected,
        "locations": len(locations),
        "disaster_types": disaster_types,
        "high_priority": high_priority
    }


report = generate_incident_report(incidents)

print(report)


#Debugged code
incidents = [
    {
        "id": "I101",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 1200
    },
    {
        "id": "I102",
        "location": "Zone B",
        "type": "Fire",
        "severity": 3,
        "affected": 400
    },
    {
        "id": "I103",
        "location": "Zone A",
        "type": "Flood",
        "severity": 4,
        "affected": 800
    },
    {
        "id": "I104",
        "location": "Zone C",
        "type": "Cyclone",
        "severity": 5,
        "affected": 2500
    },
     {
        "id": "I104",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 2500
    },
    {
        "id": "I105",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 50
    }

]


def generate_incident_report(incidents):

    id_counts = {}

    for incident in incidents:
        incident_id = incident["id"]
        id_counts[incident_id] = id_counts.get(incident_id, 0) + 1

    duplicate_records = []

    for incident in incidents:
        if id_counts[incident["id"]] > 1:
            duplicate_records.append(incident)

    total_affected = 0
    locations = set()
    disaster_types = set()
    high_priority = []
    affected_by_disaster = {}

    for incident in incidents:

        if id_counts[incident["id"]] > 1:
            continue

        total_affected += incident["affected"]

        locations.add(incident["location"])
        disaster_types.add(incident["type"])

        disaster = incident["type"]

        if disaster in affected_by_disaster:
            affected_by_disaster[disaster] += incident["affected"]
        else:
            affected_by_disaster[disaster] = incident["affected"]

        if incident["severity"] is not None:
            if incident["severity"] > 3:
                high_priority.append(incident["id"])
        elif incident["affected"] > 500:
            high_priority.append(incident["id"])

    return {
        "duplicate_records": duplicate_records,
        "total_affected": total_affected,
        "locations": len(locations),
        "disaster_types": disaster_types,
        "high_priority": high_priority,
        "affected_by_disaster": affected_by_disaster
    }


report = generate_incident_report(incidents)

print(report)

#AI version
incidents = [
    {
        "id": "I101",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 1200
    },
    {
        "id": "I102",
        "location": "Zone B",
        "type": "Fire",
        "severity": 3,
        "affected": 400
    },
    {
        "id": "I103",
        "location": "Zone A",
        "type": "Flood",
        "severity": 4,
        "affected": 800
    },
    {
        "id": "I104",
        "location": "Zone C",
        "type": "Cyclone",
        "severity": 5,
        "affected": 2500
    },
    {
        "id": "I104",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 2500
    },
    {
        "id": "I105",
        "location": "Zone A",
        "type": "Flood",
        "severity": 5,
        "affected": 50
    }
]


def generate_incident_report(incidents):

    required_fields = {
        "id", "location", "type", "severity", "affected"
    }

    valid_records = []
    invalid_records = []

    # STEP 1: Validate individual records

    for incident in incidents:

        if not isinstance(incident, dict):
            invalid_records.append({
                "record": incident,
                "reason": "Record is not a dictionary"
            })
            continue

        if not required_fields.issubset(incident):
            invalid_records.append({
                "record": incident,
                "reason": "Missing required fields"
            })
            continue

        if not all(
            isinstance(incident[field], str) and incident[field].strip()
            for field in ["id", "location", "type"]
        ):
            invalid_records.append({
                "record": incident,
                "reason": "Invalid ID, location or disaster type"
            })
            continue

        severity = incident["severity"]
        affected = incident["affected"]

        if type(severity) != int or not 1 <= severity <= 5:
            invalid_records.append({
                "record": incident,
                "reason": "Invalid severity"
            })
            continue

        if type(affected) != int or affected < 0:
            invalid_records.append({
                "record": incident,
                "reason": "Invalid affected population"
            })
            continue

        valid_records.append(incident)

    # STEP 2: Group records by incident ID

    id_groups = {}

    for incident in valid_records:

        incident_id = incident["id"]

        if incident_id not in id_groups:
            id_groups[incident_id] = []

        id_groups[incident_id].append(incident)

    unique_records = []
    exact_duplicates = []
    conflicting_records = []

    # STEP 3: Resolve duplicate IDs

    for incident_id, records in id_groups.items():

        if len(records) == 1:
            unique_records.append(records[0])

        else:
            first_record = records[0]

            identical = all(
                record == first_record
                for record in records
            )

            if identical:
                unique_records.append(first_record)

                exact_duplicates.extend(records[1:])

            else:
                conflicting_records.extend(records)

    # STEP 4: Generate incident statistics

    total_affected = 0

    locations = set()
    disaster_types = set()

    high_priority = []

    affected_by_disaster = {}
    incidents_by_disaster = {}

    for incident in unique_records:

        total_affected += incident["affected"]

        locations.add(incident["location"])
        disaster_types.add(incident["type"])

        disaster = incident["type"]

        affected_by_disaster[disaster] = (
            affected_by_disaster.get(disaster, 0)
            + incident["affected"]
        )

        incidents_by_disaster[disaster] = (
            incidents_by_disaster.get(disaster, 0) + 1
        )

        if incident["severity"] > 3:
            high_priority.append(incident["id"])

    # STEP 5: Return final report

    return {
        "total_incidents": len(unique_records),

        "total_affected": total_affected,

        "unique_locations": len(locations),

        "disaster_types": sorted(disaster_types),

        "high_priority_incidents": high_priority,

        "affected_by_disaster": affected_by_disaster,

        "incidents_by_disaster": incidents_by_disaster,

        "exact_duplicates": exact_duplicates,

        "conflicting_records": conflicting_records,

        "invalid_records": invalid_records
    }


report = generate_incident_report(incidents)

for key, value in report.items():
    print(key, ":", value)
```