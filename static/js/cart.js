
function updateItemTotal() {
    var cartTable = document.getElementsByClassName("cart-content")[0];
    var cartRows = cartTable.getElementsByClassName("cart-rows")
    var total = 0
    for (var i = 0; i < cartRows.length; i++) {
        cartRow = cartRows[i]
        cartPrice = cartRow.getElementsByClassName("c-price")[0]
        cartQuantity = cartRow.getElementsByClassName("cart_quantity_input")[0]
        price = parseFloat(cartPrice.innerText.replace('$', ''))
        quantity = cartQuantity.value
        var res = (price * quantity)
        // console.log(res)
        var textchange = cartRow.getElementsByClassName("cart_total_price")[0]
        textchange.textContent = res
        total += res

    }
    document.getElementsByClassName("cart-t")[0].textContent = "$" + total
    console.log(total)
}