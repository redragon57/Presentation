using System;
using Godot;
using T3.resources.ECS.components;

namespace T3.helpers
{
    public static class NodeHelper
    {
        /**
         * <summary>Try to get a component</summary>
         * <param name="no">The node</param>
         * <param name="component">The component to out</param>
         * <returns>The presence of the component</returns>
         */
        public static bool TryGetComponentInChildren<T>(this Node no, out T component) where T : BaseComponent
        {
            component = no.GetComponentInChildren<T>();
            return component != null;
        }
        
        /**
         * <summary>Try to get a component</summary>
         * <param name="no">The node</param>
         * <param name="component">The component to out</param>
         * <returns>The presence of the component</returns>
         */
        public static bool TryGetComponent<T>(this Node no, out T component) where T : BaseComponent
        {
            component = no.GetComponent<T>();
            return component != null;
        }

        /**
         * <summary>Try to get a component in the children</summary>
         * <param name="no">The node</param>
         * <param name="component">The component to out</param>
         * <returns>The presence of the component</returns>
         */
        public static bool TryGetComponentInChildren<T>(this BaseComponent no, out T component)
            where T : BaseComponent
        {
            return TryGetComponentInChildren(no.GetParent(), out component);
        }

        /**
         * <summary>Get a component</summary>
         * <param name="no">The node</param>
         * <returns>The presence of the component</returns>
         */
        public static T RequireComponent<T>(this Node no) where T : BaseComponent
        {
            var component = no.GetComponent<T>();
            if (component == null) throw new ArgumentNullException();
            return component;
        }

        /**
         * <summary>Get a component in the children</summary>
         * <param name="no">The node</param>
         * <returns>The presence of the component</returns>
         */
        public static T RequireComponentInChildren<T>(this Node no) where T : BaseComponent
        {
            var component = no.GetComponentInChildren<T>();
            if (component == null) throw new ArgumentNullException();
            return component;
        }
        
        /**
         * <summary>Get a component</summary>
         * <param name="c">The BaseComponent</param>
         * <returns>The presence of the component</returns>
         */
        public static T RequireComponent<T>(this BaseComponent c) where T : BaseComponent
        {
            return RequireComponent<T>(c.GetParent());
        }
        
        /**
         * <summary>Get a component in the children</summary>
         * <param name="co">The BaseComponent</param>
         * <param name="includeInactive">The include inactive</param>
         * <returns>The presence of the component</returns>
         */
        public static T RequireComponentInChildren<T>(this BaseComponent co, bool includeInactive = false)
            where T : BaseComponent
        {
            return RequireComponentInChildren<T>(co.GetParent());
        }

        /**
         * <summary>Get a component</summary>
         * <param name="no">The Node</param>
         * <returns>The presence of the component</returns>
         */
        public static T GetComponent<T>(this Node no) where T : BaseComponent
        {
            T comp = null;
            foreach (var child in no.GetChildren())
            {
                if (!(child is T component)) continue;
                comp = component;
                break;
            }

            return comp;
        }
        
        /**
         * <summary>Get a component in the children</summary>
         * <param name="no">The node</param>
         * <returns>The presence of the component</returns>
         */
        public static T GetComponentInChildren<T>(this Node no) where T : BaseComponent
        {
            T comp = null;
            foreach (Node child in no.GetChildren())
            {
                if (child is T component)
                {
                    comp = component;
                    break;
                }

                comp = child.GetComponentInChildren<T>();
                if (comp != null)
                    break;
            }

            return comp;
        }
    }
}