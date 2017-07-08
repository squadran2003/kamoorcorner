$(document).ready(function(){
 $(".order-form").hide();
 $(".form-errors").hide();

 $("input").click(function(e){

     $(this).parent().parent().css("border-bottom","none");
     $(this).parent().parent().next().css("margin","0px");

     // fade in the add to cart form
     $(this).parent().parent().next().css("margin-bottom","10px");
     $(this).parent().parent().next().next().fadeIn();     // get the closest form


     // hide the errors div
     //$(this).parent().parent().next().hide();
     //$("#order-form-errors").addClass('alert alert-warning');
     //$("#order-form-errors").show();



 });

 

 $("input[type='submit']").click(function(evt){
     $form = $(this).closest('form');
     $quantity = $('input[type="number"]',$form).val();
     console.log($quantity);
     $form.submit(function(e){
         if(parseInt($quantity)< 1){
             $(this).parent().prev().addClass("alert alert-danger");
             $(this).parent().prev().text('Order  cannot be less than 1 Kilo!');
             $(this).parent().prev().show();
             e.preventDefault();

         }

     });

 });




});
