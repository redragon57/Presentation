using Godot;

namespace T3.resources.ui
{
    /**
     * <summary>Welcome Screen gameobject</summary>
     */
    public class EcranDemarage : Panel
    {
        /**
         * <summary>Signal sent when the user start the game</summary>
         */
        [Signal]
        public delegate void PlayGame();

        /**
         * <summary>Change of the music volume</summary>
         */
        [Signal]
        public delegate void VolumeChanged(float volume);

        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            // Get menu buttons
            var playBtn = GetNode<Button>("Menu_Demarrage/StartBtn");
            var quitBtn = GetNode<Button>("Menu_Demarrage/QuitBtn");
            var slider = GetNode<Slider>("HSlider");

            // Pause the game process
            GetTree().Paused = true;

            // Connected "pressed" event to buttons
            playBtn.Connect("pressed", this, nameof(OnStartBtnPressed));
            quitBtn.Connect("pressed", this, nameof(OnQuitBtnPressed));
            slider.Connect("value_changed", this, nameof(OnVolumeChanged));
        }

        /**
         * <summary>Called when play button pressed: run the game</summary>
         */
        public void OnStartBtnPressed()
        {
            // Pause the game process
            GetTree().Paused = false;
            // Emit the "PlayGame" event and delete itself
            EmitSignal("PlayGame");
            QueueFree();
        }

        /**
         * <summary>Called when quit button pressed: quit the game</summary>
         */
        public void OnQuitBtnPressed()
        {
            GetTree().Quit();
        }

        /**
         * <summary>Change the music volume</summary>
         */
        public void OnVolumeChanged(float vol)
        {
            EmitSignal(nameof(VolumeChanged), vol);
        }
    }
}