// mejority elemet by more algo 

// #include <iostream>
// #include <vector>
// using namespace std;

// int mjorityelement(vector<int>& nums){
//     int frq = 0;
//     int ans = 0;

//     for (int i = 0; i < nums.size(); i++){
//         if (frq == 0){
//             ans = nums[i];
//         }

//         if (ans == nums[i]){
//             frq++;
//         } else {
//             frq--;
//         }
//     }

//     return ans;
// }

// int main(){
//     vector<int> nums = {1,2,2,1,1};

//     int ans = mjorityelement(nums);

//     cout << ans;

//     return 0;
// }

// pair sum by brute force aproach 
// #include <iostream>
// #include <vector>
// using namespace std ;
//  vector <int> pair_sum(vector<int>&nums2,int target){
//     vector <int> ans ; 
//     int n = nums2.size();
//     for (int i = 0 ; i<n ; i++){
//         for (int j = i+1; j<n ; j ++){
//             if(nums2[i]+nums2[j]==target){
//                 ans.push_back(i);
//                 ans.push_back(j);
//                    return ans;   
//             }
                 
           
//         }
//     }
//     return ans;
    
// }

// int main (){
//     vector <int> nums2={1,2,34,3};
//     int target= 4 ;
//     vector <int> ans = pair_sum(nums2,target);
//     cout <<ans[0] << " ," << ans[1] << "\n";
//     return 0 ;


// }

// pair sum by using two pointer aproach 
// #include <iostream>
// #include <vector>
// using namespace std;
// vector<int>pair_sum(vector <int> &nums2,int target){
//     vector <int>ans;
//     int n = nums2.size();
//     int i = 0 ;
//     int j = n-1;
//     while(i <j ){
//         int pairsum(nums2[i]+nums2[j]);
  
    
//         if(pairsum==target){
//             ans.push_back(i);
//             ans.push_back(j);
//             return ans;
//         }
        
//         else if(pairsum>target){
//             j--;
//         }
//         else if(pairsum<target){
//             i++;
//         }
        
            
//         }
//         return ans;
//     }

// int main(){
//     vector <int> nums2={2,7,11,13};
//     int target= 18;
//     vector <int>ans=pair_sum(nums2,target);
//     cout <<ans[0] << " ," << ans[1] << "\n";
//     return 0 ;

// }

// majority element by sorting 
// #include <iostream>
// #include <vector>
// using namespace std;

// int majority_element(vector<int> &nums3) {
//     int n = nums3.size();

//     for (int val : nums3) {
//         int frq = 0;

//         for (int ele : nums3) {  
//             if (ele == val) {
//                 frq++;
//             }
//         }

//         if (frq > n / 2) {
//             return val;   
//         }
//     }

//     return -1;  
// }

// int main() {
//     vector<int> nums3 = {2, 2, 1, 2, 3, 2, 2};

//     cout << "Majority Element: " << majority_element(nums3);

//     return 0;
// }

// using sorting algo #

#include <iostream>
#include <vector>
#include <algorithm>   
using namespace std;

int majority_element3(vector<int>& nums6) {
    int n = nums6.size();

    sort(nums6.begin(), nums6.end());

    int frq = 1;
    int ans = nums6[0];

    for (int i = 1; i < n; i++) {
        if (nums6[i] == nums6[i - 1]) {
            frq++;
        } else {
            frq = 1;
            ans = nums6[i];   // ✅ fixed
        }

        if (frq > n / 2) {
            return ans;
        }
    }

    return -1;   // ✅ better
}
int main(){
    vector <int> nums6={2,2,2,4,5};
    int result = majority_element3(nums6);
    cout << result << " \n";
}

