from aws.aws_session import (
    create_session,
    verify_connection
)

from aws.iam_checks import run_iam_checks


def main():

    print("=" * 50)

    print(
        "Cloud Security Posture Assessment Tool"
    )

    print("=" * 50)


    print("\nChecking AWS connection...\n")


    session = create_session()


    if session:

        connected = verify_connection(session)

        if connected:

            print(
                "\n✓ Connected successfully"
            )


            print(
                "\nRunning IAM assessment...\n"
            )


            findings = run_iam_checks(session)


            if findings:

                for finding in findings:
                    print(finding.to_dict())

            else:

                print(
                    "No IAM findings detected."
                )


        else:

            print(
                "\n✗ AWS connection failed"
            )


    else:

        print(
            "\n✗ Unable to create AWS session"
        )



if __name__ == "__main__":
    main()