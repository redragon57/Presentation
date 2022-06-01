using System.Text;
using Godot.Collections;
using T3.helpers;
using T3.resources.ECS.components;

namespace T3.resources.ECS.entities
{
    /**
     * <summary>Hospital gameobject</summary>
     */
    public class Hospital : BuildingBase
    {
        /**
         * <summary>Get the name</summary>
         */
        protected override string GetName()
        {
            return "Hopital";
        }

        /**
         * <summary>Get the Dictionary of stats</summary>
         */
        public override Dictionary<BuildingStats.Stats, double> ManageStats()
        {
            if (!this.TryGetComponent<BuildingHealth>(out var health)) return null;
            if (health.State.Equals(BuildingHealth.BuildingState.Old))
                return new Dictionary<BuildingStats.Stats, double>
                {
                    {BuildingStats.Stats.SatisfactionJ, -3},
                    {BuildingStats.Stats.SatisfactionA, -5},
                    {BuildingStats.Stats.SatisfactionV, -7},
                    {BuildingStats.Stats.Pollution, -5},
                    {BuildingStats.Stats.Proprete, -4},
                    {BuildingStats.Stats.QualiteDeVie, -2},
                    {BuildingStats.Stats.Sante, 1},
                    {BuildingStats.Stats.Satisfaction, -5},
                    {BuildingStats.Stats.Score, -3 * BuildingSize.ToInt(GetSize())}
                };

            if (health.State.Equals(BuildingHealth.BuildingState.New))
                return new Dictionary<BuildingStats.Stats, double>
                {
                    {BuildingStats.Stats.SatisfactionJ, 6},
                    {BuildingStats.Stats.SatisfactionA, 8},
                    {BuildingStats.Stats.SatisfactionV, 10},
                    {BuildingStats.Stats.Pollution, -1},
                    {BuildingStats.Stats.Proprete, 6},
                    {BuildingStats.Stats.QualiteDeVie, 6},
                    {BuildingStats.Stats.Sante, 10},
                    {BuildingStats.Stats.Satisfaction, 8},
                    {BuildingStats.Stats.Score, 5.8 * BuildingSize.ToInt(GetSize())}
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

            return builder.ToString();
        }
    }
}