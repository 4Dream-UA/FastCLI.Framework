class BaseValidater:

    @staticmethod
    def validate_not_args(args: list) -> bool:
        if not args:
            return True
        return False

    @staticmethod
    def validate_not_func(func: callable) -> bool:
        if not func:
            return True
        return False