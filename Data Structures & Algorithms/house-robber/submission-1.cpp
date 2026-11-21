class Solution
{
public:
    int rob(vector<int> &nums)
    {
       for(int i=2;i<nums.size();i++){
        nums[i]=nums[i]+maxnum(nums,i-1) ;
       } 
       return maxnum(nums,nums.size());
    }
    int maxnum(vector<int> &n,int size){
        int max1=n[0];
        for(int i=0;i<size;i++){
            max1=max(max1,n[i]);
        }
        return max1;
    }
};