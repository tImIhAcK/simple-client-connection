from tqdm import tqdm

def progress(filename, size, sent):
    """Progress function for uploads and downloads"""
    # Sizes are given in bytes. COnverting to MB
    size_mb = size / (1024 * 1024)
    sent_mb = sent / (1024 * 1024)
    progress_bar = tqdm(range(int(size_mb)))
    n = int(sent_mb)
    for i in range(n):
        progress_bar.update(1)