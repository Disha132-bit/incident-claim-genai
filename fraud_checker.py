def check_for_fraud(claim_data):
    fraud_reasons = []

    # Validate amount format and threshold
    amount_str = claim_data.get("Claim Amount", "").replace("₹", "").replace(",", "").strip()
    try:
        amount = float(amount_str)
        if amount > 100000:
            fraud_reasons.append("⚠️ High claim amount (over ₹1,00,000)")
    except ValueError:
        fraud_reasons.append("❗ Invalid claim amount format")

    # Required fields (based on parser)
    required_fields = ["Policy Number", "Claimant Name", "Claim Amount", "Date of Incident", "Claim Reason"]
    for field in required_fields:
        if not claim_data.get(field):
            fraud_reasons.append(f"❗ Missing field: {field}")

    # Suspicious keywords
    reason = claim_data.get("Claim Reason", "").lower()
    suspicious_keywords = ["lost", "fire", "theft", "stolen", "unknown"]
    for keyword in suspicious_keywords:
        if keyword in reason:
            fraud_reasons.append(f"⚠️ Suspicious keyword in reason: '{keyword}'")

    return fraud_reasons
