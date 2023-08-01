#importando o Tkinter
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

#importando calendário
from tkcalendar import Calendar, DateEntry

#importando View
from view import *

#tabela de cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

#criando janela
janela = Tk()
janela.title("")
janela.geometry('1034x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

#dividindo janela
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#criando labels titulo
app_nome = Label(frame_cima,text='Formulário de Consulta', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

#inserindo dados  no banco
def inserir():
    nome = inp_nome.get()
    email = inp_email.get()
    phone = inp_phone.get()
    dia = inp_data.get()
    status = inp_status.get()
    infor = inp_sobre.get()

    lista = [nome, email, phone, dia, status, infor]

    if nome == '':
        messagebox.showerror('Erro', 'Campo nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')
        inp_nome.delete(0, 'end')
        inp_email.delete(0, 'end')
        inp_phone.delete(0, 'end')
        inp_data.delete(0, 'end')
        inp_status.delete(0, 'end')
        inp_sobre.delete(0, 'end')
    
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

#atualizar dados
global tree
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        inp_nome.insert(0, tree_lista[1])
        inp_email.insert(0, tree_lista[2])
        inp_phone.insert(0, tree_lista[3])
        inp_data.insert(0, tree_lista[4])
        inp_status.insert(0, tree_lista[5])
        inp_sobre.insert(0, tree_lista[6])

        #inserindo dados  no banco
        def update():
            nome = inp_nome.get()
            email = inp_email.get()
            phone = inp_phone.get()
            dia = inp_data.get()
            status = inp_status.get()
            infor = inp_sobre.get()

            lista = [nome, email, phone, dia, status, infor, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'Campo nome não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso!')
                inp_nome.delete(0, 'end')
                inp_email.delete(0, 'end')
                inp_phone.delete(0, 'end')
                inp_data.delete(0, 'end')
                inp_status.delete(0, 'end')
                inp_sobre.delete(0, 'end')
            
            for widget in frame_direita.winfo_children():
                widget.destroy()
            mostrar()

        btn_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        btn_confirmar.place(x=105, y=360)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha de informação')

#deletar daddos
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Dados deletados com sucesso!')

        for widget in frame_direita.winfo_children():
            widget.destroy()
        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha de informação')

#criando labels e inputs
#Nome
lb_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lb_nome.place(x=10, y=10)
inp_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
inp_nome.place(x=10, y=40)

#email
lb_email = Label(frame_baixo,text='E-mail *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lb_email.place(x=10, y=70)
inp_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
inp_email.place(x=10, y=100)

#telefone
lb_phone = Label(frame_baixo,text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lb_phone.place(x=10, y=130)
inp_phone = Entry(frame_baixo, width=45, justify='left', relief='solid')
inp_phone.place(x=10, y=160)

#dataconsulta
lb_data = Label(frame_baixo,text='Data*', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lb_data.place(x=10, y=190)
inp_data = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
inp_data.place(x=10, y=220)

#status
lb_status = Label(frame_baixo,text='Status Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lb_status.place(x=160, y=190)
inp_status = Entry(frame_baixo, width=20, justify='left', relief='solid')
inp_status.place(x=160, y=220)

#informações
lb_sobre = Label(frame_baixo,text='Informações *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lb_sobre.place(x=10, y=250)
inp_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid')
inp_sobre.place(x=10, y=280)

#criando botões
btn_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
btn_inserir.place(x=10, y=320)

btn_upgrade = Button(frame_baixo,command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
btn_upgrade.place(x=105, y=320)

btn_delete = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
btn_delete.place(x=200, y=320)

#configurando a tabela para mostrar os resultados
def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

#chamando função mostrar
mostrar()
janela.mainloop()