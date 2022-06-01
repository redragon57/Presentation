using Godot.Collections;

namespace T3.resources.ECS.components
{
    /**
     * <summary>BuildingStats component</summary>
     */
    public class BuildingStats : BaseComponent
    {
        /**
         * <summary>Stats</summary>
         */
        public enum Stats
        {
            SatisfactionJ,
            SatisfactionA,
            SatisfactionV,
            Pollution,
            Proprete,
            QualiteDeVie,
            Sante,
            Satisfaction,
            Score
        }

        /**
         * <summary>Base parent</summary>
         */
        private BuildingBase _parent;

        /**
         * <summary>Dictionary of all Stats</summary>
         */
        public Dictionary<Stats, double> StatsDictionnaire = new Dictionary<Stats, double>
        {
            {Stats.SatisfactionJ, 0},
            {Stats.SatisfactionA, 0},
            {Stats.SatisfactionV, 0},
            {Stats.Pollution, 0},
            {Stats.Proprete, 0},
            {Stats.QualiteDeVie, 0},
            {Stats.Sante, 0},
            {Stats.Satisfaction, 0},
            {Stats.Score, 0}
        };
        
        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            if (GetParent<BuildingBase>() != null) _parent = GetParent<BuildingBase>();
        }
        
        /**
         * <summary>Init</summary>
         */
        public override void Init()
        {
            var stats = _parent.ManageStats();
            if (stats == null)
            {
            }
            else
            {
                foreach (var s in stats)
                    if (s.Value != null)
                        StatsDictionnaire[s.Key] = s.Value;
            }
        }

        /**
         * <summary>Update</summary>
         */
        public override void Update()
        {
            var stats = _parent.ManageStats();
            if (stats == null) return;

            foreach (var s in stats.Keys)
                if (stats.TryGetValue(s, out var value))
                    StatsDictionnaire[s] = value;
        }
    }
}