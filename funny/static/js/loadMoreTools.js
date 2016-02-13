/**
 * Created by xiaolu on 16/2/12.
 */
//加载更多
$(window).scroll(function () {
    if ($('#moreinfo').attr('pages') == 5) {
        $('#moreinfo').text('点击加载更多内容');
    }
    if ($('#moreinfo').attr('pages') > 4) {
        return false;
    }
    var scrollTop = $(this).scrollTop();
    var scrollHeight = $(document).height();
    var windowHeight = $(this).height();
    if (scrollTop + windowHeight == scrollHeight) {
        if ($.inArray($('#moreinfo').attr('pages'), arrayPages) < 0) {
            loadMore();
            arrayPages.push($('#moreinfo').attr('pages'));
        }
    }
});
function loadMore() {
    $.getJSON('/api/jokes/' + index, function (data) {
        attrs = data['data'];
        item = ''
        for (i in attrs) {
            item += '<article class="clearfix joke"> '
                + ' <h1> ' + attrs[i]['title'] + ' </h1> '
                + '<p style="font-size: 16px;">'
                + attrs[i]['content']
                + '</p>';
            images = attrs[i]['images'].split(',');
            for (image in images) {
                if(images[image])
                    item += '<img src="'+images[image]+'" width="430px" class="img-responsive">'
            }
            item += '<ul class="operations btn-operations .pull-right">' +
                '<li class="first"> ' +
                '<a class="btn support first like ' + (attrs[i].current_user_like ? 'selected' : '') + '"' +
                'jokeid="' + attrs[i].id + '" >顶<em class="value">' + attrs[i].like_number + '</em></a> ' +
                '</li> ' +
                '<li><a class="reply" style="display:none" href="#">回复</a></li> ' +
                '<li style=""> ' +
                '<a class="share last" href="/article/joke/' + attrs[i].id + '">...</a> </li> ' +
                '</ul>'
                + '</article>'
        }
        if (attrs.length) {
            index = attrs[attrs.length - 1]['id']
        }
        if (!attrs.length) {
            $('#moreinfo').text('没有更多内容了 :>');
            return;
        }
        $('#moreinfo').parent().before(item);
        initLikeOnclick();
        var num = parseInt($('#moreinfo').attr('pages'));
        $('#moreinfo').attr('pages', eval(num + 1));
    });
}
