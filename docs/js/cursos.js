function mostrarOuEsconderCurso() {
    var course = this.nextElementSibling;

    if (!['ads', 'adm', 'rc', 'bd', 'gti', 'jd'].includes(course.id)) return;

    course.style.display = course.style.display === '' ? 'block' : '';
}

document.querySelectorAll('.nossosCursos li > button').forEach(function(bt) {
    bt.onclick = mostrarOuEsconderCurso;
});
