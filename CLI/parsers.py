import ast


class BaseParser:

    @staticmethod
    def parse_params(args: list) -> dict:
        if "/:" not in args or ":/" not in args:
            return {}, args

        start = args.index("/:") + 1
        end = args.index(":/", start)
        params = {
            k.strip(): v.strip('"').strip("'")
            for k, v in (arg.split("=", 1) for arg in args[start:end] if "=" in arg)
        }
        remaining_args = args[end + 1:]

        return params, remaining_args

    @staticmethod
    def parse_multitypes(multitypes: bool, params: dict) -> dict:
        print(params)
        if multitypes:

            for param_key, param_value in params.items():
                try:
                    params[param_key] = ast.literal_eval(param_value)
                except ValueError:
                    params[param_key] = param_value

        return params

    @staticmethod
    def parse_func_info(cmd: str, commands: dict) -> dict:
        func_info = commands.get(cmd)

        if func_info is None:
            for value in commands.values():
                if value["alias"] is None:
                    continue

                if cmd in value["alias"]:
                    func_info = value

        return func_info

    @staticmethod
    def parse_args(argv: list, debugging: bool, fake_args: list) -> list:
        args = argv[0:]
        if debugging and fake_args:
            args = fake_args

        return args

    @staticmethod
    def parse_missing(parameters: dict, params: list, inspect_parameter: callable) -> list:
        return [
            name for name, p in parameters
            if name not in params and p.default is inspect_parameter
        ]

    @staticmethod
    def parse_set_required_exception(sig_parameters: dict, params: list, required: list):
        req_parameters = [name for name, p in sig_parameters if name in params]

        res = list()
        for param in required:
            if param not in req_parameters:
                res.append(param)

        return res
