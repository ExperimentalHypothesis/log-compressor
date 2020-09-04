import os, gzip


def compress_to_gzip(path_to_log_dir: str) -> None:
    """ Compress log files to Gzip. Specify the path to directory where logs are stored. """
    for pth, dirs, folders in os.walk(path_to_log_dir):
        for file in folders:
            if os.path.join(pth, file).endswith(".gz"):
                continue
            try:
                with open(os.path.join(pth, file), "rb") as f_input:
                    with gzip.open(os.path.join(pth, file) + ".gz", "wb") as f_output:
                        f_output.writelines(f_input)
                        os.remove(os.path.join(pth, file))
            except PermissionError: 
                print(f"Permission error for: {os.path.join(pth, file)}")
            except Exception as e:
                print(f"Unknown error: {e}")


if __name__ == "__main__":
    path_to_log_dir = "/var/log"
    compress_to_gzip(path_to_log_dir)