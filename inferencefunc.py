from inferenceCopy import *

args.checkpoint_path = 'checkpoints/wav2lip_gan.pth'
args.face = '../sample_data/dnef2.jpeg'
args.audio = '../sample_data/tts1.wav'
args.outfile = 'results/result_voice.mp4'

Wav2LipFunc(args.checkpoint_path, args.face, args.audio)
