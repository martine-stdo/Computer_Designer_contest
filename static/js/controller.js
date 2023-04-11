function gettime(){
    $.ajax({
        url:"/data/time",
        timeout:10000,
        success:function(data){
            $("#tim").html(data)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_c1_data(){
    $.ajax({
        url:"/data/c1",
        success:function(data){
            $(".num h1").eq(0).text(data.新增确诊);
            $(".num h1").eq(1).text(data.治愈人数);
            $(".num h1").eq(2).text(data.死亡人数);
            $(".num h1").eq(3).text(data.现存人数);
            },
            error:function(xhr,type,errorThrown){

            }
        });
}
function get_c2_data(){
    $.ajax({
        url:"/data/c2",
        success:function(data){
                ec_center_option.series[0].data=data.data
                ec_center.setOption(ec_center_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_l1_data(){
    $.ajax({
        url:"/data/l1",
        success:function(data){
                ec_left1_option.series[0].data=data.data
                ec_left1.setOption(ec_left1_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_r1_data(){
    $.ajax({
        url:"/data/r1",
        success:function(data){
                ec_right1_option.xAxis.data=data.area
                ec_right1_option.series[0].data=data.core
                ec_right1_option.series[1].data=data.dead
                ec_right1.setOption(ec_right1_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_r2_data(){
    $.ajax({
        url:"/data/r2",
        success:function(data){
                ec_right2_option.xAxis.data=data.date
                ec_right2_option.series[0].data=data.noInfect
                ec_right2_option.series[1].data=data.localConfirm
                ec_right2_option.series[2].data=data.dead
                ec_right2_option.series[3].data=data.heal
                ec_right2.setOption(ec_right2_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_l2_data(){
    $.ajax({
        url:"/data/l2",
        success:function(data){
                ec_left2_option.xAxis.data=data.date
                ec_left2_option.series[0].data=data.Infect
                ec_left2_option.series[1].data=data.heal
                ec_left2_option.series[2].data=data.dead
                ec_left2_option.series[3].data=data.localConfirmadd
                ec_left2.setOption(ec_left2_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_f5r_data(){
    $.ajax({
        url:"/data/f5r",
        success:function(data){
                f5_right_option.yAxis.data=data.area
                f5_right_option.series[0].data=data.newadd
                f5_right_option.series[1].data=data.exist
                f5_right.setOption(f5_right_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_f5l_data(){
    $.ajax({
        url:"/data/f5l",
        success:function(data){
                f5_left_option.series[0].data=data.data
                f5_left.setOption(f5_left_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_f21_data(){
    $.ajax({
        url:"/data/f21",
        success:function(data){
                f2_1_option.xAxis[0].data=data.name
                f2_1_option.series[0].data=data.value
                f2_1.setOption(f2_1_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_f22_data(){
    $.ajax({
        url:"/data/f22",
        success:function(data){
                f2_2_option.xAxis[0].data=data.name
                f2_2_option.series[0].data=data.value
                f2_2.setOption(f2_2_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}

function get_f23_data(){
    $.ajax({
        url:"/data/f23",
        success:function(data){
                f2_3_option.xAxis[0].data=data.name
                f2_3_option.series[0].data=data.value
                f2_3.setOption(f2_3_option)
            },
            error:function(xhr,type,errorThrown){

            }
        });
}


setInterval(gettime,1000)
setInterval(get_c1_data,1000)
setInterval(get_c2_data,1000)
setInterval(get_l1_data,1000)
setInterval(get_l2_data,1000)
setInterval(get_r1_data,1000)
setInterval(get_r2_data,1000)
setInterval(get_f5r_data,1000)
setInterval(get_f5l_data,1000)
setInterval(get_f21_data,1000)
setInterval(get_f22_data,1000)
setInterval(get_f23_data,1000)



