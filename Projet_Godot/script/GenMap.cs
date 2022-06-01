using System;
using System.Collections.Generic;
using Godot;
using T3.helpers;
using T3.resources.ECS;
using T3.resources.ECS.components;
using T3.resources.ECS.entities;

namespace T3.script
{
    public class GenMap : MultiMesh
    {
        private readonly List<List<int>> _map = new List<List<int>>();
        private readonly Random rnd = new Random();

        public GenMap(TileMap f, TileMap w, TileMap d)
        {
            GenRect();
            GenBuilding(litNewBuild: 10, highPoorBuild: 10, highNewBuild: 3, litPoorBuild: 20, highPoorHosp: 2,
                litNewHosp: 1, moyPoorBuild: 10, litNewOffice: 1, litNewSchool: 3, moyNewBuild: 3, litPoorSchool: 3);

            var buildingScene =
                (Building) GD.Load<PackedScene>("res://resources/ECS/entities/Building.tscn").Instance();
            var hospitalScene =
                (Hospital) GD.Load<PackedScene>("res://resources/ECS/entities/Hospital.tscn").Instance();
            var officeScene = (Office) GD.Load<PackedScene>("res://resources/ECS/entities/Office.tscn").Instance();
            var schoolScene = (School) GD.Load<PackedScene>("res://resources/ECS/entities/School.tscn").Instance();

            const int marge = 10;
            for (var i = -marge; i < _map.Count + marge; i++)
            for (var j = -marge; j < _map[0].Count + marge; j++)
                //si en haut de la map alors mettre herbe
                if (j > _map[0].Count + 15 || i > _map.Count + 15)
                {
                    f.SetCell(i, j, 3);
                }
                //Mettre en bas de l'eau de manière aléatoire
                else if ((i < 0 || j < 0 || j > _map[0].Count || i > _map.Count)
                         && rnd.Next(50) < (i * 1.5 + j * 1.5 - _map[0].Count - _map.Count) * 2)
                {
                    f.SetCell(i, j, 3);
                }
                // Si il n'y a rien mettre de l'herbe
                else if (i < 0 || j < 0 || j >= _map[0].Count || i >= _map.Count)
                {
                    f.SetCell(i, j, 0);
                }
                // Si c'est de la route mettre de la route
                else if (_map[i][j] == 1)
                {
                    f.SetCell(i, j, 2);
                }
                // Si c'est un batiment alors
                else if (_map[i][j] != 0)
                {
                    BuildingBase b;
                    GameManager.CountBat++;
                    //choix du batiment
                    switch ((_map[i][j] - 2) / 6)
                    {
                        case 0:
                            b = (Building) buildingScene.Duplicate();
                            break;
                        case 1:
                            b = (Hospital) hospitalScene.Duplicate();
                            GameManager.CountHos++;
                            break;
                        case 2:
                            b = (Office) officeScene.Duplicate();
                            break;
                        default:
                            b = (School) schoolScene.Duplicate();
                            break;
                    }

                    // Mettre la Position
                    b.Position = w.MapToWorld(new Vector2(i + 1, j + 1));
                    // Mettre la taille
                    if (b.TryGetComponent<BuildingSize>(out var size))
                        size.ChangeSize((BuildingSize.BSize) ((_map[i][j] - 2) % 3));
                    // Mettre la rotation
                    if (!b.TryGetComponent<BuildingRotation>(out var rot)) continue;
                    rot.ChangeRotation(Rotate(i, j));
                    // Mettre l'état
                    if (!b.TryGetComponent<BuildingHealth>(out var state)) continue;
                    state.State = (_map[i][j] - 2) / 3 % 2 == 1
                        ? BuildingHealth.BuildingState.New
                        : BuildingHealth.BuildingState.Old;
                    b.ManageStats();
                    w.AddChild(b);
                }
                //sinon mettre de la décoration
                else
                {
                    switch (_map[i][j])
                    {
                        // Parking
                        case 0 when rnd.Next(3) < 1 && Near(i, j, 1) && (Near(i, j, 10) || Near(i, j, 11)
                            || Near(i, j, 12) || Near(i, j, 13)):
                            f.SetCell(i, j, 1);
                            break;
                        // Autre décoration
                        case 0 when rnd.Next(20) < 1:
                            d.SetCell(i, j, 0, autotileCoord: new Vector2(rnd.Next(3), 0),
                                flipX: rnd.Next(2) == 1);
                            f.SetCell(i, j, 0);
                            break;
                        // Sinon mettre de l'herbe
                        default:
                            f.SetCell(i, j, 0);
                            break;
                    }
                }

            f.UpdateBitmaskRegion(Vector2.Zero, new Vector2(10 + _map.Count, 10 + _map[0].Count));
        }

