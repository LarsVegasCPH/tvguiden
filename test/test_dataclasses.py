from tvguiden.tvguiden import Channel


def test_channel():
    channel = Channel("TV2","1")
    assert channel.name == "TV2"
    assert channel.channel_id == "1"

