from models.finding import Finding


def run_iam_checks(session):

    findings = []

    iam = session.client("iam")

    response = iam.list_users()


    for user in response["Users"]:

        findings.append(
            Finding(
                "IAM",
                f"IAM user found: {user['UserName']}",
                "INFO",
                "Review user permissions"
            )
        )


    return findings