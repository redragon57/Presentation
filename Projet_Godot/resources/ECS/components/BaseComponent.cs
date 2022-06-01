using Godot;

namespace T3.resources.ECS.components
{
    /**
     * <summary>The base component will be extends to create components for buildings</summary>
     */
    public abstract class BaseComponent : Node
    {
        /**
         * <summary>Called when building is ready to initialize the component</summary>
         */
        public abstract void Init();

        /**
         * <summary>Called each tick iteration to change component state</summary>
         */
        public abstract void Update();
    }
}