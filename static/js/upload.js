function bindUploadVideoBtn() {
    $("#upload_btn").on("click",function (event){
        console.log("uploading");
        var formData = new FormData();
        formData.append("video", $("#video_input")[0].files[0]);
        $.ajax({
            url: "/video/upload",
            method: "POST",
            data: {

            },
            success: function (res) {
                const code = res['code'];
                if (code == 200) {
                    alert("视频上传成功！");
                } else {
                    alert(res['message']);
                }
            }
        })
    });

}

//等文档中所有元素加载完成再执行
$(function (){
    bindUploadVideoBtn();
})