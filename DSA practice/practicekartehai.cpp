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

// [7,1,5,3,6,4]
#include <iostream>
#include <vector>
using namespace std;

int max_profit_in_stock( vector <int> &price){
    int max_profit=0 , best_buy= price[0];
    for(int i = 1 ; i <price.size(); i++){
        if(price[i]>best_buy){
            max_profit=max(max_profit,price[i]-best_buy);
        }
        
        best_buy=min(best_buy,price[i]);
    }
    
return max_profit;
 }
 int main(){
 vector <int> price={7,1,5,3,6,4};
 int profit=max_profit_in_stock(price);
 cout << profit ;
 }

