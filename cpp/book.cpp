// following cpp book

#include <iostream> // printing library
#include "Account.h"

using namespace std;

// beginning of program
int main() {
    Account myAccount;
    myAccount.setName("Christian");

    cout << "Initial account name is: " << myAccount.getName();

    cout << "\nPlease enter the account name: ";
    string theName;
    getline(cin, theName);
    myAccount.setName(theName);

    cout << "Name in object myAccount is: " << myAccount.getName() << endl;
}
