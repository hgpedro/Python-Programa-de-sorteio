import random
from modulo import bemvindo
from modulo import tchau

bemvindo()

while True:
    menu = input("""
  • MENU •
 • 1- Alimentação
 • 2- Músicas aleatórias 
 • 3- Filmes aleatórios
 • 4- Livros aleatórios
 • 5- Sair
 • Digite a Opção desejada: """)
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:
            while True:
                listacafem = ["Ovos fritos com Bacon","Tapioca com queijo minas","crepioca com queijo minas","omelete","mamão","Abacate",
                "Melancia","Melão","Laranja","Misto quente","pão com Mortatadela","pão na chapa","queijo quente","cereal","fatia de bolo",
                "pão de queijo","torradas com Ricota","Rap10 com presunto e queijo","croissant de queijo","ovos mexidos","panqueca de banana","Waffle",
                "rosquinhas"]
                listacafemV = ["Tapioca com queijo minas","crepioca com queijo minas","omelete","mamão","Abacate","Melancia","Melão","Laranja", 
                "Quente quente","pão na chapa","queijo quente","cereal, fatia de bolo","pão de quijão","torradas com Ricota","croissant de queijo",
                "ovos mexidos","panqueca de banana","Waffle","rosquinhas"]
                listacafemB = ["Café","Café com leite","Suco de frutas","Leite morno","leite com Toddy","Leite com Nescau","Iogurte Natural",
                "Smoothie","Chá"]

                listaalmoço = ["Arroz de forno com cobertura de mussarela","Talharim com abobrinha","Espaguete à bolonhesa","Estrogonofe de carne",
                "Estrogonofe de frango","Lasanha à bolonhesa","Coxa de frango empanada","Couve-flor gratinada","Lasanha de abobrinha",
                "Frango xadrez","Panqueca de frango","Filé de peixe assado","Fricassê de frango","Escondidinho de carne moída","Risoto de frango",
                "Risoto de camarão","Canelone com presunto e queijo","Escondidinho de frango","Carne de panela com mandioca",
                "Parmigiana de carne moída no forno","Frango cremoso com batata","Frango assado na maionese","Filé de peixe frito","Peixe assado",
                "Panqueca","Galinhada da roça","Nhoque de batata ao sugo","Frango com quiabo e polenta","Espaguete com almôndegas à parmegiana",
                "Bolinho de arroz"]
                listaalmoçoV = ["Arroz de forno com cobertura de mussarela","Talharim com abobrinha","Couve-flor gratinada","Lasanha de abobrinha",
                "Panqueca","Empadão de palmito","Carne de jaca","Risoto de brócolis","Bolinho de arroz","Wrap vegetariano","Tutu de feijão vegano",
                "Strogonoff vegetariano","Picadinho vegano","Arroz com lentilhas e cebolas","Risoto de alho-poró","Nhoque de semolina",
                "Escondidinho de legumes","Lasanha de beringela","Yakisoba tailandês","Galinhada sem galinha","Salada de Penne",
                "Carne vegana de couve-flor","Carne de seitan","Falafel vegano","Bolinho de espinafre"]

                sobremesa = ["Gelatina","Mousse de leite Ninho","Sorvete","Palha italiana","Pudim","Cheesecake de limão",
                "Bolo de Chocolate com recheio de morango","Espeto de morango com chocolate","Mousse de Limão","Panna Cotta de morango","Pavlova",
                "Créme Brulée","Mousse de chocolate com morango","Tiramisu","Torta de Nutella","Torta de Morango","Bolo gelado"]

                listajantar = ["Lasanha de frigideira","Steak tartare","Berinjela recheada com frango","Bolinho de arroz e frango","Atum com quinoa",
                "Tartelete de camarão","Costelinha de porco com chutney","Conchiglione recheado","Escalope ao molho madeira","Filé de frango com laranja"
                ,"Risoto à piamontese","Salada com presunto cru"]
                listajantarV = ["Cogumelos recheados","Bruschetta","Tomates confitados","Caponata de legumes","Salada de grão-de-bico",
                "Tomate recheado com cuscuz","Carpaccio de abobrinha","Risoto de pera com gorgonzola","Conchiglione recheado","Salada de pepino agridoce"]

                while True:
                    tipo = input(" • Você é vegetariano?(S/N): ")
                    if tipo == "S" or tipo == "s":
                        vegetariano = 1
                        break
                    elif tipo == "N" or tipo == "n":
                        vegetariano = 0
                        break
                    else:
                        print("• Digite uma opção válida!")

                if vegetariano == 1:
                    while True:
                        cafeVe = input(f" • Digite a quantidade de prato(s) para o café da manhã para sortear (0 a 10): ")
                        if cafeVe.isdigit():
                            cafeVe = int(cafeVe)
                            if cafeVe <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        cafe = input(f" • Digite a quantidade de bebida(s) para o café da manhã para sortear (0 a 10): ")
                        if cafe.isdigit():
                            cafe = int(cafe)
                            if cafe <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        almocV = input(f" • Digite a quantidade de prato(s) para o almoço para sortear (0 a 10): ")
                        if almocV.isdigit():
                            almocV = int(almocV)
                            if almocV <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        sobre = input(f" • Digite a quantidade de sobremesa(s) para sortear (0 a 10): ")
                        if sobre.isdigit():
                            sobre = int(sobre)
                            if sobre <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        jantaV = input(f" • Digite a quantidade de prato(s) para o jantar para sortear (0 a 10): ")
                        if jantaV.isdigit():
                            jantaV = int(jantaV)
                            if jantaV <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    Totalprato = cafeVe + almocV + sobre + jantaV
                    bebidas = cafe
                    cv = c = acv = s = jv = 0

                    while cv < cafeVe:
                        print("   ")
                        print(" • Os pratos para café da manhã foram:")
                        while cv < cafeVe:
                            sortcafev = random.choice(listacafemV)
                            listacafemV.remove(sortcafev)
                            print(f"  > {sortcafev}")
                            cv+= 1

                    while c < cafe:
                        print("   ")
                        print(" • As bebidas para café da manhã foram:")
                        while c < cafe:
                            sortcafe = random.choice(listacafemB)
                            listacafemB.remove(sortcafe)
                            print(f"  > {sortcafe}")
                            c+= 1

                    while acv < almocV:
                        print("   ")
                        print(" • Os pratos para o almoço foram:")
                        while acv < almocV:
                            sortalmoc = random.choice(listaalmoçoV)
                            listaalmoçoV.remove(sortalmoc)
                            print(f"  > {sortalmoc}")
                            acv+= 1

                    while s < sobre:
                        print("   ")
                        print(" • As sobremesas foram:")
                        while s < sobre:
                            sortsobre = random.choice(sobremesa)
                            sobremesa.remove(sortsobre)
                            print(f"  > {sortsobre}")
                            s+= 1

                    while jv < jantaV:
                        print("   ")
                        print(" • Os pratos para o jantar foram:")
                        while jv < jantaV:
                            sortjantaV = random.choice(listajantarV)
                            listajantarV.remove(sortjantaV)
                            print(f"  > {sortjantaV}")
                            jv+= 1

                    print("   ")
                    print(f" • Totalizando {Totalprato} prato(s) e {bebidas} bebidas(s)! ")      
                    break

                else:
                    while True:
                        cafeC = input(f" • Digite a quantidade de prato(s) para o café da manhã para sortear (0 a 10): ")
                        if cafeC.isdigit():
                            cafeC = int(cafeC)
                            if cafeC <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        cafe = input(f" • Digite a quantidade de bebida(s) para o café da manhã para sortear (0 a 10): ")
                        if cafe.isdigit():
                            cafe = int(cafe)
                            if cafe <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        almoc = input(f" • Digite a quantidade de prato(s) para o almoço para sortear (0 a 10): ")
                        if almoc.isdigit():
                            almoc = int(almoc)
                            if almoc <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        sobre = input(f" • Digite a quantidade de sobremesa(s) para sortear (0 a 10): ")
                        if sobre.isdigit():
                            sobre = int(sobre)
                            if sobre <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    while True:
                        jantaC = input(f" • Digite a quantidade de prato(s) para o jantar para sortear (0 a 10): ")
                        if jantaC.isdigit():
                            jantaC = int(jantaC)
                            if jantaC <= 10:
                                break
                            else:
                                continue
                        else:
                            continue

                    Totalprato =  cafeC + almoc + sobre + jantaC
                    bebidas = cafe
                    cc = c = ac = s = jc = 0

                    while cc < cafeC:
                        print("   ")
                        print(" • Os pratos para café da manhã foram:")
                        while cc < cafeC:
                            sortcafem = random.choice(listacafem)
                            listacafem.remove(sortcafem)
                            print(f"  > {sortcafem}")
                            cc+= 1

                    while c < cafe:
                        print("   ")
                        print(" • As bebidas para café da manhã foram:")
                        while c < cafe:
                            sortcafe = random.choice(listacafemB)
                            listacafemB.remove(sortcafe)
                            print(f"  > {sortcafe}")
                            c+= 1

                    while ac < almoc:
                        print("   ")
                        print(" • Os pratos para o almoço foram:")
                        while ac < almoc:
                            sortalmoc = random.choice(listaalmoço)
                            listaalmoço.remove(sortalmoc)
                            print(f"  > {sortalmoc}")
                            ac+= 1

                    while s < sobre:
                        print("   ")
                        print(" • As sobremesas foram:")
                        while s < sobre:
                            sortsobre = random.choice(sobremesa)
                            sobremesa.remove(sortsobre)
                            print(f"  > {sortsobre}")
                            s+= 1

                    while jc < jantaC:
                        print("   ")
                        print(" • Os pratos para o jantar foram:")
                        while jc < jantaC:
                            sortjantac = random.choice(listajantar)
                            listajantar.remove(sortjantac)
                            print(f"  > {sortjantac}")
                            jc+= 1

                    print("   ")
                    print(f" • Totalizando {Totalprato} prato(s) e {bebidas} bebidas(s)! ")
                    break
                break
            
        elif menu == 2:
            while True:
                listForró = ["Xote Capixaba - Trio Forrozão","O Xote das Meninas - Luiz Gonzaga","Nosso Xote - Bicho de Pé","Ai que Saudade D'ocê - Elba Ramalho, Zé Ramalho",
                "Refazenda - Trio Nordestino","Rindo à Toa - Falamansa","Xote dos Milagres - Falamansa", "Vem Morena - Luiz Gonzaga","Xote da Alegria - Falamansa", "Deus me Proteja - Chico César"]
                
                listSambaPagode = ["Meu Lugar - Arlindo Cruz","Além de Tudo/Retalhos de Cetim/Charlie Brown - Grupo Revelação, Benito de Paula","Patricinha do Olho Azul -  Bom Gosto",
                "Insensato Destino - Zeca Pagodinho, Almir Guineto","Lama nas Ruas - Zeca Pagodinho, Almir Guineto","Conselho Almir Guineto","Sou Flamengo,Cacique e Mangueira - Grupo Fundo de Quintal",
                "Sequestraram minha Sogra - Bezerra da Silva", "Alvorada - Cartola","Quando a Gira Girou - Zeca Pagodinho"]

                listEletrônica = ["Push the Feeling 2003 - NightCrawlers","Free - Ultra Naté", "Movin On Radio Edit - Ian Van Dahl","Magnum Original Mix - Cubicolor","Northern Lights - Santin Jackets, David Harks",
                "High in The Sky - Shai T, DJ Zombi","Euphoria Pic Goes Deep Mix - Pic Schmtiz","If I lose Myself - Alesso, OneRepublic", "Save the World - Swedish House Mafia","Drug Dealer Rafael Carvalho Remix - Volac, Rafael Carvalho"]

                listBlues = ["Crossroad Blues – Robert Johnson","Manish Boy – Muddy Waters","Spoonful – Howlin’ Wolf","Baby Please Don’t Go – John Lee Hooker","Keep It To Yourself – Sonny Boy Williamson",
                "Pearline – Son House","Where Did You Sleep Last Night? – Leadbelly","Dust My Broom – Elmore James","Five Long Years – Buddy Guy","Lonesome Valley – Mississipi John Hurt"]

                listRock = ["Time - Pink Floyd","Wish you Were Here -  Pink Floyd","Shine on you Crazy Diamond - Pink Floyd","Stairway to Heaven - Led Zeppelin","Welcome to the Jungle - Guns N Roses",
                "Back in Black -  AC/DC","Walk This Way - Aerosmith","Nothing Else Matters","The Trooper -  Iron Maiden","I Was Made For Lovin' You - Kiss"]

                listBossaNova = ["Chega de Saudade — João Gilberto", "Águas de Março — Tom Jobim e Elis Regina","Pela Luz Dos Olhos Teus — Miúcha e Tom Jobim","Eu Sei Que Eu Vou Te Amar — Tom Jobim e Vinicius de Moraes",
                "Desafinado — João Gilberto","Garota de Ipanema — Tom Jobim e Vinícius de Moraes","Insensatez - Tom Jobim","Samba de Uma Nota Só - Tom Jobim","Samba de Benção - Vinícios de Moraes",
                "Onde Anda Você - Toquinho, Vimicios de Moraes"]
                
                listPop = ["Levitating - Dua Lipa, Dababy","Save Your Tears - The Weeknd","Over Now -  Calvin Harris, The Weeknd","Peaches -  Justin Bieber, Daniel Ceaser, Giveon","Prisoner - Miley Cyrus, Dua Lipa",
                "Telepatía - Kali Uchis","Ily - Surf Mesa, Emilee","Watermelon Sugar - Harry Styles","Leave The Door Open - Bruno Marsn Anderson .Park, Silk Sonic","In Your Eyes - The Weeknd"]

                listFunk = ["Modo turbo – Luísa Sonza, Pabllo Vittar, Anitta","Maçã verde – Mc Hariel","Amor ou litrão – Mila, Menor Nico, Petter Ferraz","O golpe tá aí – Matheusinho, Menor Nico",
                "Deixa de onda – Dennis, Ludmilla, Xamã","Disco Arranhado Funk remix - Malu, DJ lucas beat","Xerecard - Jeff Costa, Mc Danny","Privilégio - MC Luan Da BS, MC Vitin do LJ, MC Markey",
                "Ô Moça - MC Zaquin","Cai devagarinho até embaixo - MC Rennan, DJ Braga Oficial"]

                listSertanejo = ["Facas – Diego e Victor Hugo ft Bruno e Marrone","Foi pa pum – Simone e Simaria","Despedida de casal – Gustavo Mioto","Alô ambev – Zé Neto e Cristiano","Pulei na piscina – Guilherme e Benuto",
                "Último beijo – Bruno e Marrone ft Wesley Safadão","Lance individual – Jorge e Mateus","Batom de cereja – Israel e Rodolffo","Café e amor – Gusttavo Lima","Você não vale – Felipe Araújo ft Japinha Conde"]

                listCountry = ["She’s Got You —  Patsy Cline","I Walk The Line —  Johnny Cash","Man! I Feel Like A Woman — Shania Twain,","If Tomorrow Never Comes —  Garth Brooks","Chattahoochee —  Alan Jackson",
                "Jolene — Dolly Parton","$1000 Wedding —  Willie Nelson","Achy Breaky Heart —  Billy Ray Cyrus","Every Intention — Kevin Costner & Modern West","Indian Outlaw — Tim McGraw"]

                listRapNacional = ["A Bela e a Fera 2 - Xamã, CMK","Saudade - Luiz Lins, Konai, Mazili","Lá Vem Ela - A Banca 021","Morena - 1Kilo","Perdição - L7NNON","Bom Dia - 3030","Te Encontrar - Modéstia Parte",
                "Libra - A banca 021","Um Pedido - Hungria","Preservê - Gaab"]

                listHipHopInternacional = ["Cleaning Out My Closet - Eminem","Still D.R.E - Dr. Dre, Snoop Dog","Lose Yourself - Eminem","Best Friend - 50 Cent","In da Club - 50 Cent","Window Shopper - 50 Cent",
                "Black an Yellow - Wiz Khalifa","You Don't Know - Eminem, 50 Cent, Ca$his, Lloyd Banks","Turn My Swag On - Soulja Boy","Act A Fool - Ludacris"]

                listIndie = ["Sweater Weather — The Neighbourhood","Do I Wanna Know? — Arctic Monkeys","Say You Won’t Let Go — James Arthur","My Kind Of Woman — Mac DeMarco","Pumped Up Kicks — Foster The People",
                "Video Games — Lana Del Rey","Wild Horses — Bishop Briggs","All I Want — Kodaline","Runaway — Aurora","The Night We Met — Lord Huron"]

                listJazz = ["Take Five - Dave Brubeck","So What - Miles Davis","Take The A Train - Duke Ellington","Round Midnight - Thelonious Monk","My Favorite Thing - John Coltrane","Acknowledgement - John Coltrane",
                "All Blues - Miles Davis","Birdland - Weather Report","Sing, Sing, Sing - Benny Goodman","Strange Fruit - Billie Holiday"]

                listClássica = ["Romance d'amour - Anonymous, Norbert Kraft","Recuerdos de la Alhambra - Ana Vidovic", "Asturias - John Williams","La Catedral - John Wiliams","Nocturne Opus 9 No 2 - Chopin",
                "Prelude in E-Minor (op.28 no. 4) - Chopin","Symphony No. 7 - Beethoven"," Cello Suite No. 1 - Bach","Toccata and Fugue - Bach","Requiem - Mozart"]

                listReggae = ["Exodus - Bob Marley & The Wailers","Black Woman - Judy Mowatt","Poor and Needy - Misty in Roots","Marcus Garvey - Burning Spear","Andei só - Natiruts","Jamming -  Bob Marley & The Wailers",
                "Me Namora - Natiruts", " Easier - SOJA","True Love - SOJA","Rest of my Life - SOJA"]

                while True:
                    Forró = input(" • Digite a quantidade de músicas de Forró para sortear (0 a 10): ")
                    if Forró.isdigit():
                        Forró = int(Forró)
                        if Forró <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    SambaPagode = input(" • Digite a quantidade de músicas de Samba/Pagode para sortear (0 a 10): ")
                    if SambaPagode.isdigit():
                        SambaPagode = int(SambaPagode)
                        if SambaPagode <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Eletrônica = input(" • Digite a quantidade de músicass Eletrônicas para sortear (0 a 10): ")
                    if Eletrônica.isdigit():
                        Eletrônica = int(Eletrônica)
                        if Eletrônica <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Blues = input(" • Digite a quantidade de músicas de Blues para sortear (0 a 10): ")
                    if Blues.isdigit():
                        Blues = int(Blues)
                        if Blues <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Rock = input(" • Digite a quantidade de músicas de Rock para sortear (0 a 10): ")
                    if Rock.isdigit():
                        Rock = int(Rock)
                        if Rock <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    BossaNova = input(" • Digite a quantidade de músicas de Bossa Nova para sortear (0 a 10): ")
                    if BossaNova.isdigit():
                        BossaNova = int(BossaNova)
                        if BossaNova <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Pop = input(" • Digite a quantidade de músicas de Pop para sortear (0 a 10): ")
                    if Pop.isdigit():
                        Pop = int(Pop)
                        if Pop <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Funk = input(" • Digite a quantidade de músicas de Funk para sortear (0 a 10): ")
                    if Funk.isdigit():
                        Funk = int(Funk)
                        if Funk <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Sertanejo = input(" • Digite a quantidade de músicas de Sertanejo para sortear (0 a 10): ")
                    if Sertanejo.isdigit():
                        Sertanejo = int(Sertanejo)
                        if Sertanejo <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Country = input(" • Digite a quantidade de músicas Country para sortear (0 a 10): ")
                    if Country.isdigit():
                        Country = int(Country)
                        if Country <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    RapNacional = input(" • Digite a quantidade de músicas de Rap Nacional para sortear (0 a 10): ")
                    if RapNacional.isdigit():
                        RapNacional = int(RapNacional)
                        if RapNacional <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    HipHopInternacional = input(" • Digite a quantidade de músicas de Hip Hop Internacional para sortear (0 a 10): ")
                    if HipHopInternacional.isdigit():
                        HipHopInternacional = int(HipHopInternacional)
                        if HipHopInternacional <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Indie = input(" • Digite a quantidade de músicas Indie para sortear (0 a 10): ")
                    if Indie.isdigit():
                        Indie = int(Indie)
                        if Indie <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Jazz = input(" • Digite a quantidade de músicas de Jazz para sortear (0 a 10): ")
                    if Jazz.isdigit():
                        Jazz = int(Jazz)
                        if Jazz <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Clássica = input(" • Digite a quantidade de músicas Clássicas para sortear (0 a 10): ")
                    if Clássica.isdigit():
                        Clássica = int(Clássica)
                        if Clássica <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Reggae = input(" • Digite a quantidade de músicas de Reggae para sortear (0 a 10): ")
                    if Reggae.isdigit():
                        Reggae = int(Reggae)
                        if Reggae <= 10:
                            break
                        else:
                            continue
                    else:
                        continue
                
                Total = Forró + SambaPagode + Eletrônica + Blues + Rock + BossaNova + Pop + Funk + Sertanejo + Country + RapNacional + HipHopInternacional + Indie + Jazz + Clássica + Reggae
                fo = sp = el = bl = ro = bn = pp = fu = se = co = rn = hh = ie = ja = cl = re = 0

                while fo < Forró:
                    print("   ")
                    print(" • As músicas de Forró foram:")
                    while fo < Forró:
                        sorteioForró = random.choice(listForró)
                        listForró.remove(sorteioForró)
                        print(f"  > {sorteioForró}")
                        fo+= 1

                while sp < SambaPagode:
                    print("   ")
                    print(" • As músicas de Samba/Pagode foram:")
                    while sp < SambaPagode:
                        sorteioSambaPagode = random.choice(listSambaPagode)
                        listSambaPagode.remove(sorteioSambaPagode)
                        print(f"  > {sorteioSambaPagode}")
                        sp+= 1

                while el < Eletrônica:
                    print("   ")
                    print(" • As músicas Eletrônicas foram:")
                    while el < Eletrônica:
                        sorteioEletrônica = random.choice(listEletrônica)
                        listEletrônica.remove(sorteioEletrônica)
                        print(f"  > {sorteioEletrônica}")
                        el+= 1

                while bl < Blues:
                    print("   ")
                    print(" • As músicas de Blues foram:")
                    while bl < Blues:
                        sorteioBlues = random.choice(listBlues)
                        listBlues.remove(sorteioBlues)
                        print(f"  > {sorteioBlues}")
                        bl+= 1

                while ro < Rock:
                    print("   ")
                    print(" • As músicas de Rock foram:")
                    while ro < Rock:
                        sorteioRock = random.choice(listRock)
                        listRock.remove(sorteioRock)
                        print(f"  > {sorteioRock}")
                        ro+= 1

                while bn < BossaNova:
                    print("   ")
                    print(" • As músicas de Bossa Nova foram:")
                    while bn < BossaNova:
                        sorteioBossaNova = random.choice(listBossaNova)
                        listBossaNova.remove(sorteioBossaNova)
                        print(f"  > {sorteioBossaNova}")
                        bn+= 1

                while pp < Pop:
                    print("   ")
                    print(" • As músicas de Pop foram:")
                    while pp < Pop:
                        sorteioPop = random.choice(listPop)
                        listPop.remove(sorteioPop)
                        print(f"  > {sorteioPop}")
                        pp+= 1

                while fu < Funk:
                    print("   ")
                    print(" • As músicas de Funk foram:")
                    while fu < Funk:
                        sorteioFunk = random.choice(listFunk)
                        listFunk.remove(sorteioFunk)
                        print(f"  > {sorteioFunk}")
                        fu+= 1

                while se < Sertanejo:
                    print("   ")
                    print(" • As músicas de Sertanejo foram:")
                    while se < Sertanejo:
                        sorteioSertanejo = random.choice(listSertanejo)
                        listSertanejo.remove(sorteioSertanejo)
                        print(f"  > {sorteioSertanejo}")
                        se+= 1

                while co < Country:
                    print("   ")
                    print(" • As músicas Country foram:")
                    while co < Country:
                        sorteioCountry = random.choice(listCountry)
                        listCountry.remove(sorteioCountry)
                        print(f"  > {sorteioCountry}")
                        co+= 1

                while rn < RapNacional:
                    print("   ")
                    print(" • As músicas de Rap Nacional foram:")
                    while rn < RapNacional:
                        sorteioRapNacional = random.choice(listRapNacional)
                        listRapNacional.remove(sorteioRapNacional)
                        print(f"  > {sorteioRapNacional}")
                        rn+= 1

                while hh < HipHopInternacional:
                    print("   ")
                    print(" • As músicas de Hip Hop Internacional foram:")
                    while hh < HipHopInternacional:
                        sorteioHipHopInternacional = random.choice(listHipHopInternacional)
                        listHipHopInternacional.remove(sorteioHipHopInternacional)
                        print(f"  > {sorteioHipHopInternacional}")
                        hh+= 1

                while ie < Indie:
                    print("   ")
                    print(" • As músicas Indie foram:")
                    while ie < Indie:
                        sorteioIndie = random.choice(listIndie)
                        listIndie.remove(sorteioIndie)
                        print(f"  > {sorteioIndie}")
                        ie+= 1

                while ja < Jazz:
                    print("   ")
                    print(" • As músicas de Jazz foram:")
                    while ja < Jazz:
                        sorteioJazz = random.choice(listJazz)
                        listJazz.remove(sorteioJazz)
                        print(f"  > {sorteioJazz}")
                        ja+= 1

                while cl < Clássica:
                    print("   ")
                    print(" • As músicas Clássicas foram:")
                    while cl < Clássica:
                        sorteioClássica = random.choice(listClássica)
                        listClássica.remove(sorteioClássica)
                        print(f"  > {sorteioClássica}")
                        cl+= 1

                while re < Reggae:
                    print("   ")
                    print(" • As músicas de Reggae foram:")
                    while re < Reggae:
                        sorteioReggae = random.choice(listReggae)
                        listReggae.remove(sorteioReggae)
                        print(f"  > {sorteioReggae}")
                        re+= 1  
                
                print("   ")
                print(f""" • Totalizando {Total} músicas(s)! """)
                break

        elif menu == 3:
            while True:
                listAção = ["Kingsman: Serviço Secreto (2015)","Dunkirk (2017)","A Identidade Bourne (2002)","Os Mercenários (2010)",
                "Atômica (2017)","007 – Operação Skyfall (2012)","Indiana Jones e Os Caçadores da Arca Perdida (1981)","Duro de Matar (1988)",
                "Tropa de Elite (2007)","Kill Bill: Volume 1 (2003)","Missão Impossível – Nação Secreta (2015)","Velozes e Furiosos 7 (2015)",
                "Máquina Mortífera (1987)","Batman: O Cavaleiro das Trevas (2008)","Mad Max: A Estrada da Fúria (2015)"]

                listAventura = ["Star Wars: Episódio V – O Império Contra-Ataca (1980)","Apollo 13: Do Desastre ao Triunfo (1995)",
                "Vingadores: Ultimato (2019)","Interestelar (2014)","Avatar (2009)","Jurassic Park - Parque dos Dinossauros (1993)",
                "Jumanji: Bem-Vindo à Selva (2017)","Capitão América: Guerra Civil (2016)","De Volta para o Futuro (1985)","Jogador Nº 1 (2018)",
                "O Senhor dos Anéis: A Sociedade do Anel (2001)","Mulher-Maravilha (2017)","A Vida Secreta de Walter Mitty (2013)",
                "As Aventuras de Pi (2012)","Dois Irmãos - Uma Jornada Fantástica (2020)"]

                listComédia = ["Borat: Fita de Cinema Seguinte (2020)","Minha Mãe é Uma Peça 3 (2019)","Todo Mundo Quase Morto (2004)",
                "Se Beber, Não Case! (2009)","A Vida de Brian (1978)","Tô Ryca! (2016)","O Auto da Compadecida (2000)","As Branquelas (2004)",
                "Deadpool (2016)","Escola de Rock (2004)","Despedida em Grande Estilo (2017)","Superbad – É Hoje! (2007)",
                "Até que a Sorte nos Separe (2012)","Gênios do Crime (2016)","Este é Meu Garoto (2013)"]

                listdrama = ["Como Eu Era Antes de Você (2016)","Uma Vida com Propósito (2016)","A Culpa é das Estrelas (2014)",
                "Um Momento Pode Mudar Tudo (2014)","O Melhor de Mim (2014)","Doze Anos de Escravidão (2013)","A Última Música (2010)",
                "Sempre ao Seu Lado (2009)","Um Olhar do Paraíso (2009)","Na Natureza Selvagem (2007)","O Pianista (2002)","Uma Lição de Amor (2001)",
                "À Espera de um Milagre (1999)","O Show de Truman (1998)","A Vida é Bela (1997)"]

                listFantasia = ["As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa (2005)","As Crônicas de Nárnia: Príncipe Caspian (2008)"
                ,"As Crônicas de Nárnia: A Viagem do Peregrino da Alvorada (2010)","O Hobbit: Uma Jornada Inesperada (2012)",
                "O Hobbit: A Desolação de Smaug (2013)","O Hobbit: A Batalha dos Cinco Exércitos (2014)","Alice no País das Maravilhas (2010)"
                ,"Príncipe da Pérsia: As Areias do Tempo (2010)","Oz: Mágico e Poderoso (2013)","Zathura: Uma Aventura Espacial (2005)",
                "Thor: O Mundo Sombrio (2013)","The Princess Bride (1987)","O Labirinto do Fauno (2006)","Sete Minutos depois da Meia-Noite (2016)",
                "Harry Potter e a Pedra Filosofal (2001)"]

                listFicção_científica = ["Upgrade (2018)","Tenet (2020)","Ad Astra - Rumo às Estrelas (2019)","Blade Runner 2049 (2017)",
                "A Chegada (2016)","Aniquilação (2018)","Interstellar (2014)","Paprika (2006)","Ex Machina (2014)","Filhos da Esperança (2006)"
                ,"A Origem (2010)","Brilho Eterno de uma Mente sem Lembranças (2004)","Distrito 9 (2009)","Ela (2013)",
                "A.I.: Inteligência Artificial (2001)"]

                listRomance = ["As Vantagens de Ser Invisível (2012)","Hoje Eu Quero Voltar Sozinho (2014)","Diário de Uma Paixão (2004)",
                "A Teoria de Tudo (2014)","Pecados Íntimos (2006)","A Sociedade Literária e a Torta de Casca de Batata (2018)",
                "Como Eu Era Antes de Você (2016)","O Amor Não Tira Férias (2006)","Você Nem Imagina (2020)","Kiss e Cry (2016)",
                "Pense como Eles (2012)","Por Lugares Incríveis (2020)","O Espaço Entre Nós (2017)","Tudo e Todas as Coisas (2017)",
                "Perfeita pra Você (2018)"]

                listTerror = ["O Exorcista (2016)","O chamado (2002)","Invocação do mal (2013)","Horror em Amytville (2005)","Bruxa de Blair (2016)"
                ,"Jogos Mortais (2004)","Sexta-Feira 13 (2009)","It: a coisa (2017)","It: a coisa (2019)","A Freira (2018)",
                "Atividade Paranormal (2007)","Halloween (2018)","Ao cair da noite (2017)","A Órfã (2009)","Olhos Famintos (2001)"]

                while True:
                    Ação = input(" • Digite a quantidade de filmes de ação para sortear (0 a 10): ")
                    if Ação.isdigit():
                        Ação = int(Ação)
                        if Ação <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Aventura = input(" • Digite a quantidade de filmes de aventura para sortear (0 a 10): ")
                    if Aventura.isdigit():
                        Aventura = int(Aventura)
                        if Aventura <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Comédia = input(" • Digite a quantidade de filmes de comédia para sortear (0 a 10): ")
                    if Comédia.isdigit():
                        Comédia = int(Comédia)
                        if Comédia <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Drama = input(" • Digite a quantidade de filmes de drama para sortear (0 a 10): ")
                    if Drama.isdigit():
                        Drama = int(Drama)
                        if Drama <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Fantasia = input(" • Digite a quantidade de filmes de fantasia para sortear (0 a 10): ")
                    if Fantasia.isdigit():
                        Fantasia = int(Fantasia)
                        if Fantasia <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Ficção_científica = input(" • Digite a quantidade de filmes de ficção científica para sortear (0 a 10): ")
                    if Ficção_científica.isdigit():
                        Ficção_científica = int(Ficção_científica)
                        if Ficção_científica <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Romance = input(" • Digite a quantidade de filmes de romance para sortear (0 a 10): ")
                    if Romance.isdigit():
                        Romance = int(Romance)
                        if Romance <= 10:
                            break
                        else:
                            continue
                    else:
                        continue

                while True:
                    Terror = input(""" • Digite a quantidade de filmes de terror/suspense para sortear (0 a 10): """)
                    if Terror.isdigit():
                        Terror = int(Terror)
                        if Terror <= 10:
                            break
                        else:
                            continue
                    else:
                        continue
                
                Total = Ação + Aventura + Comédia + Drama + Fantasia + Ficção_científica + Romance + Terror
                a = av = c = d = f = fi = r = t = 0

                while a < Ação:
                    print("   ")
                    print(" • Os filmes de Ação foram:")
                    while a < Ação:
                        sorteioAção = random.choice(listAção)
                        listAção.remove(sorteioAção)
                        print(f"  > {sorteioAção}")
                        a+= 1
                
                while av < Aventura:
                    print("   ")
                    print(" • Os filmes de Aventura foram:")
                    while av < Aventura:
                        sorteioAventura = random.choice(listAventura)
                        listAventura.remove(sorteioAventura)
                        print(f"  > {sorteioAventura}")
                        av+= 1

                while c < Comédia:
                    print("   ")
                    print(" • Os filmes de Comédia foram:")
                    while c < Comédia:
                        sorteioComédia = random.choice(listComédia)
                        listComédia.remove(sorteioComédia)
                        print(f"  > {sorteioComédia}")
                        c+= 1

                while d < Drama:
                    print("   ")
                    print(" • Os filmes de Drama foram:")
                    while d < Drama:
                        sorteioDrama = random.choice(listdrama)
                        listdrama.remove(sorteioDrama)
                        print(f"  > {sorteioDrama}")
                        d+= 1

                while f < Fantasia:
                    print("   ")
                    print(" • Os filmes de Fantasia foram:")
                    while f < Fantasia:
                        sorteioFantasia = random.choice(listFantasia)
                        listFantasia.remove(sorteioFantasia)
                        print(f"  > {sorteioFantasia}")
                        f+= 1

                while fi < Ficção_científica:
                    print("   ")
                    print(" • Os filmes de Ficção científica foram:")
                    while fi < Ficção_científica:
                        sorteioFicção = random.choice(listFicção_científica)
                        listFicção_científica.remove(sorteioFicção)
                        print(f"  > {sorteioFicção}")
                        fi+= 1

                while r < Romance:
                    print("   ")
                    print(" • Os filmes de Romance foram:")
                    while r < Romance:
                        sorteioRomance = random.choice(listRomance)
                        listRomance.remove(sorteioRomance)
                        print(f"  > {sorteioRomance}")
                        r+= 1

                while t < Terror:
                    print("   ")
                    print(" • Os filmes de Terror foram:")
                    while t < Terror:
                        sorteioTerror = random.choice(listTerror)
                        listTerror.remove(sorteioTerror)
                        print(f"  > {sorteioTerror}")
                        t+= 1

                print("   ")
                print(f""" • Totalizando {Total} filme(s)! """)
                print(" • Site para ver em quais plataformas o filme está disponível: "'https://www.justwatch.com/br')
                break

        elif menu == 4:
            while True:
                ListaTerror = ["Chamado de Cthulhu - H.P Lovecraft", "Na cripta - H.P. Lovecraft", "It, a coisa - Stephen King", "O iluminado - Stephen King", 
                "O Corvo - Edgar Alan Poe", "Frankenstein - Mary Shelley", "Drácula - Bram Stoker", "HEX - Thomas Olde Heuvelt", 
                "O Médico e o Monstro - Robert Louis Stevenson", "A Assombração da Casa da Colina - Shirley Jackson", "A Loteria - Shirley Jackson"]
                ListaFantasia = ["O Senhor dos Anéis - J.R.R Tolkien", "Crônicas de Nárnia - C.S Lewis", "O Hobbit - J.R.R. Tolkien", "Trilogia Tormenta - Leonel Caldela", 
                "A Lenda de Ruff Ghanor - Leonel Caldela", "Série Harry Potter - J.K. Rowling", "Duna - Frank Herbert", "Deuses Americanos - Neil Gaiman", 
                "Crônicas de Gelo e Fogo - George Martin", "A Deusa no Labirinto - Karen Soarele", "O Nome do Vento - Patrick Rothfuss", 
                "A Batalha do Apocalipse - Eduardo Spohr", "O Espadachim de Carvão - Affonso Solano"]
                ListaDistopia = ["1984 - George Orwell", "Admirável Mundo Novo - Aldous Huxley", "Androides Sonham com Ovelhas Elétricas? - Philip K. Dick", 
                "Fahrenheit 451 - Ray Bradbury", "Laranja Mecânica -  Anthony Burgess", "O Homem do Castelo Alto - Philip K. Dick", "Jogos Vorazes - Suzanne Collins", 
                "O Conto da Aia - Margaret Atwood", "A Revolução dos Bichos - George Orwell", "A Máquina do Tempo - H.G. Wells", "O Senhor das Moscas - William Golding", 
                "Não Me Abandone Jamais - Kazuo Ishiguro"]
                ListaN_Ficção = ["A invenção da natureza - Andrea Wulf", "Breve História do Tempo - Stephen Hawking", "O Mundo Assombrado pelos Demônios - Carl Sagan",
                "Brasil Uma História - Eduardo Bueno", "Esravidão - Laurentino Gomes", "Sapiens, Uma Breve História da Humanidade - Yuval Noah Harari", 
                "Darwin sem frescura: Como a ciência evolutiva ajuda a explicar algumas polêmicas da atualidade - Reinaldo José Lopes e Pirula", 
                "A Estrutura das Revoluções Científicas - Thomas Kuhn", "A Sociedade Aberta e Seus Inimigos - Karl Popper", "Universo numa Casca de Noz - Stephen Hawking",
                "Só Pode Ser Brincadeira, Sr. Feynman! = Richard Feynman", "Diário de Anne Frank - Anne Frank", "Breve História de Quase Tudo - Bill Bryson"]
                ListaFiçãoCiêntifica = ["Eu, Robô - Isaac Asimov", "Neuromancer - William Gibson", "Ozob, Protocolo Molotov - Leonel Caldela", 
                "O Guia do Mochileiro das Galáxias - Douglas Adams", "Fim da infância - Arthur C. Clarke", "A Guerra dos Mundos - H.G Wells", 
                "Trilogia Da Fundação - Isaac Asimov", "Matéria Escura - Blake Crouch", "2001: Uma Odesséia no Espaço - Arthur C. Clarke", "Jogador Nº 1 - Ernest Cline",
                "Vinte mil léguas submarinas - Júlio Verne", "As Cavernas de Aço - Isaac Asimov"]
                ListaMistério = ["O Assassinato No Expresso Oriente - Agatha Christie", "Um estudo em vermelho - Arthur Conan Doyle", 
                "O Cão dos Baskervilles - Arthur Conan Doyle", "O Assassinato de Roger Ackroyd - Agatha Christie", "O Mistério de Marie Rogêt - Edgar Allan Poe", 
                "O Código Da Vinci - Dan Brown", "E Não Sobrou Nenhum - Aghata Christie", " A última festa - Lucy Foley", "Morte no Nilo - Aghata Christie", 
                "O homem de giz - C.J. Tudor", "Joyland - Stephen King"]

                loop1 = loop2 = loop3 = loop4 = loop5 = loop6 = 0

                while loop1 == 0:
                    Terror = input(f" • Quantidade de livros de terror ou mistério para sortea (0 a 10): ")
                    if Terror.isdigit():
                        Terror = int(Terror)
                        if Terror > 10:
                            print(f" • Quantidade inválida, favor digitar uma quantidade menor ou igual a 10")
                        else:
                            loop1 += 1
                    else:
                        loop1 += 0

                while loop2 == 0:
                    Fantasia = input(f" • Quantidade de livros de Fantasia para sortear (0 a 10): ")
                    if Fantasia.isdigit():
                        Fantasia = int(Fantasia)
                        if Fantasia > 10:
                            print(f" • Quantidade inválida, favor digitar uma quantidade menor ou igual a 10")
                        else:
                            loop2 += 1
                    else:
                        loop2 += 0

                while loop3 == 0:
                    Distopia = input(f" • Quantidade de livros de Distopia para sortear (0 a 10): ")
                    if Distopia.isdigit():
                        Distopia = int(Distopia)
                        if Distopia > 10:
                            print(f" • Quantidade inválida, favor digitar uma quantidade menor ou igual a 10")
                        else:
                            loop3 += 1
                    else:
                        loop3 += 0

                while loop4 == 0:
                    N_Ficção = input(f" • Quantidade de livros de não ficção para sortear (0 a 10): ")
                    if N_Ficção.isdigit():
                        N_Ficção = int(N_Ficção)
                        if N_Ficção > 10:
                            print(f" • Quantidade inválida, favor digitar uma quantidade menor ou igual a 10")
                        else:
                            loop4 += 1
                    else:
                        loop4 += 0

                while loop5 == 0:
                    FiçãoCiêntifica = input(f" • Quantidade de livros de Ficção Ciêntifica para sortear (0 a 10): ")
                    if FiçãoCiêntifica.isdigit():
                        FiçãoCiêntifica = int(FiçãoCiêntifica)
                        if FiçãoCiêntifica > 10:
                            print(f" • Quantidade inválida, favor digitar uma quantidade menor ou igual a 10")
                        else:
                            loop5 += 1
                    else:
                        loop5 += 0

                while loop6 == 0:
                    Mistério = input(f" • Quantidade de livros de Mistério para sortear (0 a 10): ")
                    if Mistério.isdigit():
                        Mistério = int(Mistério)
                        if Mistério > 10:
                            print(f" • Quantidade inválida, favor digitar uma quantidade menor ou igual a 10")
                        else:
                            loop6 += 1
                    else:
                        loop6 += 0


                t = f = d = Nf = Fc = i = m = 0

                while t < Terror:
                    print("\n • Os livros de Terror são: ")
                    while t < Terror:
                        SorteioTerror = random.choice(ListaTerror)
                        ListaTerror.remove(SorteioTerror)
                        print(f"  > {SorteioTerror}")
                        t += 1

                while f < Fantasia:
                    print("\n • Os livros de fantasia são: ")
                    while f < Fantasia:
                        SorteioFantasia = random.choice(ListaFantasia)
                        ListaFantasia.remove(SorteioFantasia)
                        print(f"  > {SorteioFantasia}")
                        f += 1

                while d < Distopia:
                    print("\n • Os livros de distopia são: ")
                    while d < Distopia:
                        SorteioDistopia = random.choice(ListaDistopia)
                        ListaDistopia.remove(SorteioDistopia)
                        print(f"  > {SorteioDistopia}")
                        d += 1

                while Nf < N_Ficção:
                    print("\n • Os livros de não-ficção são: ")
                    while Nf < N_Ficção:
                        SorteioN_Ficção = random.choice(ListaN_Ficção)
                        ListaN_Ficção.remove(SorteioN_Ficção)
                        print(f"  > {SorteioN_Ficção}")
                        Nf += 1

                while Fc < FiçãoCiêntifica:
                    print("\n • Os livros de ficção ciêntifica são: ")
                    while Fc < FiçãoCiêntifica:
                        SorteioFiçãoCiêntifica = random.choice(ListaFiçãoCiêntifica)
                        ListaFiçãoCiêntifica.remove(SorteioFiçãoCiêntifica)
                        print(f"  > {SorteioFiçãoCiêntifica}")
                        Fc += 1

                while m < Mistério:
                    print("\n • Os livros de Mistério são: ")
                    while m < Mistério:
                        SorteioMistério = random.choice(ListaMistério)
                        ListaMistério.remove(SorteioMistério)
                        print(f"  > {SorteioMistério}")
                        m += 1

                Total = Terror + Distopia + Fantasia + N_Ficção + FiçãoCiêntifica + Mistério
                print("  ")
                print(f" • Totalizando {Total} livro(s)! ")
                break
        elif menu == 5:
            break
        else:
            print(" • Digite uma opção válida!")
    else:
        continue

tchau()