#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from __future__ import division
from psychopy import visual, core

from display.rsvp_disp_modes import CalibrationTask
from helpers.triggers import _write_triggers_from_sequence_calibration

# Initialize Stimulus Parameters
# Task Bar
color_task = 'White'
font_task = 'Times'
height_task = 0.1
text_task = '0/100'

# Text Bar
color_text = 'white'
font_text = 'Times'

pos_text = (0, -.75)
text_text = 'Demo For Calibration Task'
txt_height = 0.1

# Stimuli
font_sti = 'Times'
pos_sti = (0, 0)
sti_height = 0.6

tr_pos_bg = (0, .5)
bl_pos_bg = (-1, -.5)
size_domain_bg = 7
color_bg_txt = 'red'
font_bg_txt = 'Arial'
color_bar_bg = 'green'

# Initialize Stimulus
is_txt_sti = True
is_presentation_by_images = False

if is_txt_sti:
    ele_sti = [
        ['B', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '<', '-', 'L'],
        ['E', '+', 'F', 'G', 'E', '-', 'S', 'Q', 'W', 'E', '<', 'A', 'Z'],
        ['W', '+', 'F', 'G', 'E', '-', 'S', 'Q', 'W', 'E', '<', 'A', 'Z'],
        ['Q', '+', 'F', 'G', 'E', '-', 'S', 'Q', 'W', 'E', '<', 'A', 'Z']]
    color_sti = [['green', 'red', 'white', 'white', 'white', 'white', 'white',
                  'white', 'white', 'white', 'white', 'white', 'white']] * 4
elif not is_presentation_by_images:
    ele_sti = [['static/images/RSVP_images/A.jpg',
                'static/images/RSVP_images/Red_Cross.png',
                'static/images/RSVP_images/C.jpg',
                'static/images/RSVP_images/D.jpg',
                'static/images/RSVP_images/E.jpg',
                'static/images/RSVP_images/P.jpg'],
               ['static/images/RSVP_images/T.jpg',
                'static/images/RSVP_images/Red_Cross.png',
                'static/images/RSVP_images/B.jpg',
                'static/images/RSVP_images/C.jpg',
                'static/images/RSVP_images/D.jpg',
                'static/images/RSVP_images/E.jpg']]
else:
    ele_sti = [['./display/RSVP_presentation_by_images/blow_bubbles.png',
                'static/images/RSVP_images/Red_Cross.png',
                './display/RSVP_presentation_by_images/hike.png',
                './display/RSVP_presentation_by_images/hunt.png',
                './display/RSVP_presentation_by_images/hunt150.png',
                './display/RSVP_presentation_by_images/hunt175.png',
                ],
               ['./display/RSVP_presentation_by_images/kick.png',
                'static/images/RSVP_images/Red_Cross.png',
                './display/RSVP_presentation_by_images/pass_out.png',
                './display/RSVP_presentation_by_images/Penguins.png',
                './display/RSVP_presentation_by_images/kick.png',
                './display/RSVP_presentation_by_images/put_out_fire_3.png'
                ]]

    '''
    Complete list of images:
    ['./display/RSVP_presentation_by_images/blow_bubbles.png', './display/RSVP_presentation_by_images/bounce_on_ball.png', './display/RSVP_presentation_by_images/carve_pumpkin.png', './display/RSVP_presentation_by_images/destroy_smash.png', './display/RSVP_presentation_by_images/digest_swallow.png', './display/RSVP_presentation_by_images/escape.png', './display/RSVP_presentation_by_images/escapesmall.png', './display/RSVP_presentation_by_images/escapesmall2.png', './display/RSVP_presentation_by_images/fight.png', './display/RSVP_presentation_by_images/fightsmall.png', './display/RSVP_presentation_by_images/fishing.png', './display/RSVP_presentation_by_images/fishingsmall.png', './display/RSVP_presentation_by_images/food_fight.png', './display/RSVP_presentation_by_images/forvandle_poff.png', './display/RSVP_presentation_by_images/hike.png', './display/RSVP_presentation_by_images/hikesmall150.png', './display/RSVP_presentation_by_images/hot_air_balloon_launch.png', './display/RSVP_presentation_by_images/hunt.png', './display/RSVP_presentation_by_images/hunt150.png', './display/RSVP_presentation_by_images/hunt175.png', './display/RSVP_presentation_by_images/iditarod_race_verb.png', './display/RSVP_presentation_by_images/juggle.png', './display/RSVP_presentation_by_images/kayaking.png', './display/RSVP_presentation_by_images/kick.png', './display/RSVP_presentation_by_images/kidnap.png', './display/RSVP_presentation_by_images/pass_out.png', './display/RSVP_presentation_by_images/Penguins.png', './display/RSVP_presentation_by_images/pull_hair.png', './display/RSVP_presentation_by_images/put_out_fire_3.png', './display/RSVP_presentation_by_images/rescue_dolphin.png', './display/RSVP_presentation_by_images/row_gondola.png', './display/RSVP_presentation_by_images/spaceSymbol.png', './display/RSVP_presentation_by_images/steal_wallet.png', './display/RSVP_presentation_by_images/Thumbs-up-icon.png', './display/RSVP_presentation_by_images/toast_glasses.png', './display/RSVP_presentation_by_images/whine.png', './display/RSVP_presentation_by_images/wink.png']

    '''

