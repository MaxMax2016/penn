CONFIG = 'crepe-1440-cce-layer-nodropout-normalize-dither'

# Width of a pitch bin
CENTS_PER_BIN = 5  # cents

# Whether to peak-normalize CREPE input audio
CREPE_NORMALIZE = True

# Whether to trade quantization error for noise during inference
DITHER = True

# The dropout rate. Set to None to turn off dropout.
DROPOUT = None

# Loss function
LOSS = 'categorical_cross_entropy'

# Type of model normalization
NORMALIZATION = 'layer'

# Number of pitch bins to predict
PITCH_BINS = 1440
