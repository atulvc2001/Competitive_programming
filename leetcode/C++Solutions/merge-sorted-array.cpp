//class Solution {
//public:
    //void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        //int i = m - 1;
        //int j = n - 1;
        //int k = m + n - 1;
//
        //while(j >= 0){
            //if (i >= 0 && nums1[i] > nums2[j])
                //nums1[k--] = nums1[i--];
            //else
                //nums1[k--] = nums2[j--];
        //};
    //};
//};

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        int last = m + n - 1;

        while(m>0 && n>0){
            if(nums1[m-1] > nums2[n-1]){
                nums1[last] = nums1[m-1];
                m--;
            }
            else{
                nums1[last] = nums2[n-1];
                n--;
            }
            last--;
        }

        while(n>0){
            nums1[last] = nums2[n-1];
            n--;
            last--;
        }

    }
};
