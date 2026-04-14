#include <stdio.h>
int main (){
    int a[50],n,key,c=0,i;
    printf("enter the number of elemnents");
    scanf("%d",&n);
    printf("enter the elements");
    for (i=0;i<n;i++)
    scanf("%d",&a[i]);
    printf("enter the key elemnets ");
    for (i=0;i<n;i++)
    scanf("%d",&key);
{
    if(a[i]==0)
    {
        c++;
        break
    }}
    if(c==1)
    printf("the search is successfull ");
    else 
    printf("the search is unseccufull");
    return 0;
}
