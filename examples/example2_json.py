from fasthell.cli.cli import CLI
import json


cli = CLI()

@cli.command("make_json", alias=["mjson"], _return=False, multitypes=True)
def make_json_from_dict(data: dict, file: str = "json.json") -> bool:
    """
    :param data:
    :param file:
    :return bool:

    Function that make from python dictionary
    a json file.
    """

    try:
        print(type(data))
        with open(file, "w", encoding="utf-8") as fn:
            json.dump(data, fn, ensure_ascii=False, indent=4)
        print(f"[OK] JSON saved in {file}")
        return True
    except Exception as e:
        print(f"[ERROR] {e}")
        return False


if __name__ == "__main__":
    # python example1_simple.py mjson
    # make_json /: data="{'name': 'John', 'age': 30}" :/
    cli.main()
