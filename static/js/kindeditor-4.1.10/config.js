KindEditor.ready(function(K) {
           K.create('#textarea[name=content]',{  <!--定义需要插入富文本编辑器的路径-->
            width:800,      <!-- 定义富文本编辑器的长宽-->
            height:200,
            uploadJson: '/admin/upload/kindeditor',
           });
});