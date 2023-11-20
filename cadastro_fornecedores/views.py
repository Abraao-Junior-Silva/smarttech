from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FormCadastroFornecedor
from .models import Fornecedor

def cadastroFornecedor(request, sucesso=None, erro=None):
    form = FormCadastroFornecedor()
    return render(request, "pages/cadastroFornecedor.html", {"form": form, "sucesso": sucesso, "erro": erro})

def form_cadastro_fornecedor(request):
    form = FormCadastroFornecedor(request.POST)
    if form.is_valid():
        form.save()
        mensagem_sucesso = "Fornecedor cadastrado com sucesso!"
        return redirect(reverse("cadastroFornecedor") + f"?sucesso={mensagem_sucesso}")
    else:
        print(form.errors)
        mensagem_erro = "Falha ao cadastrar fornecedor!"
        return redirect(reverse("cadastroFornecedor") + f"?erro={mensagem_erro}")

def listarFornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "pages/listarFornecedores.html", {"fornecedores": fornecedores})