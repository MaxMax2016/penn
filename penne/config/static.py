"""Config parameters whose values depend on other config parameters"""
import penne


###############################################################################
# Audio parameters
###############################################################################


# Hopsize in seconds
HOPSIZE_SECONDS = penne.HOPSIZE / penne.SAMPLE_RATE


###############################################################################
# Directories
###############################################################################


# Location to save dataset partitions
PARTITION_DIR = penne.ASSETS_DIR / 'partitions'

# Default checkpoint for generation
DEFAULT_CHECKPOINT = penne.ASSETS_DIR / 'checkpoints' / 'default.pt'

# Default configuration file
DEFAULT_CONFIGURATION = penne.ASSETS_DIR / 'configs' / 'default.py'


###############################################################################
# Evaluation
###############################################################################


# Timer for benchmarking generation
TIMER = penne.time.Context()


###############################################################################
# Training parameters
###############################################################################


# Number of samples used during training
NUM_TRAINING_SAMPLES = \
    (penne.NUM_TRAINING_FRAMES - 1) * penne.HOPSIZE + penne.WINDOW_SIZE
