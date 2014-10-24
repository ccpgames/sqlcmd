import argparse

import pytds


def execute_sql_file(
    server,
    login_id,
    password,
    database,
    input_file,
):

    dbconn = pytds.connect(
        server=server,
        database=database,
        user=login_id,
        password=password,
        autocommit=True,
        appname="python-sqlcmd",
        row_strategy=pytds.namedtuple_row_strategy,
    )

    cursor = dbconn.cursor()
    for msgclass, msg in cursor.messages:
        print msg.message

    print "Executing", input_file
    with open(input_file, "r") as sqlfile:
        sqltext = sqlfile.read()

    blocks = sqltext.split("\nGO\n")

    # Strip trailing GO statement
    if not blocks[-1]:
        del blocks[-1]

    for i, block in enumerate(blocks):
        print ">>> executing block {} of {}".format(i + 1, len(blocks))
        ##print block
        cursor.execute(block)
        for msgclass, msg in cursor.messages:
            print msg.message


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-S', '--server', action='store', nargs='?', default=None,
        help="Server."
    )

    parser.add_argument(
        '-U', '--login-id', action='store', nargs='?', default=None,
        help="Login ID."
    )

    parser.add_argument(
        '-P', '--password', action='store', nargs='?', default="",
        help="Password."
    )

    parser.add_argument(
        '-d', '--database', action='store', nargs='?', default=None,
        help="Use database name."
    )

    parser.add_argument(
        '-i', '--input-file', action='store', nargs='?', default="CON",
        help="Input file."
    )

    args = parser.parse_args()

    execute_sql_file(
        server=args.server,
        login_id=args.login_id,
        password=args.password,
        database=args.database,
        input_file=args.input_file,
    )


if __name__ == "__main__":
    main()
