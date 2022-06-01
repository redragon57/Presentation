using Godot;

namespace T3.script
{
    public class GameManager : Node
    {
        public static TileMap WorldTileMap;
        public static TileMap DecorMap;
        public static Camera2D Camera;
        public static TileMap TileMap;
        public static int CountBat;
        public static int CountHos;
        public static double Score;
        public static double ScoreInitial;
        public static double Satisfaction;
        public static double SatisfactionInitial;
        public static int pop;

        public static bool PopAcceptation;
        //public const int TotalPop = 0;
    }
}