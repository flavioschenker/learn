#include <iostream>
#include <vector>
using namespace std;

// Pass by reference &, original array myVector is modified
void modifyVector(vector<int>& nums) {
    nums.push_back(100);
}

int main() {
    vector<int> myVector = {1, 2, 3};
    modifyVector(myVector);
    
    for (int num : myVector) {
        cout << num << " ";  // Output: 1 2 3 100
    }
    return 0;
}
