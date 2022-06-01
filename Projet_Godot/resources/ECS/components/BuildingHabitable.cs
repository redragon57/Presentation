using Godot;
using T3.helpers;

namespace T3.resources.ECS.components
{
    /**
     * <summary>BuildingHabitable component</summary>
     */
    public class BuildingHabitable : BaseComponent
    {
        /**
         * <summary>Signal sent every time the resident count is changed</summary>
         * <param name="count">The new resident count</param>
         */
        [Signal]
        public delegate void OnResidentsCountChanged(int count);

        /**
         * <summary>The maximum residents count</summary>
         */
        [Export(PropertyHint.Range, "1,50,1")]
        public int MaxResidentsCount { get; private set; }

        /**
         * <summary>The resident count</summary>
         */
        [Export]
        public int ResidentsCount { get; private set; }

        /**
         * <summary>Change the resident count and emit a signal</summary>
         * <param name="newCount">The new resident count to set</param>
         */
        public void ChangeResidentsCount(int newCount)
        {
            ResidentsCount = newCount;
            EmitSignal(nameof(OnResidentsCountChanged), newCount);
        }

        /**
         * <summary>Init</summary>
         */
        public override void Init()
        {
            if (!GetParent().TryGetComponentInChildren<BuildingSize>(out var sizeComp)) return;

            MaxResidentsCount = (int) sizeComp.Size * 50;
            sizeComp.Connect("OnSizeChanged", this, nameof(OnSizeChanged));
        }

        /**
         * <summary>Update</summary>
         */
        public override void Update()
        {
        }

        /**
         * <summary>OnSizeChanged</summary>
         * <param name="s">The size</param>
         */
        private void OnSizeChanged(BuildingSize.BSize s)
        {
            MaxResidentsCount = (int) s * 50;
        }
    }
}