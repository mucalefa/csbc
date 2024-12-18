# Cyber Security Bootcamp dio.me

## Passo a Passo
Este é o HowTo de uma das atividades do Bootcamp de Segurança Cibernetica realizado pela dio em parceria com o banco

Utilizei um container docker para instalar a ferramenta e executar o teste:
```
docker run -t -i -p 80:80 --rm kalilinux/kali-rolling 
```
> importante não esquecer o ``` -p 80:80 ```, pois ele é o que garante que o container vai responder as solicitações que chegarem

 O container é executado no usuário root diretamente, portanto nao precisa usar ```sudo```. Como as imagens do kali vem apenas o sistema base, sem os chamados metapackages, é preciso instalar:

```
apt update
apt install kali-linux-headless -y  
```
> essa instalacao baixa aproximadamente 1.7GB de dados (7.7GB expandidos)

Ou, se preferir instalar apenas o necessário para o ```setoolkit```:
```
apt update
apt install set -y
```
> essa instalacao baixa aproximadamente 700MB de dados (2.2GB expandidos)


Com todos os pacotes instalados é possível executar o comando ```setoolkit``` e simular o phishing. 

## Resultado
Veja o resultado:

![Simulaçao de Phishing usando setoolkit](https://github.com/user-attachments/assets/42da59b6-bf1b-48fa-afd6-a3d511844b79)
