using System;
using System.Collections.Generic;
using Godot;

namespace T3.scenes
{
    /**
     * <summary>Manage music of the game</summary>
     */
    public class AudioPlayer : AudioStreamPlayer2D
    {
        /**
         * <summary>Random used to select the music</summary>
         */
        private readonly Random _rnd = new Random();

        /**
         * <summary>Previous music</summary>
         */
        private int _oldIndex;

        /**
         * <summary>List of audio stream containing musics</summary>
         */
        [Export] private List<AudioStream> _streams = new List<AudioStream>();


        /**
         * <summary>Called when the node enters the scene tree for the first time.</summary>
         */
        public override void _Ready()
        {
            Connect("finished", this, nameof(OnFinished));
        }

        /**
         * <summary>Called when the game start to run musics</summary>
         */
        public void OnPlayGame()
        {
            if (_streams.Count <= 0) return;
            // Select the next musics
            _oldIndex = _rnd.Next(_streams.Count);
            // Set the audio steam and volume and finally play the music
            Stream = _streams[_oldIndex];
            GD.Print("Now PLaying : " + Stream.ResourcePath);
            Play();
        }

        /**
         * <summary>Called when the current music is finished to called the next one</summary>
         */
        public void OnFinished()
        {
            // Select the next music
            var index = _rnd.Next(_streams.Count);
            // Ask the ID again if the ID is the same than the current one
            while (index == _oldIndex && _streams.Count > 1) index = _rnd.Next(_streams.Count);
            // Change the index, set the audio stream and play it.
            _oldIndex = index;
            Stream = _streams[index];
            Play();
        }

        public void SetVolume(float value)
        {
            VolumeDb = value * 44 / 100 - 40f;
        }
    }
}