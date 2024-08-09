class Solution {
public:
    int romanToInt(string s) {
        map<char, int>mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;

        int output = 0;
        int n = s.size();

        for (int i = 0; i<n; i++){
            if (i < n-1 && mp[s[i]]<mp[s[i+1]]){
                output -= mp[s[i]];
            }
            else (output += mp[s[i]]);

        }return output;
        
    }
};