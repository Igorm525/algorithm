// 1 Написать функцию, преобразующую число в объект. Передавая на вход число в диапазоне [0,
// 999],
// мы должны получить на выходе объект, в котором в соответствующих свойствах описаны
// разряды числа:
// - единицы (в свойстве frsttigit)
// - десятки (в свойстве secondtigit)
// - сотни (в свойстве thirdtigit)
// Например, для числа 45 мы должны получить следующий объект:
// ```
// {
// frsttigit: 5,
// secondtigit: 4,
// thirdtigit: 0,
// }
// ```
// Если число было передано вне [0, 999] диапазона, не целое число или вообще не число,
// необходимо выдать соответствующее сообщение с помощью console.log и вернуть пустой объект.

const digitConvert = num => {
    let digits = [];
    let rest = num;
    let divider = Math.pow(10, String(num).length - 1);
    while (rest) {
        digits.push(parseInt(rest / divider));
        rest %= divider;
        divider /= 10;
    }
    return digits;
};

const stringConvert = num => {
    let str = String(num);
    let digits = [];
    let i = 0;
    while (i < str.length) {
        digits.push(parseInt(str[i++]))
    }
    return digits;
};

console.log(digitConvert(6536));
console.log(stringConvert(6536));
