from pls.args import args


PIPE = "│"
TEE = "├"
BEND = "└"
DASH = "─"
NONE = ""

# Pre shapes
PIPE_SPACE = f"{PIPE} "
SPACE_SPACE = "  "
if not args.no_align:
    PIPE_SPACE = f"{PIPE_SPACE} "
    SPACE_SPACE = f"{SPACE_SPACE} "

# Last shapes
TEE_DASH = f"{TEE}{DASH}"
BEND_DASH = f"{BEND}{DASH}"