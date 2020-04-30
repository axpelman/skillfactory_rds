#  Игра угадай число
----
### Задача:
Угадать загаданное компьютером число за минимальное число попыток. 

* * * * * * * * *
### Условие
Компьютер загадывает целое число от 1  до 100 , и его нужно угадать за минимальное число попыток . Под «угадать», конечно, подразумевается «написать программу, которая угадывает число».
* * * * * * * * *
### Решение
Решение задачи основано на использовании алгоритма двочного (бинарного) поиска.
[**Двоичный (бинарный) поиск**](https://ru.wikipedia.org/wiki/Двоичный_поиск) (также известен как метод деления пополам или дихотомия) — классический алгоритм поиска элемента в отсортированном массиве (векторе), использующий дробление массива на половины:
1. Определение значения элемента в середине структуры данных. Полученное значение сравнивается с ключом.
2. Если ключ меньше значения середины, то поиск осуществляется в первой половине элементов, иначе — во второй.
3. Поиск сводится к тому, что вновь определяется значение серединного элемента в выбранной половине и сравнивается с ключом.
4. Процесс продолжается до тех пор, пока не будет найден элемент со значением ключа или не станет пустым интервал для поиска.

![double search](common/algorithm_double_search.png "двоичный бинарный поиск" )

* * * * * * * * 


----
----

# Game guess the number
----
### Task:
Guess the guessed computer number in the minimum number of attempts. 

* * * * * * * * *
### Condition
The computer makes an integer from 1 to 100, and it must be guessed for a minimum number of attempts . By “guessing”, of course, is meant “writing a program that guesses a number.
* * * * * * * * *
### Decision
The solution to the problem is based on the use of the binary search algorithm.
[**Binary search**](https://en.wikipedia.org/wiki/Binary_search_algorithm) also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array.
Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. If the target value matches the element, its position in the array is returned. If the target value is less than the element, the search continues in the lower half of the array. If the target value is greater than the element, the search continues in the upper half of the array. By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration.

![binary search](common/Binary_search_algorithm.jpg "binary search" )

* * * * * * * * 