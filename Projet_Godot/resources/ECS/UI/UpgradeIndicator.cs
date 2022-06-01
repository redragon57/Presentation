using Godot;

namespace T3.resources.ECS.UI
{
    /**
     * <summary>Upgrade indicator gameobject used for buildings state</summary>
     */
    public class UpgradeIndicator : Node2D
    {
        /**
         * <summary>Signal sent when the building upgrade is finished</summary>
         */
        [Signal]
        public delegate void OnUpgradeFinished();

        /**
         * <summary>Timer node used for the cooldown</summary>
         */
        private readonly Timer _timer = new Timer();

        /**
         * <summary>The texture for the progress bar</summary>
         */
        private TextureProgress _textureProgress;

        /**
         * <summary>Starting time for the cooldown</summary>
         */
        private float _time = 1;

        /**
         * <summary>Current percentage proportional to the remaining time</summary>
         */
        [Export]
        public int Percent { get; private set; }

        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            // Get nodes
            _textureProgress = GetNode<TextureProgress>("TextureProgress");

            // Added the timer in the current node childs
            AddChild(_timer);
            // Connect to the timer finished event
            _timer.Connect("timeout", this, nameof(OnTimer_timeout));
        }

        /**
         * <summary>Process</summary>
         */
        public override void _Process(float delta)
        {
            // Update the progress texture value
            _textureProgress.Value = _timer.TimeLeft;
        }

        /**
         * <summary>Define the starting time for the timer</summary>
         * <param name="cooldown">Starting time for the cooldown</param>
         */
        public void SetTime(float cooldown)
        {
            _time = cooldown;
        }

        /**
         * <summary>Method called when the timer cooldown has finished</summary>
         */
        private void OnTimer_timeout()
        {
            // Emit the "OnUpgradeFinished" event
            EmitSignal(nameof(OnUpgradeFinished));
            // Delete itself
            QueueFree();
        }

        /**
         * <summary>Start the cooldown</summary>
         */
        public void StartCooldown()
        {
            // Set default values
            _textureProgress.MaxValue = _time;
            _textureProgress.Value = _time;
            _textureProgress.MinValue = 0;

            // Stop the previous timer if running
            if (!_timer.IsStopped()) _timer.Stop();
            // Start the timer
            _timer.Start(_time);
        }
    }
}