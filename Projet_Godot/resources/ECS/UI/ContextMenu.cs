using Godot;
using T3.resources.ECS.entities;
using T3.resources.ui;

namespace T3.resources.ECS.UI
{
    /**
     * <summary>Building context menu gameobject that will be show when right click on a building</summary>
     */
    public class ContextMenu : PanelContainer
    {
        /**
         * <summary>Label for the context content</summary>
         */
        private RichTextLabel _infoLabel;

        /**
         * <summary>Label for the context title</summary>
         */
        private Label _nameLabel;

        [Export] private NodePath _renovBtnPath, _nameLabelPath, _infoLabelPath;

        private Button _renovButton;
        private Control _renovMenu;

        /**
         * <summary>Context text title</summary>
         */
        public string Text
        {
            get => _nameLabel.Text;
            set => SetText(value);
        }

        /**
         * <summary>Context text content</summary>
         */
        public string Info
        {
            get => _infoLabel.Text;
            set => SetInfo(value);
        }

        /**
         * <summary>Context Rénovation</summary>
         */
        public bool Renov
        {
            get => _renovButton.Visible;
            set => _renovButton.Visible = value;
        }

        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            // Get nodes from the current scene
            _nameLabel = GetNode<Label>(_nameLabelPath);
            _infoLabel = GetNode<RichTextLabel>(_infoLabelPath);
            _renovButton = GetNode<Button>(_renovBtnPath);
            if (GetParent().GetParent<BuildingBase>() is Building)
            {
                _renovMenu = GetTree().CurrentScene.GetNode<RenovHab>("Interfaces/RenovHab");
            }
            else
            {
                _renovMenu = GetTree().CurrentScene.GetNode<RenovAdmin>("Interfaces/RenovAdmin");
            }

            // Connect event
            _renovButton.Connect("pressed", this, nameof(OnRenovBtnPressed));
        }

        /**
         * <summary>Input</summary>
         */
        public override void _Input(InputEvent @event)
        {
            // If the event is a right click and the event is not an echo of a previous event
            if (!(@event is InputEventMouseButton button) || button.IsEcho() ||
                button.IsActionReleased("ui_cancel")) return;

            // If the mouse position is outside the context box, delete itself
            if (!GetRect().HasPoint(button.Position)) GetParent().QueueFree();
        }

        /**
         * <summary>Set the context title</summary>
         * <param name="value">The new title</param>
         */
        private void SetText(string value)
        {
            _nameLabel.Text = value;
        }

        /**
         * <summary>Set the context content info</summary>
         * <param name="value">The new content</param>
         */
        private void SetInfo(string value)
        {
            _infoLabel.BbcodeText = value;
        }

        /**
         * <summary>Press Button</summary>
         */
        private void OnRenovBtnPressed()
        {
            var bBase = GetParent().GetParent<BuildingBase>();
            if (bBase is Building)
                ((RenovHab) _renovMenu).ShowMenu(bBase);
            else
                ((RenovAdmin) _renovMenu).ShowMenu(bBase);
            GetParent().QueueFree();
        }
    }
}