time_flash = .25
time_target = 2
time_cross = .6

timing_sti = [[time_target] + [time_cross] + [time_flash] *
              (len(ele_sti[0]) - 1)] * 4

task_text = ['1/100', '2/100', '3/100', '4/100']
task_color = [['white'], ['white'], ['white'], ['white']]

# Initialize decision
ele_list_dec = [['[<]'], ['[R]']]

# Initialize Window
win = visual.Window(size=[500, 500], fullscr=False, screen=0, allowGUI=False,
                    allowStencil=False, monitor='testMonitor', color='black',
                    colorSpace='rgb', blendMode='avg',
                    waitBlanking=True)
win.recordFrameIntervals = True
frameRate = win.getActualFrameRate()

print frameRate

# Initialize Clock
clock = core.StaticPeriod(screenHz=frameRate)
experiment_clock = core.MonotonicClock(start_time=None)

rsvp = CalibrationTask(window=win, clock=clock,
                       experiment_clock=experiment_clock,
                       text_information=text_text,
                       color_information=color_text, pos_information=pos_text,
                       height_information=txt_height,
                       font_information=font_text,
                       color_task=['white'],
                       font_task=font_task, text_task=task_text[0],
                       height_task=height_task,
                       font_sti=font_sti, pos_sti=pos_sti,
                       sti_height=sti_height,
                       ele_list_sti=['a'] * 10, color_list_sti=['white'] * 10,
                       time_list_sti=[3] * 10,
                       tr_pos_bg=tr_pos_bg, bl_pos_bg=bl_pos_bg,
                       size_domain_bg=size_domain_bg,
                       color_bg_txt=color_bg_txt, font_bg_txt=font_bg_txt,
                       color_bar_bg=color_bar_bg,
                       is_txt_sti=is_txt_sti)

# uncomment trigger_file lines for demo with triggers!
# trigger_file = open('calibration_triggers.txt','w')
for idx_o in range(len(task_text)):

    rsvp.update_task_state(text=task_text[idx_o], color_list=task_color[idx_o])
    rsvp.draw_static()
    win.flip()
    rsvp.sti.height = sti_height

    # Schedule a sequence
    rsvp.ele_list_sti = ele_sti[idx_o]

    if is_txt_sti:
        rsvp.color_list_sti = color_sti[idx_o]

    rsvp.time_list_sti = timing_sti[idx_o]

    core.wait(.4)
    sequence_timing = rsvp.do_sequence()

    # _write_triggers_from_sequence_calibration(sequence_timing, trigger_file)

    core.wait(.5)

# close the window and trigger_file
win.close()
# trigger_file.close()

# Print intervals
# intervalsMS = np.array(win.frameIntervals) * 1000
# print(intervalsMS)
