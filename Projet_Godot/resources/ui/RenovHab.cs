using System;
using Godot;
using T3.helpers;
using T3.resources.ECS;
using T3.resources.ECS.components;
using T3.scenes;
using T3.script;

namespace T3.resources.ui
{
    public class RenovHab : Control
    {
        /**
         * <summary>Label of the menu renovation menu</summary>
         */
        private Label _label;
        
        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            _button = GetNode<Button>("Menu_Demarrage/VBoxContainer/Ok");
            _label = GetNode<Label>("Menu_Demarrage/VBoxContainer/explication");
            _button.Connect("pressed", this, nameof(OnPressed));
        }

        /**
         * <summary>Show the renovation menu</summary>
         */
        public void ShowMenu()
        {
            var root = GetTree().Root.GetNode<Main>("Main");

            if (ComputeResult(root))
            {
                _label.Text = Helpers.ReplaceVars(_label.Text, "choix", "acceptes");
                if (buildingBase.TryGetComponent<BuildingHealth>(out var health))
                    health.ChangedState(BuildingHealth.BuildingState.Upgrading);
            }
            else
            {
                _label.Text = Helpers.ReplaceVars(_label.Text, "choix", "refuses");
            }

            Show();
        }

        /**
         * <summary>Calcul of the result</summary>
         */
        private bool ComputeResult()
        {
            Hide();
        }
    }
}
