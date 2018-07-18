"""it shows sample usage of the for TextCover."""
#oggpnson #hkhr
from TextCover import Summarizer
from Utility import load_sample_example


if __name__ == "__main__":
    # load sample data for demo purpose.
    sample_example = load_sample_example()
    # instantiate the summarizer.
    summarizer = Summarizer()
    summary = summarizer.summarize(sample_example, distance_threshold=.2,
                                   summary_length=5)
