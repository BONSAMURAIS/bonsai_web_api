$( document ).ready(function() {     
function add_row_to_table(btn){
            $("#div_calc_setup").show();
            var row_id = btn.id;
            $("#table_search_results tr").each(function() {
                if ($(this).find('td').eq(1).text() == row_id){
                    var tr = $(this).closest("tr").remove().clone();
                    tr.find('td').eq(2).html("<button class='btn btn-outline-danger my-2 my-sm-0' id='"+tr.find('td').eq(1).text()+"' onclick='remove_row_from_table(this)'>Yes</button>");
                    $("#table_products_calc tbody").append(tr);
                    
                    $.when($.ajax({url: "/rest/products/search_by_uri/"+row_id,dataType: 'json',type: 'GET',success : function(data) {
                        
                        return data
                    }})).then(function(data) {var unit =  data[0]["productionVolumeUnit"]
                     $('#table_calculation_setup > tbody:last-child').append('<tr><td>'+tr.find('td').eq(0).text()+'</td><td><input type="number" id=input_qty_'+row_id+' name="'+row_id+'" required></td><td>'+unit+'</td></tr>');}); 
                };});
         
                    $.when($.ajax({url: "/rest/methods/",dataType: 'json',type: 'GET',success : function(data) {
                        
                        return data
                    }})).then(function(data) {
                        for (var i = 0; i < data.length; i++) {
                           
                            var option = new Option(data[i]["name_method"], data[i]["name_method"]); $('#method_type').append($(option));    
                        };
                    }); 
        };
    
        $('#search_input').keyup(function() {


            var search_val = $(this).val();
            var search_type = $("#search_type_select").val();
            var search_lim = $("#search_lim_select").val()

            $.when($.ajax({
                url: "/rest/products/search_by_"+search_type+"/"+search_val,
                dataType: 'json',
                type: 'GET',
                success : function(data) {
                   var json = data
                    return json
                    },
                error: function(xhr, status, error){console.log(error)}})
            ).then(function(json){
                $("#table_search_results").find("tr:gt(0)").remove();
                        for (var i = 0; i < json.length; i++) {
                            var name = json[i]["name"]
                            var newRowContent = "<tr><td><a id='popoverData' class='btn' href='/product_description/"+json[i]['uri']+" target='_blank' data-content='"+json[i]["introduction"]+"' rel='popover' data-placement='bottom' data-original-title='"+json[i]['name']+"' data-trigger='hover' style='font-size:12px;'>"+String(json[i]["name"])+"</a></td><td>"+json[i]["uri"]+"</td><td><button class='btn btn-outline-success my-2 my-sm-0' id="+json[i]["uri"]+" onclick='add_row_to_table(this)'>Yes</button></td></tr>";
                            $("#table_search_results tbody").append(newRowContent);  
                            };
                        $('#table_search_results a').popover();

            })
        });

        function remove_row_from_table(btn){
            var row_id = btn.id;
            var name_row;
            $("#table_products_calc tr").each(function() {
                if ($(this).find('td').eq(1).text() == row_id){
                    name_row = $(this).find('td').eq(0).text()
                    var tr = $(this).closest("tr").remove();
                };

                });
            $("#table_calculation_setup tr").each(function() {
                if ($(this).find('td').eq(0).text() == name_row){
                    var tr = $(this).closest("tr").remove();
                };

                });
        };

    $('#table_search_results a').popover();
    
    $(document).ready(function() {
        $("form").submit(function(e) {
            e.preventDefault();
            $("#col_results").show()
            graph_1();
            graph_2();
        });
        
    });
};