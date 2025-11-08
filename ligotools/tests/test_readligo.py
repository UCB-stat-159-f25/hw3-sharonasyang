import pytest

from ligotools import dq_channel_to_seglist
from ligotools import read_frame

# This test tests the dq_channel_to_seglist function and asserts that the function raises a KeyError when the channel parameter that's passed in does not contain a 'DEFAULT' key.
def testing_channel_seglist():
    channel_dict = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3"
    }
    with pytest.raises(KeyError):
        dq_channel_to_seglist(channel_dict, fs=4096)

# This test tests the read_frame function and asserts that the function raises a TypeError when the ifo parameter is None.
def testing_read_frame():
    filename = "test filename"
    ifo = None

    with pytest.raises(TypeError):
        read_frame(filename, ifo, readstrain=True, strain_chan=None, dq_chan=None, inj_chan=None)