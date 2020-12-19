eel.expose(prnt)
eel.expose(showports)

var result, cnt, scan_bt, prm, body, sscan;

cnt = document.getElementById('cnt');
scan_bt = document.getElementById('scan_bt');
prm = document.getElementById('addr');
body = document.getElementById('bd');

function prnt(obj) {
    result = obj;
    cnt.innerHTML = ''
    for (let x = 0; x < result.length; x++) {
        var dvc, icon, img, info, services, more;
        dvc = document.createElement('div');
        icon = document.createElement('div');
        img = document.createElement('img');
        info = document.createElement('div');
        services = document.createElement('div');

        img.setAttribute('src', 'icons/pc-01.svg');
        icon.appendChild(img);

        dvc.appendChild(icon);

        dvc.className = 'device';
        icon.className = 'icon';
        info.className = 'info';
        services.className = 'services';

        info.innerHTML = `<label><b> Ipv4 Address:</b> ${result[x]['ip']}</label><label><b>MAC:</b> ${result[x]['mac']}</label>`;

        dvc.appendChild(info);
        dvc.appendChild(services)

        if (result[x]['ports'].length > 0) {
            for (let z = 0; z < result[x]['ports'].length; z++) {
                services.innerHTML += `<label class="tag">${result[x]['ports'][z]}</label>`
            }
        } else {
            var lb = document.createElement('label');
            lb.className = "tag sscan";
            lb.innerText = 'Start Socket Scan';
            services.appendChild(lb)
        }

        dvc.innerHTML += '<div class="more"><img src="icons/more-05.svg" alt=""></div>'
        cnt.appendChild(dvc)

        var sscan = document.getElementsByClassName('sscan')

    }
    for (let x = 0; x < sscan.length; x++) {
        var ip = sscan[x].parentElement.parentElement.childNodes[1].firstElementChild["innerText"].split(' ')[2];
        console.log(ip)
        sscan[x].setAttribute('id', `tag${x}`)
        sscan[x].addEventListener('click', function () {
            var ipid = sscan[x].parentElement.parentElement.childNodes[1].firstElementChild["innerText"].split(' ')[2]
            eel.startscan(ipid, `tag${x}`)
        })
    }
}

function scan(addr) {
    var rx = RegExp('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d+(\/\d)?').test(addr);
    var check = true;
    var arr;
    var vl = addr.split('.')
    vl = addr.split('/')
    if (vl.length > 0) {
        arr = vl[0]
    } else {
        arr = vl
    }
    if (arr.length > 7) {
        var nm = arr.split('.')
        console.log(nm)
        for (let x = 0; x < nm.length; x++) {
            if (parseInt(nm[x]) > 255) {
                check = false
                break;
            }
        }
        if (check) {
            console.log('All alrigth now scanning')
            eel.scan(addr)
        } else {
            alert('Something is wrong with the given address')
        }
    }
}

scan_bt.addEventListener('click', function () {
    var prm = document.getElementById('addr').value
    scan(prm)
})


prm.addEventListener('keyup', function (key) {
    if (key['key'] == 'Enter') {
        var prm = document.getElementById('addr').value;
        scan(prm)
    }
})

function showports(ports, lbid) {
    var cnt = document.getElementById(lbid).parentElement;
    cnt.innerHTML = ''
    for (let x = 0; x < ports.length; x++) {
        cnt.innerHTML += `<label class="tag">${ports[x]}</label>`
    }
}