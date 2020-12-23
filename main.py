import os
from os.path import abspath, join

import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd

from utils import unpack_archived_data


def upload_meta():
    file = os.path.abspath(os.path.join('data', 'subject-info.csv'))
    df = pd.read_csv(file)
    bad_index = df[df['Count quality'] == 0].index
    good_index = df[df['Count quality'] == 1].index
    good_ones = df.drop(bad_index)
    bad_ones = df.drop(good_index)

    print('awerjhf')

    return good_ones, bad_ones


def process_data_with_mne():
    # unpack archive
    unpack_archived_data()
    mne.set_log_level("WARNING")

    # EXAMPLE
    # example file
    # file = abspath(join('data', 'edf', 'Subject09_2.edf'))
    # raw_data = mne.io.read_raw_edf(file, preload=True)
    # raw_data.drop_channels(['ECG ECG'])

    # raw_data.info.set_montage("standard_1020", on_missing='ignore')

    # set custom reference channel
    # raw_data.set_eeg_reference(ref_channels=['EEG Fp1'])
    # raw_data.plot()

    # get data info
    # print(raw_data.info)

    # Plotting spectral density of continuous data
    # raw_data.plot_psd(fmax=50)

    # Plot filtered data


def plot_eeg():
    good, bad = upload_meta()

    for file_name in bad['Subject']:
        file = abspath(join('data', 'edf', f'{file_name}_2.edf'))
        raw_data = mne.io.read_raw_edf(file, preload=True)
        raw_data.drop_channels(['ECG ECG'])

        sfreq = raw_data.info['sfreq']

        data, times = raw_data[1:10, int(sfreq * 1):int(sfreq * 10)]
        # data, times = raw_data[11:20, int(sfreq * 1):int(sfreq * 10)]

        fig = plt.subplots(figsize=(10, 8))
        plt.plot(times, data.T)
        plt.xlabel('Seconds')
        plt.ylabel('$\mu V$')
        plt.title(f'Channels: 1-10 {os.path.basename(file)}')
        # plt.title(f'Channels: 11-20 {os.path.basename(file)}')
        plt.legend(raw_data.ch_names[1:10])
        # plt.legend(raw_data.ch_names[11:20])
        plt.savefig(os.path.join('results', 'bad', f'during_{file_name}'))

        # plt.show()


def eeg_simple_stat():
    good, _ = upload_meta()
    certain_good = [name for name in good['Subject'] if name in ['Subject01', 'Subject07', 'Subject15']]

    for file_name in certain_good:
        file = abspath(join('data', 'edf', f'{file_name}_2.edf'))
        raw_data = mne.io.read_raw_edf(file, preload=True)

        sfreq = raw_data.info['sfreq']
        raw_data.drop_channels(['ECG ECG'])
        O1_channel, times = raw_data[15:16, int(sfreq * 1):int(sfreq * 10)]

        print(np.var(O1_channel.T))


if __name__ == '__main__':
    # process_data_with_mne()
    # plot_eeg()
    eeg_simple_stat()
    # upload_meta()
    # process_with_pyedf()
