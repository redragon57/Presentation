using Godot;
using T3.helpers;
using T3.resources.ECS.components;

namespace T3.resources.ECS.script
{
    public class AutoSprite : Sprite
    {
        /**
         * <summary>Health associated</summary>
         */
        private BuildingHealth _health;
        
        /**
         * <summary>Rotation associated</summary>
         */
        private BuildingRotation _rotation;
        
        /**
         * <summary>Size associated</summary>
         */
        private BuildingSize _size;

        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            if (GetParent().TryGetComponent<BuildingRotation>(out var r)) _rotation = r;
            if (GetParent().TryGetComponent<BuildingHealth>(out var h)) _health = h;
            if (GetParent().TryGetComponent<BuildingSize>(out var s)) _size = s;
            UpdateSprite();
        }

        /**
         * <summary>Process</summary>
         */
        public override void _Process(float delta)
        {
            UpdateSprite();
        }

        /**
         * <summary>Update sprite</summary>
         */
        private void UpdateSprite()
        {
            var regionRect = RegionRect;
            var position = regionRect.Position;

            position.y = _size != null ? (int) _size.Size * 108.0f : 0;

            if (_health != null)
                position.x = _health.State == BuildingHealth.BuildingState.Upgrading
                    ? 71f * 7
                    : _health != null
                        ? (int) _health.State * 71f
                        : 0f;

            position.x += _rotation != null ? (int) _rotation.Rotation * 71f : 0f;

            regionRect.Position = position;
            RegionRect = regionRect;
        }
    }
}