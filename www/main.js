var filter, filter_cnt;

filter = document.getElementById('filter');
filet_cnt = document.getElementById('filter-cnt');

filter.addEventListener('click', function () {
    if (filet_cnt.style.marginLeft == '0px') {
        filet_cnt.style.marginLeft = '-100vw';
    } else {
        filet_cnt.style.marginLeft = '0px';
    };
});