from fasthell.cli.cli import CLI


cli = CLI()


@cli.command("greeting", multitypes=True)
def greet_list(people: list, people_count: int) -> int:
    """
    :param people:
    :param people_count:
    :return int:

    This function print greet text for `people`
    `people_count` time and return how many people
    are not greet today.
    """

    people_len = len(people)
    if people_count > people_len:
        raise AssertionError("people_count > people_len")
    if people is False:
        return 0
    if people_count < 1:
        return 0


    for index in range(people_count):
        print(f"Hello, {people[index]}!")

    return len(people) - people_count

if __name__ == "__main__":
    # python example1_simple.py greeting
    # /: people=["Yevhen", "Vladimir", "Ruslan"] people_count=2 :/
    cli.main()
