import os

def load_env(file_name: str = ".env.sample"):
    try:
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

    except Exception as e:
        print(f"File with name {file_name} is not found")
        raise e