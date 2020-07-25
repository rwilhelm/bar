#!/usr/bin/env python

from asyncio import sleep
from colour import Color
from math import ceil
from pulsectl import Pulse, PulseEventInfo
from re import compile
from shared.fmt import Action, fmt
from shared.log import get_logger


logger = get_logger('pulse')

def fire(val):
    rev = True if val > 100 else False
    gradient = list(Color("grey").range_to(Color("orange"), 100))

    try:
        fg = gradient[round(val-1)].hex
    except IndexError:
        fg = 'white'
        pass

    colors = {'fg': fg, 'rev': rev}
    return colors

#async def pulseaudio2():
#    with Pulse('event-printer') as pulse:
#        # print('Event types:', pulsectl.PulseEventTypeEnum)
#        # print('Event facilities:', pulsectl.PulseEventFacilityEnum)
#        # print('Event masks:', pulsectl.PulseEventMaskEnum)
#
#        def print_events(ev):
#            print('Pulse event:', ev)
#            ### Raise PulseLoopStop for event_listen() to return before timeout (if any)
#            # raise pulsectl.PulseLoopStop
#
#        # def print_events2(ev_t, ev_fac, idx):
#        #     print('Pulse event:', ev_t, ev_fac, idx)
#        #     # await sleep(2)
#        #     ### Raise PulseLoopStop for event_listen() to return before timeout (if any)
#        #     # raise pulsectl.PulseLoopStop
#
#        pulse.event_mask_set('all')
#        pulse.event_callback_set(print_events)
#        pulse.event_listen(timeout=10)
#
#        yield pulse
#        # await sleep(2)


async def pulseaudio():
    p = Pulse('HELLO_FROM_BAR_PULSEAUDIO')

    states = {
        'idle': {
            'colors': {
                'fg': 'grey'
            }
        },
        'invalid': {
            'colors': {
                'fg': 'black',
                'bg': 'red'
            }
        },
        'running': {
            'colors': {
                'fg': 'white'
            }
        },
        'suspended': {
            'colors': {
                'fg': 'grey'
            }
        }
    }

    while True:
        out = []

        try:
            for source in p.sink_input_list()[1:]:
                index = source.index
                volume = int(float(source.volume.value_flat) * 100)

                actions = [
                    Action(1, "pactl set-sink-input-volume {} 100%".format(index)),
                    Action(2, "pactl set-sink-input-mute {} toggle".format(index)),
                    Action(3, "pavucontrol&".format()),
                    Action(4, "pactl set-sink-input-volume {} +10%".format(index)),
                    Action(5, "pactl set-sink-input-volume {} -10%".format(index)),
                ]

                if source.mute == 1:
                    colors = {'fg': 'grey'}
                else:
                    colors = fire(volume)

                out.append(fmt(volume, colors=colors, actions=actions, pad=""))

        except Exception as e:
            pass
        #except pulsectl.pulsectl.PulseOperationFailed as e:
        #    if e == 158:
        #        pass



        #for sink in p.sink_list():

        #    if sink.description == 'Built-in Audio Analog Stereo':
        #        colors = {'fg': 'yellow'}
        #    elif sink.description == 'PCM2902 Audio Codec Analog Stereo':
        #        colors = {'fg': 'cyan'}
        #    else:
        #        colors = {'fg': 'white'}

        #    # sink_state = sink
        #    # print(sink_state)

        #    volume = int(float(sink.volume.value_flat) * 100)

        #    actions = [
        #        Action(1, "pactl set-sink-volume {} 100%".format(sink.index)),
        #        Action(2, "pactl set-sink-mute {} toggle".format(sink.index)),
        #        Action(3, "pavucontrol&".format()),
        #        Action(4, "pactl set-sink-volume {} +10%".format(sink.index)),
        #        Action(5, "pactl set-sink-volume {} -10%".format(sink.index)),
        #    ]

        #    if sink.mute == 1:
        #        colors = {'fg': 'grey'}
        #    else:
        #        colors = fire(volume)

        #    out.append(fmt(volume, colors=colors, actions=actions, pad=""))

        # yield fmt(list(map(lambda x: str(x).strip(), out)))

        yield fmt(" ".join(out))
        await sleep(0.5)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
