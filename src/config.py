"""All tunable parameters for the pipeline, each with a why-comment. See SPEC Section 4."""

RANDOM_SEED = 42  # fixed so splits, sampling, and models are reproducible

IP_ON = 50e3  # A; plasma current above this counts as "plasma exists" (t_start)
WINDOW_MS = 20  # feature window length; long enough to see a slope, short enough to stay local
STRIDE_MS = 5  # step between window ends; finer than WINDOW_MS so windows overlap
HORIZON_MS = 30  # positive-label horizon; how far before t_disrupt we want the model to warn
K_CONSEC = 2  # consecutive over-threshold windows required to raise an alarm, to reject single-window noise
MIN_WARNING_MS = 5  # an alarm firing closer than this to t_disrupt isn't useful ("tardy", not "caught")

CQ_DROP_FRAC = 0.8  # current-quench detector: |Ip| must fall by this fraction of its value at t...
CQ_MAX_MS = 10  # ...within this many ms, distinguishing a quench from a slow controlled ramp-down

MIN_PEAK_IP = 100e3  # A; shots whose |Ip| never exceeds this never really formed a plasma, so skip them
