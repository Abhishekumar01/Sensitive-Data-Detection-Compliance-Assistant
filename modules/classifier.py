"""Risk Classification Module"""

RISK_WEIGHTS = {

    "Email Address": 2,

    "Phone Number": 2,

    "Employee ID": 3,

    "PAN Number": 5,

    "Aadhaar Number": 5,

    "Bank Account": 6,

    "IFSC Code": 4,

    "Credit Card": 8,

    "Password": 10,

    "API Key": 10,

    "Confidential Business Information": 8

}


def calculate_risk(detected_items):

    score = 0

    breakdown = []

    for item in detected_items:

        category = item["type"]

        count = item["count"]

        weight = RISK_WEIGHTS.get(category, 1)

        item_score = weight * count

        score += item_score

        breakdown.append({

            "Type": category,

            "Count": count,

            "Weight": weight,

            "Score": item_score

        })

    if score < 10:

        level = "Low"

        color = "green"

    elif score < 25:

        level = "Medium"

        color = "orange"

    else:

        level = "High"

        color = "red"

    return {

        "score": score,

        "level": level,

        "color": color,

        "breakdown": breakdown

    }