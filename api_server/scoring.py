def score_output(output):
    score = 0

    # Simple heuristic scoring
    if len(output) > 50:
        score += 1
    if "-" in output or "•" in output:
        score += 1
    if len(output.split()) < 120:
        score += 1

    return score