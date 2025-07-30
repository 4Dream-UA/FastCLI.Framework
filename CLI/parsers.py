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
        if multitypes:
            for param_key, param_value in params.items():
                params[param_key] = ast.literal_eval(param_value)

        return params