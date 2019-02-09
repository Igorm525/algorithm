// 1. Добавьте стили для верхнего меню, товара, списка товаров и кнопки вызова корзины.
// 2. Добавьте значения по умолчанию для аргументов функции. Как можно упростить или сократить запись функций?
// 3. *Сейчас после каждого товара на странице выводится запятая. Из-за чего это происходит? Как это исправить?

const products = [
    {title: 'Notebook', price: 2000, img: 'http://pluspng.com/img-png/free-png-laptop-laptop-free-png-image-2046.png'},
    {title: 'Mouse', price: 20, img: 'http://pluspng.com/img-png/mouse-hd-png-avid-media-composer-or-many-othernle-s-the-bella-corporation-has-a-mouse-that-will-improve-your-editing-workflow-the-hd-mouse-is-an-incredibly-504.png'},
    {title: 'Keyboard', price: 35, img: 'http://pluspng.com/img-png/keyboard-hd-png-keyboard-png-hd-png-image-419.png'},
];

const renderProduct = (item) => `
<div class="col-lg-4 col-md-6 mb-4">
    <div class="card h-100">
        <a class="img-wrap" href="#"><img class="card-img-top" src="${item.img}" alt="${item.title}"></a>
        <div class="card-body">
            <h5 class="card-title">
                <a class="text-info" href="#">${item.title}</a>
            </h5>
            <h5>${item.price}</h5>
        </div>
    </div>
</div>
`;

const renderPage = (list = products) => {
    document.querySelector('.products').innerHTML = list.map(item => renderProduct(item)).join('');
};

renderPage();

