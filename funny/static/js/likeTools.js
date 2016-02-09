/**
 * Created by xiaolu on 16/2/10.
 */
function likeSuccuss(obj, type) {
    $(obj).addClass('selected')
    $(obj).children('em.value').each(function () {
        value = $(this).text()
        $(this).text(parseInt(value) + 1)
    })
    obj.onclick = ''
}
function initLikeOnclick() {
    $('a.like').each(function () {
        if($(this).hasClass('selected'))
            return;
        this.onclick = function () {
            var jokeid = $(this).attr('jokeid')
            _this = this
            $.getJSON('/api/like/article/' + jokeid, function (info) {
                if (info.error) {
                    console.log(info['error'])
                    return
                }
                if (info.success)
                    likeSuccuss(_this, info.info);
            });
        }
    });
}
$(document).ready(function () {
    initLikeOnclick();
});
