using System;
using Godot;
using T3.helpers;
using T3.resources.ECS;
using T3.resources.ECS.components;
using T3.scenes;
using T3.script;

namespace T3.resources.ui
{
    public class RenovAdmin : Control
    {
        private Button _button;
        private Label _label;

        public override void _Ready()
        {
            _button = GetNode<Button>("Menu_Demarrage/Ok");
            _label = GetNode<Label>("Menu_Demarrage/explication");
            _button.Connect("pressed", this, nameof(OnPressed));
        }

        public void ShowMenu(BuildingBase buildingBase)
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

        private bool ComputeResult(Main root)
        {
            if (root.GetTicCounter() < 6) return true;
            var rnd = new Random();
            var check = root.GetStatsSys()._statsDictionnaire[BuildingStats.Stats.Score] - GameManager.Score;
            var ok = rnd.Next(1, 100);
            return ok + ok * check / 100 > 50;
        }

        private void OnPressed()
        {
            Hide();
        }
    }
}