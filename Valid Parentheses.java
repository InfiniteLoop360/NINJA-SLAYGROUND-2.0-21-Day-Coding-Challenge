import java.util.Stack;

public class Solution {
    public static boolean isValidParenthesis(String s) {
        // Create a stack to store opening brackets
        Stack<Character> stack = new Stack<>();

        // Traverse through each character in the string
        for (char ch : s.toCharArray()) {
            // If the character is an opening bracket, push it onto the stack
            if (ch == '{' || ch == '[' || ch == '(') {
                stack.push(ch);
            }
            // If the character is a closing bracket
            else if (ch == '}' || ch == ']' || ch == ')') {
                // Check if the stack is empty or the top of the stack doesn't match the closing bracket
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                // Check if the top of the stack matches the corresponding opening bracket
                if ((ch == '}' && top != '{') || (ch == ']' && top != '[') || (ch == ')' && top != '(')) {
                    return false;
                }
            }
        }

        // If the stack is empty, all the opening brackets were properly matched
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(isValidParenthesis("[()]{}{[()()]()}")); // true
        System.out.println(isValidParenthesis("[[}")); // false
    }
}
