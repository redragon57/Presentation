using Godot;
using Godot.Collections;
using T3.helpers;
using T3.resources.ECS.components;
using T3.resources.ECS.entities;
using T3.script;

namespace T3.resources.ECS
{
    public class StatisticsSystem : Reference
    {
        private readonly Dictionary<Vector2, BuildingStats> _buildingsStatsList =
            new Dictionary<Vector2, BuildingStats>();

        public Dictionary<BuildingStats.Stats, double> _statsDictionnaire = new Dictionary<BuildingStats.Stats, double>
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

        /**
         * <summary>nombre batiment (nouveau puis vieux) pour respectivement (residence, hopitaux, ecole et bureau) puis nombre de parc, de jeune, d'adulte et de personne agée</summary>
         */
        public void Setup(Array buildings, TileMap tileMap)
        {
            foreach (var building in buildings)
            {
                if (!(building is Node2D b)) continue;
                var location = tileMap.WorldToMap(b.GlobalPosition);
                if (building.GetType() == typeof(Building))
                    if (b.TryGetComponentInChildren<BuildingSize>(out var size))
                        if (b.TryGetComponentInChildren<BuildingHabitable>(out var hab))
                            switch (size.Size)
                            {
                                case BuildingSize.BSize.L1:
                                    GameManager.pop += 40;
                                    hab.ChangeResidentsCount(40);
                                    break;
                                case BuildingSize.BSize.L2:
                                    hab.ChangeResidentsCount(85);
                                    GameManager.pop += 85;
                                    break;
                                default:
                                    hab.ChangeResidentsCount(135);
                                    GameManager.pop += 135;
                                    break;
                            }

                if (b.TryGetComponentInChildren<BuildingStats>(out var stats))
                    _buildingsStatsList.Add(location, stats);
            }
        }

        /**
         * <summary>Update statistiques</summary>
         */
        public void Update()
        {
            double score = 0;
            var nbHos = GameManager.CountHos;
            //var _nbBat = GameManager.CountBat;

            foreach (var kv in _buildingsStatsList)
            {
                kv.Value.Update();
                /*if (kv.GetType() == typeof(Hospital))
                    _statsDictionnaire[BuildingStats.Stats.Score] += kv.Value.StatsDictionnaire[BuildingStats.Stats.Score] / (nbHos/2);
                else
                _statsDictionnaire[BuildingStats.Stats.Score] += kv.Value.StatsDictionnaire[BuildingStats.Stats.Score];*/

                foreach (var s in _statsDictionnaire.Keys)
                    if (_statsDictionnaire.ContainsKey(s) && kv.Value.StatsDictionnaire.ContainsKey(s))
                        _statsDictionnaire[s] += kv.Value.StatsDictionnaire[s];
            }

            //Impact de la pollution sur la satisfaction jeunes
            /*if (_statsDictionnaire[BuildingStats.Stats.Pollution] > 2)
            {
                _statsDictionnaire[BuildingStats.Stats.SatisfactionJ] -=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionJ] *
                    _statsDictionnaire[BuildingStats.Stats.Pollution] / 10;
                
                //Impact de la pollution sur la satisfaction Adultes
                _statsDictionnaire[BuildingStats.Stats.SatisfactionA] -=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionA] *
                    _statsDictionnaire[BuildingStats.Stats.Pollution] / 100;
            }
            else
            {
                _statsDictionnaire[BuildingStats.Stats.SatisfactionJ] +=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionJ] *
                    -1 * _statsDictionnaire[BuildingStats.Stats.Pollution] / 10;
                
                //Impact de la pollution sur la satisfaction Adultes
                _statsDictionnaire[BuildingStats.Stats.SatisfactionA] +=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionA] *
                    -1 * _statsDictionnaire[BuildingStats.Stats.Pollution] / 100;
            }



            if (_statsDictionnaire[BuildingStats.Stats.Sante]<0)
            {
                //Impact de la santé sur la satisfaction Vieux
                _statsDictionnaire[BuildingStats.Stats.SatisfactionV] +=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionV] *
                    -1 * _statsDictionnaire[BuildingStats.Stats.Sante] / 10;

                //Impact de la santé sur la satisfaction Adultes
                _statsDictionnaire[BuildingStats.Stats.SatisfactionA] +=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionA] *
                    -1 * _statsDictionnaire[BuildingStats.Stats.Sante] / 100;
            }
            else
            {
                //Impact de la santé sur la satisfaction Vieux
                _statsDictionnaire[BuildingStats.Stats.SatisfactionV] -=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionV] *
                    _statsDictionnaire[BuildingStats.Stats.Sante] / 10;

                //Impact de la santé sur la satisfaction Adultes
                _statsDictionnaire[BuildingStats.Stats.SatisfactionA] -=
                    _statsDictionnaire[BuildingStats.Stats.SatisfactionA] *
                    _statsDictionnaire[BuildingStats.Stats.Sante] / 100;
            }

            _statsDictionnaire[BuildingStats.Stats.Satisfaction] =
                (_statsDictionnaire[BuildingStats.Stats.SatisfactionJ] +
                 _statsDictionnaire[BuildingStats.Stats.SatisfactionA] +
                 _statsDictionnaire[BuildingStats.Stats.SatisfactionV]) / 3;*/

            GameManager.Score = _statsDictionnaire[BuildingStats.Stats.Score];
            GameManager.Satisfaction = _statsDictionnaire[BuildingStats.Stats.Satisfaction];
        }
    }
}