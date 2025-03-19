# name=Alesis V49 MKII

# Транспортная панель
import transport
import midi


# BASIC TRANSPORT CONTROLS

Transport_START = 20

Transport_STOP = 21

Transport_RECORD = 22


def OnMidiMsg(event):

 event.handled = False

 if event.midiId == midi.MIDI_CONTROLCHANGE:

	 # START BUTTON

	 if event.data1 == Transport_START and event.data2 > 0:

		 transport.start()

		 event.handled = True

	 # STOP BUTTON

	 elif event.data1 == Transport_STOP and event.data2 > 0:

		 transport.stop()

		 event.handled = True

	 # RECORD BUTTON`

	 elif event.data1 == Transport_RECORD and event.data2 > 0:

		 transport.record()

		 event.handled = True


# Энкодер переключения каналов
import channels

# Настройки
CC_NUM = 76  # Номер CC энкодера
ENCODER_MAX = 127
SENSITIVITY = 1  # Уменьшили порог для большей плавности

last_channel = -1

def OnControlChange(event):
    global last_channel

    if event.data1 == CC_NUM:
        total_channels = channels.channelCount()
        cc_value = event.data2

        # Если CC = 0 — выбираем первый канал
        if cc_value == 0:
            channels.deselectAll()
            channels.selectChannel(0)
            last_channel = 0
            print(f"Channel selected: 1 (automatic reset at CC=0)")
            event.handled = True
            return

        # Вычисляем индекс канала с более чувствительным шагом для небольшого числа каналов
        if total_channels < 8:
            # Уменьшаем чувствительность, увеличивая шаг на канал
            sensitivity_factor = 127 // (total_channels - 1)  # делим на (total_channels - 1), чтобы оставить последний канал доступным
        else:
            sensitivity_factor = 1

        # Вычисляем канал, принимая во внимание увеличенную чувствительность
        channel_index = int(cc_value / sensitivity_factor)

        # Ограничиваем индекс, чтобы он не выходил за пределы доступных каналов
        if channel_index >= total_channels:
            channel_index = total_channels - 1

        # Проверка чувствительности
        if abs(channel_index - last_channel) >= SENSITIVITY:
            channels.deselectAll()
            channels.selectChannel(channel_index)
            last_channel = channel_index
            print(f"Channel selected: {channel_index + 1}")
            event.handled = True
