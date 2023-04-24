$(document).ready(function() {

        $("[id^='add-to-cart']").click(function(){
            var productId = $(this).data("id");
            if ($("#quantity-input-"+productId).css("display") == 'none') {
                $("#quantity-input-"+productId).css("display", "block");
            } else {
               qvalue = $("[id^='input-quantity']").val();
               $.ajax({
                  url: pathurl + "orders/add-to-cart/",
                  type: "POST",
                  data: {
                        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                        productId : productId,
                    },
                  success: function(response) {
                        updateCartQuant(response,qvalue)
                  },
                  error: function(jqXHR, textStatus, errorThrown) {
                    console.log("Error: " + textStatus + " - " + errorThrown);
                  }
                });

            }

        })

function updateCartQuant(response,qvalue){
    if ($("#add-to-cart-icon").css("display") == 'none') {
        $("#add-to-cart-icon").css("display", "block");
        }
        totatlQuant = $('#cart-total-quant').text();
        $('#cart-total-quant').text(totatlQuant)
        product = JSON.parse(response.data)

        totatlQuant = parseInt(totatlQuant) + parseInt(qvalue)
        console.log(typeof totatlQuant)
        $('#cart-total-quant').text(totatlQuant)


}

        $('.minus-btn').click(function () {
            var $input = $(this).parent().find('input');
            var count = parseInt($input.val()) - 1;
            count = count < 1 ? 1 : count;
            $input.val(count);
            $input.change();
            return false;
        });
        $('.plus-btn').click(function () {
            var $input = $(this).parent().find('input');
            $input.val(parseInt($input.val()) + 1);
            $input.change();
            return false;
        });
    });