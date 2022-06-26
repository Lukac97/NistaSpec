import hash_module


if __name__ == "__main__":
    hash = hash_module.hash_password("loptica")
    print(hash_module.check_password(hash, "loptica"))
