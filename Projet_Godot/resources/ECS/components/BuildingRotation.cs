using Godot;

namespace T3.resources.ECS.components
{
    /**
     * <summary>BuildingRotation component</summary>
     */
    public class BuildingRotation : BaseComponent
    {
        /**
         * <summary>Signal sent every time the rotation is changed</summary>
         * <param name="rotation">The new building rotation</param>
         */
        [Signal]
        public delegate void OnRotationChanged(BRotation rotation);

        /**
         * <summary>Rotation direction</summary>
         */
        public enum BRotation
        {
            North,
            South,
            East,
            West
        }

        /**
         * <summary>Current rotation of the building</summary>
         * <returns>Rotation State</returns>
         */
        [Export]
        public BRotation Rotation { get; private set; } = BRotation.South;

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

        /**
         * <summary>Change the rotation of the building and emit a signal</summary>
         * <param name="newRotation">The new rotation of the building</param>
         */
        public void ChangeRotation(BRotation newRotation)
        {
            Rotation = newRotation;
            EmitSignal(nameof(OnRotationChanged), newRotation);
        }
    }
}