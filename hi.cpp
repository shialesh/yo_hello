#include<iostream>
#include<cmath>
using namespace std;
int main()
{
long t,n,i,arr[1000][3];
long long temp,te;
cin>>t;
for(i=0;i<t;i++)
{
cin>>n;
if(n<3)
{
cout<<-1;
continue;
}
if(n==3)
cout<<210;
if(n>3)
{
temp=pow(10,n-1);
te=int(temp/210);
if(te*210<temp)
cout<<((te+1)*210);
else
cout<<(te*210);


}


}



}
