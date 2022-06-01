using Godot;

namespace T3.resources.ECS.components
{
    /**
     * <summary>BuildingSize component</summary>
     */
    public class BuildingSize : BaseComponent
    {
        /**
         * <summary>Signal sent every time the size is changed</summary>
         * <param name="s">The new building size</param>
         */
        [Signal]
        public delegate void OnSizeChanged(BSize s);

        /**
         * <summary>Different Building sizes</summary>
         */
        public enum BSize
        {
            L1,
            L2,
            L3
        }

        /**
         * <summary>The current building size</summary>
         * <param name="s">The new building size</param>
         */
        [Export]
        public BSize Size { get; private set; } = BSize.L1;

        /**
         * <summary>Change the size</summary>
         */
        public void ChangeSize(BSize s)
        {
            Size = s;
            EmitSignal(nameof(OnSizeChanged), s);
        }

        /**
         * <summary>Convert to int</summary>
         */
        public static int ToInt(BSize s)
        {
            switch (s)
            {
                case BSize.L1:
                    return 1;
                case BSize.L2:
                    return 2;
                default:
                    return 3;
            }
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