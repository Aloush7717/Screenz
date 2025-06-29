import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple HR Bot skeleton.")
    subparsers = parser.add_subparsers(dest="command")

    greet_parser = subparsers.add_parser("greet", help="Send a greeting")
    greet_parser.add_argument("name", help="Name of the person to greet")

    args = parser.parse_args()

    if args.command == "greet":
        print(f"Hello {args.name}, how can I assist you with HR tasks today?")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
