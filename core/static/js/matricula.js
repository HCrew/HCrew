var table = document.querySelector('#alunos table'),
    rows = [],
    template = ('<tr>\
    <td>${id}</td>\
    <td>Aluno ${id}</td>\
    <td>\
        <input type="radio" class="approve" id="approve-${id}" name="status-${id}" value="aprovado" required>\
        <label for="approve-${id}">Aprovado</label>\
        <br>\
        <input type="radio" class="cancel" id="cancel-${id}" name="status-${id}" value="cancelado" required>\
        <label for="cancel-${id}">Cancelado</label>\
        <br>\
    </td>\
</tr>');

for (let i = 10001, pattern = /\$\{id\}/g; i <= 10080; i++) {
    rows.push(template.replace(pattern, i));
}
table.innerHTML += rows.join('\n');

document.forms['alunos'].onsubmit = function(e) {
    e.preventDefault();
    var approved = Array.from(document.querySelectorAll('input.approve')).filter(i => i.checked).length;

    if (20 <= approved && approved <= 60) {
        this.submit();
    }
    else {
        alert('Número de alunos aprovados precisa ser\num número entre 20 e 60 (é ' + approved + ')');
    }
};
