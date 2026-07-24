from aws.aws_session import (
    create_session,
    verify_connection
)


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