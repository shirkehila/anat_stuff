def log_duration(duration, output_file_path):
    print(duration)
    with open(output_file_path, 'w') as f:
        print(duration, file=f)