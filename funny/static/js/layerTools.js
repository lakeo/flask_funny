/**
 * Created by xiaolu on 16/2/13.
 */
$(document).ready(function () {
    //加载扩展模块
    layer.config({
        extend: 'extend/layer.ext.js'
    });

});

function showBigImage(_this) {
    img = ''
    if ((imgs = $(_this).parent().find('img.hide_flag')).length == 0) {
        img = document.createElement('img')
        $(img).attr('src', $(_this).attr('src'))
        $(img).css('display', 'none')
        $(img).addClass('hide_flag')
        $(img).click(function (e) {
            layer.closeAll();
        })
        $(img).insertAfter(_this)

    } else {
        img = imgs[0]
    }
    if (!img) {
        return;
    }
    layer.open({
        type: 1,
        title: false,
        closeBtn: 0,
        area: '430px',
        skin: 'layui-layer-nobg', //没有背景色
        shadeClose: true,
        content: $(img)
    });
}
