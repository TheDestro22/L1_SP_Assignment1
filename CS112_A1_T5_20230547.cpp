/*
# File: CS112_A1_T2_2_20230547
# Program: Game2 (Number Scrabble) Number Scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw.
# Author: Mohamed Ehab Sabry
# Section: NA
# ID: 20230547
# Version: 2.0
# Date: 16/2/2024
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int main(){

//Variables and Arrays
string pl1_name = "";
string pl2_name ="";
vector <int> Num_list = {1,2,3,4,5,6,7,8,9}; //range of choices from 1 to 9
vector <int> pl1_choices = {};
vector <int> pl2_choices = {};
int choice = 0;
int choices_counter = 0;
bool winner = false;
int pl1_sum = 0;
int pl2_sum = 0;

//The main program
cout << "\033[92m\033[1m ** Hello and welcome to the Number scrabble game. A game where you have to think deepely, and choose wisely **\033[0m \n"<<endl;
cout << "Please enter the name of the first contestant: " << endl;
cin >> pl1_name;
cout << "Please enter the name of the second contestant: " << endl; 
cin >> pl2_name; 
//A loop that keeps the game going tell there is a winner or there is a draw
while (choices_counter <= 8){
//Player1:
    cout << pl1_name << ",choose a number from this list: " << "[";
    for (int i = 0 ; i < Num_list.size(); ++i){
        cout << Num_list[i] << " ";        
    }
    cout << "]";
    cout << endl;
    cin >> choice; 

//asking the player to choose again if he picks a number out of range or a character
    auto Num1_exist = find(Num_list.begin(),Num_list.end(),choice);
    while (Num1_exist == Num_list.end()){
        cout << "\033[91mThe number you have entered is not valid ,please choose a number from 1-9: \033[0m" << endl;
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cin >> choice;
        Num1_exist = find(Num_list.begin(),Num_list.end(),choice);

    }
    
//saving the player choice and erasing it from the main list
    pl1_choices.push_back(choice);
    choices_counter += 1;
    Num_list.erase(Num1_exist);

//calculating the sum of each player choices and deciding the winner
    size_t pl1_picked_nums = pl1_choices.size();
    if (pl1_picked_nums == 3)
    {
        pl1_sum = pl1_choices[0] + pl1_choices[1] + pl1_choices[2];

        if (pl1_sum == 15)
        {
            cout << "YOU HAVE WON " << pl1_name << " !!!! Congratulations, better luck next time " << pl2_name <<endl;
            return 0;
        }

    }
    else if (pl1_picked_nums == 4)
    {
        if (pl1_choices[0] + pl1_choices[1] + pl1_choices[3] == 15 || pl1_choices[0] + pl1_choices[2] + pl1_choices[3] == 15 || pl1_choices[1] + pl1_choices[2] + pl1_choices[3] == 15)
        {
            cout << "YOU HAVE WON " << pl1_name << " !!!! Congratulations, better luck next time " << pl2_name <<endl;
            return 0;
        }
    }
    else if (pl1_picked_nums == 5)
    {
        if (pl1_choices[0] + pl1_choices[1] + pl1_choices[4] == 15 || pl1_choices[0] + pl1_choices[2] + pl1_choices[4] == 15 || pl1_choices[0] + pl1_choices[3] + pl1_choices[4] == 15 || pl1_choices[1] + pl1_choices[2] + pl1_choices[4] == 15 || pl1_choices[1] + pl1_choices[3] + pl1_choices[4] == 15 || pl1_choices[2] + pl1_choices[3] + pl1_choices[4] == 15)
        {
            cout << "YOU HAVE WON " << pl1_name << " !!!! Congratulations, better luck next time " << pl2_name <<endl;
            return 0;
        }
    }

//Player2:
    cout << pl2_name << ",choose a number from this list: " << "[";
    for (int i = 0 ; i < Num_list.size(); ++i){
        cout << Num_list[i] << " ";        
    }
    cout << "]";
    cout << endl;
    cin >> choice; 

//asking the player to choose again if he picks a number out of range or a character
    auto Num2_exist = find(Num_list.begin(),Num_list.end(),choice);
    while (Num2_exist == Num_list.end()){
        cout << "\033[91mThe number you have entered is not valid ,please choose a number from 1-9: \033[0m" << endl;
        cin >> choice;
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cin >> choice;
        Num2_exist = find(Num_list.begin(),Num_list.end(),choice);

    }
    
    
//saving the player choice and erasing it from the main list
    pl2_choices.push_back(choice);
    choices_counter += 1;
    Num_list.erase(Num2_exist);

//calculating the sum of each player choices and deciding the winner
    size_t pl2_picked_nums = pl2_choices.size();
    if (pl2_picked_nums == 3)
    {
        pl2_sum = pl2_choices[0] + pl2_choices[1] + pl2_choices[2];

        if (pl2_sum == 15)
        {
            cout << "YOU HAVE WON " << pl2_name << " !!!! Congratulations, better luck next time " << pl1_name <<endl;
            return 0;
        }

    }
    else if (pl2_picked_nums == 4)
    {
        if (pl2_choices[0] + pl2_choices[1] + pl2_choices[3] == 15 || pl2_choices[0] + pl2_choices[2] + pl2_choices[3] == 15 || pl2_choices[1] + pl2_choices[2] + pl2_choices[3] == 15)
        {
            cout << "YOU HAVE WON " << pl2_name << " !!!! Congratulations, better luck next time " << pl1_name <<endl;
            return 0;
        }
    }
    else if (pl2_picked_nums == 5)
    {
        if (pl2_choices[0] + pl2_choices[1] + pl2_choices[4] == 15 || pl2_choices[0] + pl2_choices[2] + pl2_choices[4] == 15 || pl2_choices[0] + pl2_choices[3] + pl2_choices[4] == 15 || pl2_choices[1] + pl2_choices[2] + pl2_choices[4] == 15 || pl2_choices[1] + pl2_choices[3] + pl2_choices[4] == 15 || pl2_choices[2] + pl2_choices[3] + pl2_choices[4] == 15)
        {
            cout << "YOU HAVE WON " << pl1_name << " !!!! Congratulations, better luck next time " << pl2_name <<endl;
            return 0;
        }
    }
  
}
    cout << "It's a draw gentelmen, have some rest and try again later";
    return 0;
}