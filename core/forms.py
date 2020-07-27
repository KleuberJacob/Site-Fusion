from django import forms
from django.core.mail.message import EmailMessage


class Contatoform(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(), max_length=500)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema Fusion',
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br'],
            headers={'Reply to': email}
        )
        mail.send()

