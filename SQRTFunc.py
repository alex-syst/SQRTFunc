Python 3.14.10 (main, Oct 26 2026, 14:10:46) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #include <iostream>
... #include <string>
... // Объявление и реализация функции расчета квадратного корня
... double calSqrt(double target)
... {
...     double x = 1;
...     double oldx;
...     do {
...         oldx = x;
...         x = (x + target / x) / 2;
...     } while (oldx != x);
...     return x;
... }
... int main()
... {
...     double target = 2021;
...     double result = calSqrt(target);
...     std::cout << "x = " << result << "\n";
...     std::cout << "x^2 = " << result * result << "\n";
...     return 0;
... }
