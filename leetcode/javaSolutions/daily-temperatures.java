class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] ans = new int[temperatures.length];
        Stack<Integer> monostack = new Stack<>();

        for (int i = temperatures.length - 1; i >= 0; i--) {
            while (!monostack.isEmpty() && temperatures[monostack.peek()] <= temperatures[i]) {
                monostack.pop();
            }

            if (!monostack.isEmpty()) {
                ans[i] = monostack.peek() - i;
            }

            monostack.push(i);
        }

        return ans;
    }
}
