using Godot;
using T3.resources.ECS.entities;
using T3.resources.ECS.UI;

namespace T3.resources.ECS.components
{
    public class BuildingHealth : BaseComponent
    {
        /**
         * <summary>Signal sent every time the building state is changed</summary>
         * <param name="state">The new building state</param>
         * <returns></returns>
         */
        [Signal]
        public delegate void OnStateChanged(BuildingState state);

        /**
         * <summary>Building state</summary>
         */
        public enum BuildingState
        {
            Old,
            Upgrading,
            PlannedToUpgrade,
            UpgradeFinished,
            New
        }

        /**
         * <summary>PackedScene of the upgrade indicator</summary>
         */
        private static readonly PackedScene UpgradeIndicator =
            ResourceLoader.Load<PackedScene>("res://resources/ECS/UI/UpgradeIndicator.tscn");

        /**
         * <summary>Cooldown time a building need to be upgraded</summary>
         */
        [Export(PropertyHint.Range, "0.1,10,0.1")]
        private readonly float _upgradeCooldown = 5.0f;

        /**
         * <summary>Current state of the building</summary>
         */
        [Export]
        public BuildingState State { get; set; } = BuildingState.Old;

        /**
         * <summary>Change the building state and emit a signal</summary>
         */
        public void ChangedState(BuildingState newState)
        {
            State = newState;
            EmitSignal(nameof(OnStateChanged), State);

            if (State == BuildingState.Upgrading) CallDeferred(nameof(SpawnIndicator), _upgradeCooldown);
        }

        /**
         * <summary>Spawn the upgrade indicator above the building and start a cooldown</summary>
         * <param name="cooldown">Remaining time for cooldown</param>
         */
        private void SpawnIndicator(float cooldown)
        {
            var indicator = (UpgradeIndicator) UpgradeIndicator.Instance();
            if (indicator == null) return;

            indicator.SetTime(cooldown);
            GetParent().AddChild(indicator);
            indicator.GlobalPosition = ComputeIndicatorPosition();
            indicator.Connect("OnUpgradeFinished", this, nameof(UpdateState));
            indicator.StartCooldown();
        }

        /**
         * <summary>Compute the indicator position to show it properly at the right height</summary>
         * <returns>Global node Position</returns>
         */
        private Vector2 ComputeIndicatorPosition()
        {
            var pos = GetParent<Node2D>().GlobalPosition;
            pos.y -= 71 + (int) GetParent<Building>().GetSize() * 16;
            return pos;
        }

        /**
         * <summary>Method called when the cooldown is finished. Will set the state to finished and emit a signal.</summary>
         */
        private void UpdateState()
        {
            ChangedState(BuildingState.New);
        }

        /**
         * <summary>Init</summary>
         */
        public override void Init()
        {
        }
        
        /**
         * <summary>Update</summary>
         */
        public override void Update()
        {
        }
    }
}