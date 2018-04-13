function mostrar(curso) {
    if(curso=="ads") {
        status = document.getElementById('ads').style.display;
        if(status=="none") {
            document.getElementById('ads').style.display = 'block';
        } else {
            document.getElementById('ads').style.display = 'none';
        }
    } else if(curso=="adm") {
        status = document.getElementById('adm').style.display;
        if(status=="none") {
            document.getElementById('adm').style.display = 'block';
        } else {
            document.getElementById('adm').style.display = 'none';
        }
    } else if(curso=="rc") {
        status = document.getElementById('rc').style.display;
        if(status=="none") {
            document.getElementById('rc').style.display = 'block';
        } else {
            document.getElementById('rc').style.display = 'none';
        }
    } else if(curso=="bd") {
        status = document.getElementById('bd').style.display;
        if(status=="none") {
            document.getElementById('bd').style.display = 'block';
        } else {
            document.getElementById('bd').style.display = 'none';
        }
    } else if(curso=="gti") {
        status = document.getElementById('gti').style.display;
        if(status=="none") {
            document.getElementById('gti').style.display = 'block';
        } else {
            document.getElementById('gti').style.display = 'none';
        }
    } else if(curso=="jd") {
        status = document.getElementById('jd').style.display;
        if(status=="none") {
            document.getElementById('jd').style.display = 'block';
        } else {
            document.getElementById('jd').style.display = 'none';
        }
    }
}