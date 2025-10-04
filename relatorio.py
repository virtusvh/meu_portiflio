kv = '''
ScreenManager:
    
    MDScreen:
        name:'tela_1'
        MDFloatLayout:
            MDLabel:
                text: ''
            MDRectangleFlatButton:
                pos_hint: {'center_x': 0.3,'center_y': 0.5}
                text: 'Relatorio Águia'
                on_release: app.root.current = 'tela_2'
        
            MDRectangleFlatButton:
                pos_hint: {'center_x': 0.6,'center_y': 0.5}
                text: 'PRELEÇÃO'
                on_release: app.root.current = 'tela_3'
    
    MDScreen:
        name: 'tela_2'
        MDScrollView:
            keyboard_dismiss_mode: 'on_drag'
            do_scroll_y: True
            MDBoxLayout:
                id: relatoriofinal
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 0.5
        
                MDTopAppBar:
                    title: 'Relatorio Águia'
                    left_action_items: [['arrow-left', lambda x: app.voltar_tela()]]
                    md_bg_color: app.theme_cls.bg_dark
        
                MDLabel:
                    text: 'informe o supervisor e o rondante'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_supervisor
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'supervisor?: '
                MDTextField:
                    id: input_rondante
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'rondante?: '
                #datação
                MDLabel:
                    text: 'informe a data'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_dia
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'qual o dia do mês? '
                MDTextField:
                    id: input_mes
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'qual o mês? '
                MDTextField:
                    id: input_ano
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'qual o ano? '
                #turno
                MDLabel:
                    text: 'informe o turno'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_turno
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'qual o turno? '
                #guarnição
                MDLabel:
                    text: 'informe os componentes da GU (SE FOR UM NOME COMPOSTO USE "-"(HIFEN) PARA SEPARAR'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_gu
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'quais os componentes'
                #abordagens
                MDLabel:
                    text: 'abordagens, apreenções e outras atividades administrtivas'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_onibus
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'onibus abordados'
                MDTextField:
                    id: input_van
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'vans abordadas'
                MDTextField:
                    id: input_caminhao
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'Caminhoões abordados'
                MDTextField:
                    id: input_carro
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'Carro de passeio'
                MDTextField:
                    id: input_moto
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'motos abordadas'
                MDTextField:
                    id: input_bicicleta
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'bicicletas abordadas'
                MDTextField:
                    id: input_residencia
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'residências abordadas'
                MDTextField:
                    id: input_bankLoja
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'quantas loja/Estab. bancários abordados'
                MDTextField:
                    id: input_bar
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'quantos bares ou Similares'
                MDTextField:
                    id: input_pessoas
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'quantas pessoas abordadas?'
                MDTextField:
                    id: input_barco
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text:'embarcações abordadas'
                MDTextField:
                    id: input_armas_f
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'armas de fogo apreendidas '
                MDTextField:
                    id: input_armas_b
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'armas brancas apreendidas'
                MDTextField:
                    id: input_motos_r
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'motos recuperadas'
                MDTextField:
                    id: input_carros_r
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text:'carros recuperados'
                MDTextField:
                    id: input_seccional
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'veiculos entregues na seccional'
                MDTextField:
                    id: input_CTTUC
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'entregues na CTTUC'
                MDTextField:
                    id: input_DETRAN
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'entregues no DETRAN'
                MDTextField:
                    id: input_drogas
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'Apreensões de drogas'
                MDTextField:
                    id: input_furto_roubo_recuperados
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'produtos de furto/roubo recuperados'
                MDTextField:
                    id: input_apresentacoes
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'apresentações na DEPOL'
                MDTextField:
                    id: input_apoio
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text:'operações de apoio a outros orgãos'
                MDTextField:
                    id: input_intervencao
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'intervenção policial c / ou sem morte'
                MDTextField:
                    id: input_BAPMs
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'quantidade de BAPMs'
        
                MDLabel:
                    text: 'numeros de BAPM'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_BAPM
                    size_hint_y: None
                    height: self.minimum_height
                    multiline: True
                    font_size: dp(16)
                    hint_text: 'quais os números? '
        
                MDLabel:
                    text: 'informações complementares'
                    size_hint_y: None
                    height: 30
                MDTextField:
                    id: input_complemento
                    size_hint_y: None
                    height: dp(45)
                    font_size: dp(16)
                    hint_text: 'quer adicionar algum relato? '
        
                MDLabel:
                    id: resultado
                    text: ''
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    
                MDRectangleFlatButton:
                    text: 'gerar relatório'
                    size_hint_y: None
                    height: '35dp'
                    pos_hint:{'center_x': 0.5}
                    line_color: 1, 1, 1, 1
                    on_release: app.relatorio_final()
        
                MDRectangleFlatButton:
                    text: 'copiar texto'
                    on_release: app.clipboard1()
                    size_hint_y: None
                    height: 40
                    pos_hint:{'center_x': 0.5}
                    line_color: 1, 1, 1, 1
    MDScreen:
        name: 'tela_3'
        ScrollView:
            do_scroll_y: True
    
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 0.5
                
                MDTopAppBar:
                    title: 'Preleção Águia'
                    left_action_items: [['arrow-left', lambda x: app.voltar_tela3()]]
                    md_bg_color: app.theme_cls.bg_dark
                    
                MDTextField:
                    id: imput_tela3_turno
                    hint_text: 'QUAL O TURNO? '
                    
                MDTextField:
                    id: imput_tela3_moto
                    hint_text: 'QUAIS AS MOTOCICLETAS? '
                    
                MDTextField:
                    id: imput_tela3_comp
                    hint_text: 'QUAIS OS COMPONENTES? (use virgula para separar cada componente)'
                    
                
                MDBoxLayout:
                    id: prelasbox
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: 10
                    spacing: 0.5
                        
                MDRectangleFlatButton: 
                    id: plau
                    text: 'próximo'
                    on_release: app.tela_prelecao()
                    
                MDRectangleFlatButton:
                    text: 'copiar'
                    on_release: app.clipboard2()
                    
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: 10
                    spacing: 0.5
                    
                    MDLabel:
                        id: prelecao_label
                        text: ''
                        size_hint_y: None
                    
'''
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.clipboard import Clipboard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp, sp
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.scrollview import MDScrollView