        private void GenRect()
        {
            var nbRects = rnd.Next(5, 10);
            var rects = new List<Vector2[]>(); //ensemble des position de début et de fin (haut gauche, bas droit)
            var pos = new Vector2(1, 1);
            var maxEndPos = new Vector2(1, 1);
            for (var i = 0; i < nbRects; i++)
            {
                var endPos = new Vector2(pos.x + rnd.Next(5, 10), pos.y + rnd.Next(5, 10));
                rects.Add(new[] {pos, endPos});
                if (maxEndPos.x < endPos.x) maxEndPos.x = endPos.x;
                if (maxEndPos.y < endPos.y) maxEndPos.y = endPos.y;
                pos = rnd.Next(2) == 0
                    ? new Vector2(rnd.Next((int) pos.x, (int) endPos.x), endPos.y)
                    : new Vector2(endPos.x, rnd.Next((int) pos.y, (int) endPos.y));
            }

            for (var i = 0; i < maxEndPos.x + 2; i++)
            {
                _map.Add(new List<int>());
                for (var j = 0; j < maxEndPos.y + 2; j++)
                {
                    var exist = false;
                    for (var k = 0; k < nbRects; k++)
                    {
                        var posX = (int) rects[k][0].x;
                        var posy = (int) rects[k][0].y;
                        var endPosX = (int) rects[k][1].x;
                        var endPosY = (int) rects[k][1].y;
                        exist = i >= posX && i <= endPosX && (j == posy || j == endPosY)
                                || j >= posy && j <= endPosY && (i == posX || i == endPosX);
                        if (exist) break;
                    }

                    _map[i].Add(exist ? 1 : 0);
                }
            }
        }

        private bool Near(int i, int j, int k)
        {
            var n = false;
            if (i > 0) n = _map[i - 1][j] == k;
            if (i < _map.Count - 1 && !n) n = _map[i + 1][j] == k;
            if (j > 0 && !n) n = _map[i][j - 1] == k;
            if (j < _map[0].Count - 1 && !n) n = _map[i][j + 1] == k;
            return n;
        }

        //chaque batiment est numéroté par rapport à sa position dans la liste +2
        public void GenBuilding(int? litPoorBuild = 0, int? moyPoorBuild = 0, int? highPoorBuild = 0,
            int? litNewBuild = 0, int? moyNewBuild = 0, int? highNewBuild = 0,
            int? litPoorHosp = 0, int? moyPoorHosp = 0, int? highPoorHosp = 0,
            int? litNewHosp = 0, int? moyNewHosp = 0, int? highNewHosp = 0,
            int? litPoorOffice = 0, int? moyPoorOffice = 0, int? highPoorOffice = 0,
            int? litNewOffice = 0, int? moyNewOffice = 0, int? highNewOffice = 0,
            int? litPoorSchool = 0, int? moyPoorSchool = 0, int? highPoorSchool = 0,
            int? litNewSchool = 0, int? moyNewSchool = 0, int? highNewSchool = 0)
        {
            int?[] bat =
            {
                litPoorBuild, moyPoorBuild, highPoorBuild, litNewBuild, moyNewBuild, highNewBuild,
                litPoorHosp, moyPoorHosp, highPoorHosp, litNewHosp, moyNewHosp, highNewHosp,
                litPoorOffice, moyPoorOffice, highPoorOffice, litNewOffice, moyNewOffice, highNewOffice,
                litPoorSchool, moyPoorSchool, highPoorSchool, litNewSchool, moyNewSchool, highNewSchool
            };
            var sizeMap = _map.Count * _map[0].Count;
            var vide = true;
            for (var i = 0; i < bat.Length && vide; i++) vide = bat[i] == 0;
            while (!vide)
            {
                for (var i = 0; i < _map.Count; i++)
                for (var j = 0; j < _map[0].Count; j++)
                {
                    if (_map[i][j] != 0 || !Near(i, j, 1)) continue;
                    for (var k = 0; k < bat.Length; k++)
                    {
                        if (rnd.Next(sizeMap) >= bat[k]) continue;
                        _map[i][j] = k + 2;
                        bat[k]--;
                        break;
                    }
                }

                vide = true;
                for (var i = 0; i < bat.Length && vide; i++) vide = bat[i] == 0;
            }
        }

        private BuildingRotation.BRotation Rotate(int i, int j)
        {
            if (i > 0 && _map[i - 1][j] == 1 || (j > 0 && _map[i][j - 1] == 1)) 
                return BuildingRotation.BRotation.South;
            if (i < _map.Count - 1 && _map[i + 1][j] == 1)
                return BuildingRotation.BRotation.West;
            return BuildingRotation.BRotation.North;
        }
    }
}