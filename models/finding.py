class Finding:

    def __init__(
        self,
        service,
        issue,
        severity,
        recommendation
    ):
        self.service = service
        self.issue = issue
        self.severity = severity
        self.recommendation = recommendation


    def to_dict(self):

        return {
            "service": self.service,
            "issue": self.issue,
            "severity": self.severity,
            "recommendation": self.recommendation
        }