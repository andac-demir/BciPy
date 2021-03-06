from itertools import cycle
from bcipy.tasks.task import Task
from bcipy.tasks.rsvp.calibration.calibration import RSVPCalibrationTask


class RSVPTimingVerificationCalibration(Task):
    """RSVP Calibration Task that for verifying timing.

    Input:
        win (PsychoPy Display Object)
        daq (Data Acquisition Object)
        parameters (Dictionary)
        file_save (String)

    Output:
        file_save (String)
    """
    TASK_NAME = 'RSVP Timing Verification Task'

    def __init__(self, win, daq, parameters, file_save):
        super(RSVPTimingVerificationCalibration, self).__init__()
        parameters['stim_height'] = 0.8
        parameters['stim_pos_y'] = 0.2
        self._task = RSVPCalibrationTask(win, daq, parameters, file_save)
        self._task.generate_stimuli = self.generate_stimuli

    def generate_stimuli(self):
        """Generates the sequences to be presented.
        Returns:
        --------
            tuple(
                samples[list[list[str]]]: list of sequences
                timing(list[list[float]]): list of timings
                color(list(list[str])): list of colors)
        """
        samples, times, colors = [], [], []

        solid_box = '\u25A0'
        empty_box = '\u25A1'

        target = 'x'  # solid_box  # 'X'
        fixation = '\u25CB'  # circle

        # alternate between solid and empty boxes
        letters = cycle([solid_box, empty_box])
        time_target, time_fixation, time_stim = self._task.timing
        color_target, color_fixation, color_stim = self._task.color

        seq_len = self._task.stim_length
        seq_stim = [target, fixation, *[next(letters) for _ in range(seq_len)]]
        seq_times = [time_target, time_fixation, *[time_stim for _ in range(seq_len)]]
        seq_colors = [color_target, color_fixation, *[color_stim for _ in range(seq_len)]]

        for _ in range(self._task.stim_number):
            samples.append(seq_stim)
            times.append(seq_times)
            colors.append(seq_colors)

        return (samples, times, colors)

    def execute(self):
        self.logger.debug(f'Starting {self.name()}!')
        self._task.execute()

    @classmethod
    def label(cls):
        return RSVPTimingVerificationCalibration.TASK_NAME

    def name(self):
        return RSVPTimingVerificationCalibration.TASK_NAME
