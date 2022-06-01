namespace T3.helpers
{
    public static class Helpers
    {
        /**
         * <summary>Transform a text and replace all occurence of a variable name with provided value</summary>
         * <param name="text">The text to change</param>
         * <param name="varName">The variable name to replace</param>
         * <param name="value">The new value</param>
         * <returns>The transformed text</returns>
         */
        public static string ReplaceVars(string text, string varName, string value)
        {
            return text.Replace("${" + varName + "}", value);
        }
    }
}