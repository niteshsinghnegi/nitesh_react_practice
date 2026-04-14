#include <stdio.h>

int main()
{
   int a[50],n,i,key ,c=0;
   printf ("enter the no of element ");
   scanf ("%d",&n);
   printf ("enter the element/n");
   for(i=0;i<n;i++)
   scanf("%d",&a[i]);
   printf ("enter the key element");
   scanf("%d",&key);
   for (i=0;i<n;i++)
   {
       if(a[i]==key)
       {
           c++;
           break;
           
       }
   }
   if(c==1)
   printf("search is successful");
  
   else;
   printf("search is unsucessful");
   return 0;
   
}