function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click",function (event){
        var $this = $(this);
       var email = $("input[name ='email']").val();
       if(! email){
           alert("请输入邮箱！");
           return;
       }
       // 通过js发网络请求ajax
        $.ajax({
            url: "/user/captcha",
            method:"POST",
            data:{
                "email":email
            },
            success:function (res){
                var code = res['code'];
                if (code == 200){
                    $this.off("click");
                    //开始倒计时
                    var countDown =60;
                    var timer = setInterval(function () {
                        if(countDown>0) {
                            $this.text(countDown + "秒后重新发送");
                            countDown = countDown - 1
                        }else{
                             $this.text("获取验证码");
                             bindCaptchaBtnClick();
                             clearInterval(timer);
                        }
                    },1000);
                    alert("验证码发送成功");
                }else{
                    alert(res['message']);
                }
            }
        })
    });
}
//等文档中所有元素加载完成再执行
$(function (){
    bindCaptchaBtnClick();
})
