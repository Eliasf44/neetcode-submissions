class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        int[] count = new int[26];

        for (char c: s.toCharArray()){
            count[c - 'a']++;
        }

        for (char b: t.toCharArray()){
            count[b - 'a']--;
        }

        for (int a : count) {
            if (a != 0) {
                return false;
            }
        }
        return true;
    }
}
