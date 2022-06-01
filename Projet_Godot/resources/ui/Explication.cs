using System.Security.Principal;
using Godot;
using T3.helpers;

namespace T3.resources.ui
{
    /**
     * <summary>Explication gameobject contained by EcranDemarage</summary>
     */
    public class Explication : Label
    {
        /**
         * <summary>Ready</summary>
         */
        public override void _Ready()
        {
            // Get the current user name on the computer
            var name = WindowsIdentity.GetCurrent().Name;
            // Update the label text with provided variables
            Text = Helpers.ReplaceVars(Text, "name", name);
        }
    }
}