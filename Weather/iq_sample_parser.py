import os
import numpy as np
import argparse


def parse_bin(frame, board) :
    print(f"Parsing frame {frame}, board {board}")

    # Ensure the 'frames' directory exists
    os.makedirs('frames', exist_ok=True)

    # Generate file names
    file_names = [
        (f"frames/rx{0 + (board * 4)}i{frame}.py", f"frames/rx{0 + (board * 4)}q{frame}.py"),
        (f"frames/rx{1 + (board * 4)}i{frame}.py", f"frames/rx{1 + (board * 4)}q{frame}.py"),
        (f"frames/rx{2 + (board * 4)}i{frame}.py", f"frames/rx{2 + (board * 4)}q{frame}.py"),
        (f"frames/rx{3 + (board * 4)}i{frame}.py", f"frames/rx{3 + (board * 4)}q{frame}.py"),
    ]

    # Open files for writing
    files = [(open(i, "w"), open(q, "w")) for i, q in file_names]

    # Initialize files with NumPy array definitions
    for idx, (rx_i, rx_q) in enumerate(files) :
        rx_i.write(f"import numpy as np\nrx{idx}_imag = np.array([")
        rx_q.write(f"import numpy as np\nrx{idx}_real = np.array([")

    bin_file = f'frames/board_{board}frame{frame}.bin'
    print(f"Opening file: {bin_file}")

    # Check if the binary file exists
    if not os.path.isfile(bin_file) :
        print(f"File not found: {bin_file}")
        return

    # Read binary data
    with open(bin_file, 'rb') as f :
        samples = np.fromfile(f, dtype=np.int16)

    print(f"Number of samples: {len(samples)}")
    num_samples = int(len(samples) / 8)
    print(f"Number of sample sets: {num_samples}")

    # Write data to files
    for i in range(num_samples) :
        j = i * 8
        for idx, (rx_i, rx_q) in enumerate(files) :
            rx_q.write(f"{samples[j + 2 * idx]},")
            rx_i.write(f"{samples[j + 2 * idx + 1]},")

    # Finalize files
    for rx_i, rx_q in files :
        rx_q.write("])\n")
        rx_i.write("])\n")
        rx_q.close()
        rx_i.close()


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Process some frames.')
    parser.add_argument('-nframes', dest="nframes", type=int, default=1, help='Number of frames')
    parser.add_argument('-nboards', dest="nboards", type=int, default=1, help='Number of boards')
    args = parser.parse_args()

    for i in range(args.nboards) :
        for j in range(args.nframes) :
            print(f"Parsing board {i} frame {j}")
            parse_bin(j, i)
