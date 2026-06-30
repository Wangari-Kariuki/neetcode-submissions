class Solution { 
public:
    bool hasDuplicate(vector<int>& nums) {
        bool duplicate = false;
        for (int num = 0; num < nums.size(); num ++){
            for (int num2 = num + 1; num2 < nums.size(); num2 ++){
                if (nums[num2] == nums[num]){
                    duplicate = true;
                    return duplicate;
                }
            }
        }
        return duplicate;
    }
};