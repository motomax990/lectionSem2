#include <iostream>

int main()
{
    std::cout << "Введите до кагого числа сортировать" << std::endl;
    int n = 0;
    std::cin >> n;
    bool mass_to_sort[n+1]; 
    for(int i=2; i < n+1; i++){
        mass_to_sort[i] = true;
    }
    std::cout <<  '\n';
    int x=2;
    while (x*x <= n){
        if(mass_to_sort[x] == true){
            for(int i=x*x; i <= n; i+=x){
                mass_to_sort[i] = false;
            }
            x += 1;
        }

    }
    
    for (int i = 2; i < n+1; i++) {
        if (mass_to_sort[i] == true) {
            std::cout << i << ' ';
        }
    }
    std::cout << std::endl;

}