class Relatorio(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.softinput_mode = 'below_target'
        return Builder.load_string(kv)

    def tela_prelecao(self):
        self.plau = self.root.ids.plau

        if self.plau.text == 'próximo':
            self.turno = self.root.ids.imput_tela3_turno
            motos = self.root.ids.imput_tela3_moto.text.split(' ')
            comp = self.root.ids.imput_tela3_comp.text.split(',')
            prelasbox = self.root.ids.prelasbox
            self.dic_km = {}
            self.dic_comb = {}

            for kmc in motos:
                self.km = MDTextField(hint_text = f'qual km da {kmc}?')
                self.comb = MDTextField(hint_text = f'qual o combustive da {kmc}?')

                prelasbox.add_widget(self.comb)
                prelasbox.add_widget(self.km)

                self.dic_km[kmc] = self.km
                self.dic_comb[kmc] = self.comb

            self.gu = dict(zip(motos, comp))
            self.plau.text = 'enviar'

        else:
            corpo_prelecao = f'grupamento águia {self.turno.text}° turno\n'
            for m, c in self.gu.items():
                km =  self.dic_km[m].text
                combustivel = self.dic_comb[m].text
                corpo_prelecao += f'{m}: {c} -  km: {km}, combustivel: {combustivel}\n'

            self.root.ids.prelecao_label.text = corpo_prelecao

    def clipboard1(self):
        clip1 = self.root.ids.resultado.text
        Clipboard.copy(clip1)

    def clipboard2(self):
        clip2 = self.root.ids.prelecao_label.text
        Clipboard.copy(clip2)

    def voltar_tela(self):
        self.root.current = 'tela_1'

    def voltar_tela3(self):
        self.root.current = 'tela_1'

    def relatorio_final(self):
    #comandantes
        tela2 = self.root
        supervisor = tela2.ids.input_supervisor.text.upper()
        rondante = tela2.ids.input_rondante.text.upper()
    #datação
        dia = tela2.ids.input_dia.text
        mes = tela2.ids.input_mes.text
        ano = tela2.ids.input_ano.text
    #turno
        turno = tela2.ids.input_turno.text
    #guarnição
        guarnicao = tela2.ids.input_gu.text.strip().upper()
        inputgu = guarnicao.split()
        componentes = []
        for g in range (0,len(inputgu),2):
            try:
                componentes.append(inputgu[g] + ' ' + inputgu[g+1])
            except IndexError:
                componentes.append(inputgu[g])
    #informações complementares e numero de BAPMs
        complemento = tela2.ids.input_complemento.text.upper()
        ba = tela2.ids.input_BAPM.text

    #questionário: abordagens, apreenções, apoios, conduções e BAPMs
        abordagens = {"onibus":tela2.ids.input_onibus.text,
        "van":tela2.ids.input_van.text,
        "caminhoes":tela2.ids.input_caminhao.text,
        "carro":tela2.ids.input_carro.text,
        "moto":tela2.ids.input_moto.text,
        "bicicleta":tela2.ids.input_bicicleta.text,
        "residencia":tela2.ids.input_residencia.text,
        "bankLoja":tela2.ids.input_bankLoja.text,
        "bar":tela2.ids.input_bar.text,
        "pessoas":tela2.ids.input_pessoas.text,
        "embarcacoes":tela2.ids.input_barco.text,
        "armas_f":tela2.ids.input_armas_f.text,
        "armas_b":tela2.ids.input_armas_b.text,
        "motos_r":tela2.ids.input_motos_r.text,
        "carros_r":tela2.ids.input_carros_r.text,
        "seccional":tela2.ids.input_seccional.text,
        "CTTUC":tela2.ids.input_CTTUC.text,
        "DETRAN":tela2.ids.input_DETRAN.text,
        "drogas":tela2.ids.input_drogas.text,
        "furto_roubo_recuperados":tela2.ids.input_furto_roubo_recuperados.text,
        "apresentacoes":tela2.ids.input_apresentacoes.text,
        "apoio":tela2.ids.input_apoio.text,
        "intervencao":tela2.ids.input_intervencao.text,
        "BAPMs":tela2.ids.input_BAPMs.text}

    #inicio do relatório
        corpo_relatorio = (f'➡ CMT CPR IV: CEL CHAVES\n'
        f'➡ CMT 13º BPM: TEN CEL MACIEL\n'
        f'➡ SUB CMT: MAJ NOLASCO\n'
        f'➡ CMT 1°CIA ORG: CAP M OLIVEIRA\n'
        f'➡ CMT 2°CIA ORG:TEN MARCIO\n'
        f'➡ SUPERVISÃO: {supervisor}\n'
        f'➡ RONDANTE: {rondante}\n\n'
        f'{dia} de {mes} de {ano}\n\n'
        f'*CPR IV - 13° BPM *\n\n'
        f'*GRUPAMENTO ÁGUIA *\n\n')

        for comp in componentes:
            corpo_relatorio += f"🚨{comp.replace('-',' ')}\n"

        corpo_relatorio += '\n' + '-'*20 + '\n\n'
        corpo_relatorio += (f"■ TOTAL DE OCORRÊNCIAS\n"
                           f"> Abordagem\n")
        corpo_relatorio += (f'▪ Ônibus: {abordagens["onibus"]}\n'
        f'▪ VAN: {abordagens["van"]}\n'
        f'▪ Caminhões: {abordagens["caminhoes"]}\n'
        f'▪ Carro de passeio: {abordagens["carro"]}\n'
        f'▪ Moto: {abordagens["moto"]}\n'
        f'▪ Bicicleta: {abordagens["bicicleta"]}\n'
        f'▪ Residência: {abordagens["residencia"]}\n'
        f'▪ Loja/Estab. bancário: {abordagens["bankLoja"]}\n'
        f'▪ Bar ou Similares: {abordagens["bar"]}\n'
        f'▪ Pessoas: {abordagens["pessoas"]}\n'
        f'▪ Embarcação: {abordagens["embarcacoes"]}\n'
        f'▪ armas de fogo apreendidas: {abordagens["armas_f"]}\n'
        f'▪ armas brancas apreendidas: {abordagens["armas_b"]}\n'
        f'▪ motos recuperadas: {abordagens["motos_r"]}\n'
        f'▪ carros recuperados: {abordagens["carros_r"]}\n'
        f'▪ veiculos entregues na seccional: {abordagens["seccional"]}\n'
        f'▪ entregues na CTTUC: {abordagens["CTTUC"]}\n'
        f'▪ entregues no DETRAN: {abordagens["DETRAN"]}\n'
        f'*Apreensões de drogas*\n'
        f'▪ quantidade:{abordagens["drogas"]}\n'
        f'*produto de furto/roubo recuperado*\n'
        f'▪ quantidade:{abordagens["furto_roubo_recuperados"]}\n'
        f'*apresentação na DEPOL*\n'
        f'▪ quantidade:{abordagens["apresentacoes"]}\n'
        f'*operações de apoio a outros orgãos*\n'
        f'▪ quantidade:{abordagens["apoio"]}\n'
        f'*intervenção policial c / ou sem morte*\n'
        f'▪ quantidade:{abordagens["intervencao"]}\n'
        f'▪ BAPM: {abordagens["BAPMs"]}\n\n')
        corpo_relatorio += f'Nº BAPM:\n{ba}\n'

        if complemento == '':
            pass
        else:
            corpo_relatorio += f'◾ {complemento}\n\n'
        if turno == '1':
            corpo_relatorio += f'◾ Que a Gu trabalhou conforme escala de serviço.\nForam feitas rondas ostensivas e preventivas\nnos bairros centrais eperiféricos da cidade.\nE conforme a escala foi feita barreira na portaria da vila de 07:00h as 08:30h\n\n'
        else:
            corpo_relatorio += f'◾ Que a Gu trabalhou conforme escala de serviço.\nForam feitas rondas ostensivas e preventivas\nnos bairros centrais eperiféricos da cidade.\n\n'

        corpo_relatorio += f'🚨PASSAGEM DO SERVICO S / A.🚨'

        tela2.ids.resultado.text = corpo_relatorio

Relatorio().run()