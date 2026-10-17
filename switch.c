#include<stdio.h>
int main(){

    int day ;
    scanf("%d",&day);
    //int hour=10;
    switch (day)
    {
    case 1:
        printf("Saturday\n");
        // switch(hour){          extra protion for nested condition but switch case is fun
        // Nice easy to learn 
        // case 10:
        //     printf("%d hours",hour);
        //     break;
        // default:
        //     printf("Print without hours");
        //     break;
        // }

        break;
    case 2:
        printf("Sunday\n");
        break;
    case 3:
        printf("Mondayu\n");
        break;
    case 4:
        printf("Tuesday\n");
        break;
    case 5:
        printf("Wednesday\n");
        break;    
    case 6:
        printf("Thursday\n");
        break;
    case 7:
        printf("Friday\n");
        break;

    default:
        printf("Worng day");
        break;
    }
}