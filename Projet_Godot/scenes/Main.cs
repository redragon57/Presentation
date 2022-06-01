using Godot;
using T3.resources.ECS;
using T3.resources.ECS.components;
using T3.resources.ui;
using T3.script;

namespace T3.scenes
{
    /**
     * <summary>Main scene of the game</summary>
     */
    public class Main : Node2D
    {
        /**
         * Create the statistic system instance
         */
        private readonly StatisticsSystem _statisticsSystem = new StatisticsSystem();

        private readonly Timer _timer = new Timer();

        private GenMap _genMap;
        private AudioPlayer _musicManager;
        private Control _pauseOverlay;
        private Score _scoreBoard;
        private int _tickCounter;

        [Export] private NodePath scoreBoardPath;

        public override void _Ready()
        {
            // Get nodes
            var ecranDemarage = GetNode<EcranDemarage>("Interfaces/Fond_Demar");
            _musicManager = GetNode<AudioPlayer>("AudioStreamPlayer2D");
            _pauseOverlay = GetNode<Control>("Interfaces/Pause_Overlay");
            _scoreBoard = GetNode<Score>(scoreBoardPath);

            // Connect events listener
            ecranDemarage.Connect("PlayGame", _musicManager, nameof(_musicManager.OnPlayGame));
            ecranDemarage.Connect("PlayGame", this, nameof(OnPlayGame));
            ecranDemarage.Connect("VolumeChanged", this, nameof(OnVolumeSliderChanged));

            // Initialize globals variables
            GameManager.WorldTileMap = GetNode<TileMap>("World/World");
            GameManager.TileMap = GetNode<TileMap>("World/Floor");
            GameManager.DecorMap = GetNode<TileMap>("World/Decor");
            GameManager.Camera = GetNode<Camera2D>("Camera2D");
            _genMap = new GenMap(GameManager.TileMap, GameManager.WorldTileMap, GameManager.DecorMap);

            // Initialize statistics system
            _statisticsSystem.Setup(
                GetTree().GetNodesInGroup("building"),
                GameManager.WorldTileMap
            );

            // Toggle menu overlays
            ecranDemarage.Show();
            _pauseOverlay.Hide();

            _statisticsSystem.Update();
            _scoreBoard.Update(_statisticsSystem);

            GameManager.ScoreInitial = _statisticsSystem._statsDictionnaire[BuildingStats.Stats.Score];
            GameManager.SatisfactionInitial = _statisticsSystem._statsDictionnaire[BuildingStats.Stats.Satisfaction];
            // Setup timer timeout
            _timer.Connect("timeout", this, nameof(OnTimeout));

            AddChild(_timer);
            _timer.Start(5);
        }

        public override void _Input(InputEvent @event)
        {
            switch (@event)
            {
                case InputEventKey _ when @event.IsActionPressed("pause"):
                {
                    if (GetTree().Paused)
                    {
                        _timer.Paused = false;
                        _pauseOverlay.Hide();
                        _musicManager.StreamPaused = false;
                        GetTree().Paused = false;
                    }
                    else
                    {
                        _timer.Paused = true;
                        _pauseOverlay.Show();
                        _musicManager.StreamPaused = true;
                        GetTree().Paused = true;
                    }

                    break;
                }
                case InputEventKey _ when @event.IsActionPressed("exit"):
                    GetTree().Quit();
                    break;
                case InputEventKey _ when @event.IsActionPressed("changeMusic"):
                    _musicManager.OnFinished();
                    break;
            }
        }

        private void OnPlayGame()
        {
            GD.Print(GameManager.CountBat);
            _scoreBoard.Show();
        }

        private void OnVolumeSliderChanged(float value)
        {
            _musicManager.SetVolume(value);
        }

        private void OnTimeout()
        {
            GD.Print("Iteration finished: " + _tickCounter);

            // Update the stats system
            GD.Print(_tickCounter);
            // Update the tick count
            _tickCounter++;
            _statisticsSystem.Update();
            _scoreBoard.Update(_statisticsSystem);
            // 10 minutes = (10 * 60 secondes) / 15 sec per iteration
            if (_tickCounter < 10 * 60 / 15)
            {
                _timer.Start(15);
            }
            else
            {
                _timer.Stop();
                FinishGame();
            }
        }

        private void FinishGame()
        {
            GD.Print("You lost the Game");
        }

        public void SetPaused(bool pause)
        {
            _timer.Paused = pause;
        }

        public StatisticsSystem GetStatsSys()
        {
            return _statisticsSystem;
        }

        public int GetTicCounter()
        {
            return _tickCounter;
        }
    }
}