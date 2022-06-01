using System.Text;
using Godot.Collections;
using T3.helpers;
using T3.resources.ECS.components;

namespace T3.resources.ECS.entities
{
    /**
     * <summary>Building gameobject</summary>
     */
    public class Building : BuildingBase
    {
        /**
         * <summary>Get the name</summary>
         */
        protected override string GetName()
        {
            return "Residence";
        }

        /**
         * <summary>Get the dictionary of there stats</summary>
         */
        public override Dictionary<BuildingStats.Stats, double> ManageStats()
        {
            if (!this.TryGetComponent<BuildingHealth>(out var health)) return null;
            if (health.State.Equals(BuildingHealth.BuildingState.Old))
                return new Dictionary<BuildingStats.Stats, double>
                {
                    {BuildingStats.Stats.SatisfactionJ, -1},
                    {BuildingStats.Stats.SatisfactionA, -3},
                    {BuildingStats.Stats.SatisfactionV, -2},
                    {BuildingStats.Stats.Pollution, -3},
                    {BuildingStats.Stats.Proprete, -2},
                    {BuildingStats.Stats.QualiteDeVie, -2},
                    {BuildingStats.Stats.Sante, -2},
                    {BuildingStats.Stats.Satisfaction, -2},
                    {BuildingStats.Stats.Score, -2.2 /* *BuildingSize.ToInt(GetSize())*/}
                };

            if (health.State.Equals(BuildingHealth.BuildingState.New))
                return new Dictionary<BuildingStats.Stats, double>
                {
                    {BuildingStats.Stats.SatisfactionJ, 1},
                    {BuildingStats.Stats.SatisfactionA, 3},
                    {BuildingStats.Stats.SatisfactionV, 2},
                    {BuildingStats.Stats.Pollution, -1},
                    {BuildingStats.Stats.Proprete, 4},
                    {BuildingStats.Stats.QualiteDeVie, 2},
                    {BuildingStats.Stats.Sante, 2},
                    {BuildingStats.Stats.Satisfaction, 2},
                    {BuildingStats.Stats.Score, 1.8 * BuildingSize.ToInt(GetSize())}
                };

            return new Dictionary<BuildingStats.Stats, double>
            {
                {BuildingStats.Stats.SatisfactionJ, 0},
                {BuildingStats.Stats.SatisfactionA, 0},
                {BuildingStats.Stats.SatisfactionV, 0},
                {BuildingStats.Stats.Pollution, 0},
                {BuildingStats.Stats.Proprete, 0},
                {BuildingStats.Stats.QualiteDeVie, 0},
                {BuildingStats.Stats.Sante, 0},
                {BuildingStats.Stats.Satisfaction, 0},
                {BuildingStats.Stats.Score, 0}
            };
        }

        /**
         * <summary>Get the description</summary>
         */
        protected override string GetDescription()
        {
            var builder = new StringBuilder();
            if (!this.TryGetComponent<BuildingHealth>(out var health)) return null;
            if (!this.TryGetComponent<BuildingHabitable>(out var hab)) return null;
            if (this.TryGetComponent<BuildingStats>(out var comp))
            {
                builder.Append("[color=yellow][b]Etat:[/b][/color] ");
                builder.Append(health.State.ToString());
                builder.Append("\n[color=yellow][b]Habitants:[/b][/color] ");
                builder.Append(hab.ResidentsCount.ToString());
                builder.Append("\n");
            }

            return builder.ToString();
        }
    }
}