def extract_claim_info(file_content):
    lines = file_content.splitlines()
    claim_info = {}

    for line in lines:
        line = line.strip()
        if "Policy Number" in line:
            claim_info["Policy Number"] = line.split(":")[-1].strip()
        elif "Claimant Name" in line:
            claim_info["Claimant Name"] = line.split(":")[-1].strip()
        elif "Claim Amount" in line:
            claim_info["Claim Amount"] = line.split(":")[-1].strip()
        elif "Date of Incident" in line:
            claim_info["Date of Incident"] = line.split(":")[-1].strip()
        elif "Claim Reason" in line:
            claim_info["Claim Reason"] = line.split(":")[-1].strip()

    return claim_info
