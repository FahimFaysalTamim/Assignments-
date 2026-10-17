#include<stdio.h>
int main(){

    int n;
    int a[100000];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int num;
        scanf("%d",&num);
        a[num]++;
    }
    int count=0;
    for(int i=0;i<n;i++){
        if(a[i]==1){
            count+=1;
        }
    }
    printf("%d",count);

}