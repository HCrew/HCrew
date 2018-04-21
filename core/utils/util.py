import difflib
import datetime


class Util:

    @staticmethod
    def calculaMediaFinal(ac, prova):
        'retornar media ponderada entre ac prova'
        'media e dada por 60% e acs 40%'
        'caso algum paramentro seja negativo ou maior que 10'
        if ac < 0 or ac > 10:
            return None
        elif prova < 0 or prova > 10:
            return None
        ac60 = ac*6
        prova40 = prova*4
        return (ac60 + prova40)/10

    @staticmethod
    def gerarNumeroRA(ultimoRa):
        'o ra deve ter 7 digitos, no formato AAXXXXX'
        'AA: representa o ano'
        'xxxxx: proximo 5 digitos deve ser o proximo numero dos ultimos 5 digitos do parametro'
        today = datetime.date.today()
        n = today.strftime('%y')
        ultimo_ra = str(ultimoRa)
        a = ultimo_ra[:2]
        x = ultimo_ra.replace(a, n)
        x = x[:2]
        w = ultimo_ra[2:]
        w = int(w) + 1
        w = str(w)
        if len(w) == 6:
            w = '00000'
            return x + w
        elif len(w) <= 5:
            while len(w) <= 5:
                w = w.zfill(5)
                return x + w

    @staticmethod
    def calculaMedia(listaNotas):
        'retorna media aritimetica'
        total = 0
        i = 0
        for nota in listaNotas:
            total += nota
            i += 1
        return total/i

    @staticmethod
    def descontaNota(nota, porcentagem):
        'retorna nota calculada'
        valorDesconto = nota*porcentagem/100
        return nota - valorDesconto

    @staticmethod
    def verificaCopia(texto1, texto2):
        'verificar se os texto sao parecidos'
        'retornar true se for 80% ou mais parecido'
        'biblioteca difflib'
        seq = difflib.SequenceMatcher(None, texto1, texto2)
        qtd = seq.ratio()*100

        if qtd >= 80:
            return True

        return False
