// #include <iostream>
// #include <vector>
// using namespace std;

// vector <int> pairsum(vector <int> &nums, int target ){
//     vector<int> ans;
//     int n = nums.size();
//     for(int i = 0 ; i <n ; i ++){
//         for (int j = i+1 ; j <n ; j++){
//             if(nums[i]+nums[j]==target){
//                 ans.push_back(i);
//                 ans.push_back(j);
//                 return ans;
//             }
        
//     }
//        return ans;
// }
// }

// int main (){
//     vector <int> nums={2,7,11,15};
//     int target = 9 ;
//     vector <int>ans=pairsum(nums,target);
//     cout << ans[0] <<" ," << ans[1] << "\n";
//     return 0 ;

// }

// #include <iostream>
// #include <vector>
// using namespace std;

// vector <int> pair_sum(vector <int> &nums2,int target){
//     vector <int> ans;
//     int n = nums2.size();
//     int i = 0 ;
//     int j = n-1;

//     while(i<j){
//         int pairsum1=nums2[i]+nums2[j];
//         if(pairsum1 >target){
//             j --;
//         }
//         else if(pairsum1<target){
//             i++;
//         }
//         else {
        
//             ans.push_back(i);
//             ans.push_back(j);
//             return ans;
//         }
        
//     }
//     return ans;
    
// }

// int main (){
//     vector <int> nums2 ={2,7,11,13};
//     int target= 9;
//     vector <int>ans= pair_sum(nums2,target);
//     cout << ans[0] << " ," << ans[1] << "\n";
//     return 0 ;

// }

// #include <iostream>
// #include <vector>
// using namespace std;
// vector <int> pairsum(vector <int> &nums4 ,int target ){
//     vector <int > ans ;
//     int n = nums4.size();
//     for (int i = 0 ; i <n ; i ++){
//         for (int j = i+1  ; j< n ; j++){
//             if (nums4[i]+nums4[j]==target){
//                 ans.push_back(i );
//                 ans.push_back(j);
//                 return ans;
//             }
//         }
//     }
//     return ans;
// }

// int main (){
//     vector <int> nums4 = {2,7,11,13};
//     int target = 9 ;
//     vector <int> ans= pairsum(nums4,target);
//     cout << ans[0] << " , " << ans [1] << " \n";
//     return 0 ;
// }

// using two pointer aproch 
// #include <iostream>
// #include <vector>
// using namespace std ;
// vector <int> pair_sum(vector <int> &nums5 , int target){
//     vector <int > ans;
//     int n = nums5.size();
//     int i = 0 ;
//     int j = n-1;

//     while(i <j){
//         int pairsum3=nums5[i]+nums5[j];
//             if(pairsum3<target){
//                 i++;
//             }
//             else if (pairsum3>target){
//                 j--;

//             }
//             else{
//                 ans.push_back(i);
//                 ans.push_back(j);
//                 return ans;
//             }
        
//     }
//     return ans ; 
// }
// #include <iostream>
// #include <vector>
// using namespace std;
// int majority_element1(vector <int>&nums5){
//     int n = nums5.size();
//     for(int val : nums5){
//         int frq=0;
//         for(int ele : nums5){
//             if(val==ele){
//                 frq++;
//             }
//         }
//         if(frq>n/2){
//             return val;
//         }
//     }
//     return -1;
// }

// int main (){
//     vector <int> nums5={7,7,7,13};
//     int result=majority_element1(nums5);
//     cout << result << "\n";
// }

// #include <iostream>
// #include <vector>
// using namespace std ;
// vector <int> pair_sum_in_vector(vector<int> &nums12,int target){
//     vector <int> ans;
//     int n = nums12.size();
//     for (int i = 0 ; i < n ; i++){
//         for(int j = i ; j<n ; j++){
//             if (nums12[i]+nums12[j]== target){
//                 ans.push_back(i);
//                 ans.push_back(j);
//                 return ans;
//             }
//         }
//     }
//     return ans;
// }

// int main(){
//     vector <int> nums12={4,5,12,24};
//     int target = 17;
//     vector <int>ans=pair_sum_in_vector(nums12,target);
//     cout << ans[0] << " , " << ans[1] << "\n";
//     return 0 ;
// }

// #include <iostream>
// using namespace std;
// int my_pow(double x , int n ){
//     long binform =n;
//     double ans=1;
//     if(n==0)return 1.0;
//     if(x==0) return 0.0;
//     if(x==1)return 1.0;
//     if(x==-1 && n %2==1)return 1.0;
//     if(x==-1 && n%2!=1)return -1.0;
    
//     if(binform<0){
//         x=1/x;
//         binform=-binform;

//     }
//     while(binform>0){
//         if(binform %2==1){
//             ans *=x;
//             x *=x;
//         }
//             binform /=2;

//         }
//         return ans;
//     }

//     int main (){
//         double x= 2;
//         int n = 3;
//         int result= my_pow(x,n);
//         cout<< result ;
//     }

// #include <iostream>
// #include <vector>
// using namespace std;
// int max_profit_in_prices(vector <int> price){
//     int max_profit=0 ,  best_buy= price[0];
//     for(int i = 1 ; i < price.size(); i++){
//         if(price[i]>best_buy){
//             max_profit=max(max_profit,price[i]-best_buy);
//         }
//         best_buy=min(best_buy,price[i]);
//     }
//     return max_profit;
    
// }

// int main(){
//     vector <int> price= {7,1,5,3,6,4};
//     int result= max_profit_in_prices(price);
//     cout << result ;
// }


// // binary exponention
// #include <iostream>
// using namespace std;
// int my_pow(double x,int n ){
//     long binform =n;
//     double ans=1;
//     if(n==0)return 1.0;
//     if(x==0)return 0.0;
//     if(x==1)return 1.0;
//     if(x==-1 && n%2==0)return 1.0;
//     if(x==-1 && n%2!=0)return -1.0;

// if(binform<0){
//     x=1/x;
//     binform = -binform;
// }
// while(binform>0){
//     if(binform %2==1){
//         ans*=x;}
//         x*=x;
//         binform /=2;
   
   
//     }
//      return ans;
    

// }

// int main (){
//    double x=2;
//    int n = 5;
//    int result=(my_pow(x,n));
//    cout<< result ;
// }

// #include <iostream>
// #include <vector>
// using namespace std;
// int max_profit_sales(vector <int> price){
//     int maxprofit=0;
//     int bestbuy=1;
//     for (int i = 1 ; i<price.size(); i++){
//         if(price[i]>bestbuy){
//             maxprofit=max(maxprofit,price[i]-bestbuy);
//         }
//         bestbuy=min(bestbuy,price[i]);
//     }
//     return maxprofit;
// }

// int main (){
//     vector <int> price={7,1,5,3,6,4};
//     int result = max_profit_sales(price);
//     cout << result ;
// }

// pair sum 

