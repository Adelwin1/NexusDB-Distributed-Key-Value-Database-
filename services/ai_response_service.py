def generate_response(query: str, results):
    if not results:
        return {
            "answer": "No similar tickets found.",
            "confidence": 0.0
        }

    top = results[0][0]
    score = results[0][1]

    # simple reasoning layer (rule-based AI)
    if "payment" in query.lower() or "charged" in query.lower():
        suggestion = "This looks like a billing issue. Recommend checking duplicate charges and refund status."

    elif "login" in query.lower():
        suggestion = "This appears to be authentication-related. Check password reset or account lockout."

    elif "crash" in query.lower() or "error" in query.lower():
        suggestion = "This is likely a technical bug. Check logs and recent deployments."

    else:
        suggestion = "Review similar tickets and escalate if unresolved."

    return {
        "answer": suggestion,
        "top_match": {
            "title": top.title,
            "description": top.description,
            "category": top.category
        },
        "confidence": float(score)
    }