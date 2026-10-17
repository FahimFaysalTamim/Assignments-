// #include<stdio.h>
// #include<math.h>
// int main(){
//     int a = 4, b = 5;
    
//     printf("%d",a+b);

//     return 0;
// }

#include<stdio.h>
#include<math.h>
#include<stdbool.h>
int main(){

    int tourdays;
    scanf("%d",&tourdays);
    if (tourdays==2){

        bool BoatAvaliable = false;
        if (BoatAvaliable){
            printf("Going to Tanguarhaur");
        }else{
            printf("Going to srimongol");
        }
    }else if(tourdays=4){

        bool ShipAvaildable = true;

        if(ShipAvaildable){
            printf("Going to Saintmartin");
        }else{
            printf("Going to Cox's Bazer");
        }
    }
}