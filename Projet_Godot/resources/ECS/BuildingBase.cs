using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Godot;
using T3.helpers;
using T3.resources.ECS.components;
using T3.resources.ECS.UI;

namespace T3.resources.ECS
{
    /**
     * <summary>BuildingBase component used as base for differents buildings</summary>
     */
    [Tool]
    public abstract class BuildingBase : Node2D
    {
        /**
         * <summary>Detect the collision to the area2D</summary>
         */
        private static readonly Godot.Collections.Dictionary<BuildingSize.BSize, Vector2[]> CollisionPolygons =
            new Godot.Collections.Dictionary<BuildingSize.BSize, Vector2[]>
            {
                {
                    BuildingSize.BSize.L1,
                    new[]
                    {
                        new Vector2(0, 0), new Vector2(-36, -17), new Vector2(-36, -43), new Vector2(0, -60),
                        new Vector2(35, -43), new Vector2(35, -17)
                    }
                },
                {
                    BuildingSize.BSize.L2,
                    new[]
                    {
                        new Vector2(0, 0), new Vector2(-36, -17), new Vector2(-36, -67), new Vector2(0, -84),
                        new Vector2(35, -67), new Vector2(35, -17)
                    }
                },
                {
                    BuildingSize.BSize.L3,
                    new[]
                    {
                        new Vector2(0, 0), new Vector2(-36, -17), new Vector2(-36, -91), new Vector2(0, -108),
                        new Vector2(35, -91), new Vector2(35, -17)
                    }
                }
            };

        /**
         * <summary>List of components used for the building</summary>
         */
        [Export] private List<NodePath> _components = new List<NodePath>();

        /**
         * <summary>Canvas player for context menu</summary>
         */
        private CanvasLayer _layer = new CanvasLayer();

        /**
         * <summary>Zone of the mouse</summary>
         */
        private Area2D _mouseZone;

        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            // Get nodes
            _mouseZone = GetNode<Area2D>("Area2D");

            // connect events
            _mouseZone.Connect("input_event", this, nameof(OnArea2DInputEvent));
            if (this.TryGetComponent<BuildingSize>(out var s))
            {
                s.Connect("OnSizeChanged", this, nameof(OnSizeChanged));
                OnSizeChanged(s.Size);
            }
        }

        /**
         * <returns>The building size</returns>
         */
        public BuildingSize.BSize GetSize()
        {
            return BuildingSize.BSize.L1;
        }

        /**
         * <summary>List of node</summary>
         */
        private static IEnumerable<T> ToList<T>(IEnumerable array) where T : Node
        {
            return array.Cast<T>().ToList();
        }

        /**
         * <summary>Get the building type name</summary>
         * <returns>The building name</returns>
         */
        protected new abstract string GetName();

        /**
         * <summary>Manage the Building statistics</summary>
         */
        public abstract Godot.Collections.Dictionary<BuildingStats.Stats, double> ManageStats();

        /**
         * <summary>Get the building type description</summary>
         * <returns>The building description</returns>
         */
        protected abstract string GetDescription();

        /**
         * <summary>Open the building content menu</summary>
         * <param name="coordinates">The mouse coordinates</param>
         */
        private void ShowContext(Vector2 coordinates)
        {
            // Delete and recreate a canvas layer
            _layer?.QueueFree();
            _layer = new CanvasLayer();

            // Create the context menu instance and place it
            var m = GD.Load<PackedScene>("res://resources/ECS/UI/ContextMenu.tscn").Instance();
            if (!(m is ContextMenu m2)) return;
            m2.RectPosition = coordinates;

            // Add it as a child of the canvas layer
            _layer.AddChild(m2);
            AddChild(_layer);

            // Set context informations
            m2.Text = GetName();
            m2.Info = GetDescription();
            m2.Renov = this.TryGetComponent<BuildingHealth>(out var state) &&
                       state.State == BuildingHealth.BuildingState.Old;
        }
        
        /**
         * <summary>Clique sur l'area2d</summary>
         * <param name="viewport">Fenêtre</param>
         * <param name="event">Évenement</param>
         * <param name="shapeIndex">Index of the shape</param>
         */
        public void OnArea2DInputEvent(Node viewport, InputEvent @event, int shapeIndex)
        {
            // If the event is a mouse right click and is not an echo of a previous event
            if (!(@event is InputEventMouseButton mouse) || mouse.IsEcho() ||
                !mouse.IsActionPressed("ui_cancel")) return;

            // Show the context
            ShowContext(mouse.Position);
        }

        /**
         * <summary>Lors du changement de taille</summary>
         * <param name="size">Nouvel taille</param>
         */
        public void OnSizeChanged(BuildingSize.BSize size)
        {
            var collider = _mouseZone.GetChild<CollisionPolygon2D>(0);
            if (CollisionPolygons.ContainsKey(size)) collider.Polygon = CollisionPolygons[size];
        }
    }
}