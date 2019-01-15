// 5 Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
// где arg1, arg2 – значения аргументов, operation – строка с названием операции. В зависимости
// от
// переданного значения операции (использовать switch) выполнить одну из арифметических
// операций
// (использовать функции из задания 4) и вернуть полученное значение.

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+':
            sum(arg1, arg2);
            break;
        case '-':
            sub(arg1, arg2);
            break;
        case '*':
            mul(arg1, arg2);
            break;
        case '/':
            div(arg1, arg2);
            break;
        default:
            alert('Неверная операция');
    }
}
