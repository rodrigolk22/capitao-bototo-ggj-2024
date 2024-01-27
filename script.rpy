
define cp = Character(_("Capitão Bototo"), color="#4efc03")
define fe = Character(_("Feroz"), color="#037ffc")
define es = Character(_("Esquelina"), color="#b103fc")
define atd = Character(_("Atendente"), color="#fc0377")
define gn = Character(_("Gnomo"), color="#03fca9")
define we = Character(_("Wesley Sniper"), color="#b6fc03")
define ra = Character(_("Rapaz"), color="#fc8803")


label start:

    $ renpy.music.set_volume(.15, 0.0, channel = "music")
    play music "Town2.ogg"

    scene cozy-cafe-street-evening
    with fade

    show bototo idle
    
    play sound "bototo/Uaaa-Que-preguiça-Es.mp3"

    cp "Uaaa! Que preguiça! Estou sem mistérios para investigar."
    
    play sound "bototo/Bem-que-podia-ter-al.mp3"

    cp "Bem que podia ter algo para investigar. Que tédio!"
    
    hide bototo idle
    with dissolve

    show bototo idle at left
    with dissolve

    show feroz idle at right
    with dissolve
    
    play sound "feroz/Olá capitão .mp3"

    fe "Olá capitão!"
    
    play sound "bototo/Olá-Feroz-Que-tal-a-.mp3"

    cp "Olá Feroz! Que tal a gente dar uma volta pelo centro da cidade? Talvez nós encontremos uma grande aventura hoje!"
    
    play sound "feroz/Então vamos logo cap.mp3"
    
    fe "Então vamos logo capitão! Por que vai chover!"
    
    play sound "bototo/Hmmm-como-você-sabe-.mp3"
    
    cp "Hmmm... como você sabe?"
    
    play sound "feroz/Olhe as nuvens capit.mp3"
    
    fe "Olhe as nuvens capitão!"
    
    hide bototo idle
    
    hide feroz idle
    
    show ceu
    $ renpy.pause (5.0)
    
    hide ceu
    
    show bototo surprised at left
    with dissolve

    show feroz idle at right
    with dissolve
    
    play sound "bototo/Feroz-vamos-correr-a.mp3"
    
    cp "Feroz vamos correr até a aquela casa!"
    
    jump achados

    return


label achados:

    scene garden-rainy
    with fade
    
    "O grupo chega até uma casa. Olhando atentamente é uma casa e achados e perdidos"
    
    show bototo idle at left
    with dissolve
    
    show feroz idle at left
    with dissolve
    
    show esquelina idle at right
    with dissolve
    
    play sound "esquelina/Olá amigos .mp3"
    
    es "Olá amigos!"
    
    play sound "bototo/Olá-Esquelina-Quanto.mp3"
    
    cp "Olá Esquelina! Quanto tempo!"
    
    play sound "feroz/Oi Esquelina .mp3"
    
    fe "Oi Esquelina!"
    
    play sound "esquelina/Vocês estão bem molh.mp3"
    
    es "Vocês estão bem molhados! Não sairam com guarda-chuva hoje?"
    
    play sound "bototo/Pois-é-minha-amiga-e.mp3"
    
    cp "Pois é minha amiga, estava andando no mundo das nuvens e não é que elas apareceram!"
    
    play sound "feroz/Esquelina você não p.mp3"
    
    fe "Esquelina, você não parece ter um guarda-chuva também."
    
    play sound "esquelina/Eu perdi o meu Eu vi.mp3"
    
    es "Eu perdi o meu... Eu vim aqui no achados e perdidos ver se a encontro..."
    
    jump storage
    
    
label storage:

    play music "Castle2.ogg"

    scene storage-room
    with fade
    
    show bototo idle at left
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    show feroz idle at left
    with dissolve
    
    show atendente at right
    with dissolve
    
    play sound "atendente/Boa tarde Aqui é os .mp3"
    
    atd "Boa tarde! Aqui é os Achados e Perdidos da cidade! Como posso ajudar vocês?"
    
    play sound "esquelina/Procuro um guarda ch.mp3"
    
    es "Procuro um guarda chuva, acho que perdi pode ser que esteja aqui... Ele é cheio de flores!"
    
    play sound "atendente/Alguém entregou esse.mp3"
    
    atd "Alguém entregou esse aqui esses dias... ele combina muito com você!"
    
    play sound "esquelina/É esse mesmo Nossa m.mp3"
    
    es "É esse mesmo! Nossa muito obrigado por guardar pra mim!"
    
    play sound "atendente/De nada Fico feliz p.mp3"
    
    atd "De nada. Fico feliz por ter encontrado!"
    
    hide atendente
    with dissolve
    
    hide esquelina idle
    with dissolve
    
    show esquelina umbrella at right
    with dissolve
    
    "Esquelina abre o guarda chuva e cai um papel de dentro."
    
    "Esquelina pega o papel, vê que tem um recado e começa a ler:"
    
    "Muito bem aventureiros! Tenho uma missão e preciso de ajuda para resolvê-lo!"
    
    "Conto com a ajuda de vocês! Sigam até a rua {b}Evidências{/b}, passem pelo {b}Observatório{/b} municipal,
    sigam por uma {b}pista{/b} de corrida. Tenham cuidado ao passar. É importante que nada fique pra trás."
    
    "Vocês vão avistar um laboratório. Lá vocês vão encontrar uma {b}solução{/b} muito importante com um cientista.
    Por favor peguem pra mim e mandem pelo correio, preciso mandar pra {b}Juiz{/b} De Fora, Minas Gerais."
    
    "Ass.: Narrador"
    
    play sound "esquelina/Nossa que bilhete es.mp3"
    
    es "Nossa que bilhete estranho! O que vocês acham?"
    
    play sound "bototo/Hmm-aí-nao-fala-nada.mp3"
    
    cp "Hmm... aí nao fala nada de pagamento. Triste, triste..."
    
    play sound "feroz/Capitão Meus instint.mp3"
    
    fe "Capitão! Meus instintos felinos de detetive apontam para uma rua aqui, que é, por acaso, totalmente do lado contrário desse bilhete."
    
    play sound "bototo/Boa-Feroz-Vamos-numa.mp3"
        
    cp "Boa Feroz! Vamos numa aventura!"
    
    play sound "esquelina/Hey Também quero ir .mp3"
    
    es "Hey! Também quero ir, me esperem!"
    
    jump streets
    

label streets:

    play music "Town2.ogg"

    scene creepy-supernatural-street
    with fade

    "Enquanto caminhavam pelas ruas, Feroz, de repente, parou e arqueou suas costas, olhando fixamente para um beco estreito."
    
    show feroz idle at right
    with dissolve
    
    show bototo idle at left
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    play sound "feroz/Capitão tem algo est.mp3"
    
    fe "Capitão, tem algo estranho ali. Meu instinto de detetive felino está agindo."
    
    "Bototo, um tanto relutante, seguiu o olhar de Feroz e encontrou uma porta aparentemente comum, mas com uma maçaneta em forma de banana."
    
    play sound "esquelina/Ah banana Eu amo ban.mp3"
    
    es "Ah, banana! Eu amo bananas!"
    
    "Esquelina, sempre ansiosa por uma aventura, sem hesitar, abriu a porta."
    
    "O grupo foi sugado para dentro. Caindo em um lugar escuro, parecido com uma caverna."
    
    jump caverna
    
    
label caverna:

    play music "Dungeon1.ogg"

    scene cave-dark
    with fade
    
    show bototo idle at left
    with dissolve
    
    show esquelina idle at right
    with dissolve
    
    show feroz idle at right
    with dissolve
    
    play sound "bototo/Alguém tem uma lante.mp3"
    
    cp "Alguém tem uma lanterna ou algo assim? Não da pra enxengar nada aqui."
    
    play sound "esquelina/Não tenho .mp3"
    
    es "Não tenho."
    
    play sound "feroz/Tipo eu tenho um lan.mp3"
    
    fe "Tipo eu tenho um lança chamas no meu bolso, mas só que não."
    
    "O grupo avistou ao longe um foco de luz. Eles se aproximaram e acharam um gnomo."
    
    hide feroz idle
    with dissolve
    
    hide esquelina idle
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    show feroz idle at left
    with dissolve
    
    show gnomo at right
    with dissolve
    
    play sound "gnomo/Olha a lanterna lant.mp3"
    
    gn "Olha a lanterna, lanterna fresquinha! Compra duas leva três!"
    
    play sound "bototo/Caramba-que-convenie.mp3"
    
    cp "Caramba que conveniente, um vendedor de lanternas justo aqui!"
    
    play sound "gnomo/Venham Venham compra.mp3"
    
    gn "Venham! Venham comprar! 10 rupias e essa bela lanterna será sua!"
    
    play sound "bototo/Onde estamos.mp3"
    
    cp "Onde estamos?"
    
    play sound "gnomo/Huuummmm na minha lo.mp3"
    
    gn "Hmmmm... na minha loja de lanternas!"
    
    play sound "bototo/Certo mas que lugar .mp3"
    
    cp "Certo, mas... que lugar é esse?"
    
    play sound "gnomo/Aqui Bem huuummm Aqu.mp3"
    
    gn "Aqui? Bem... huuummm... Aqui é um ótimo ponto para vendas de lanternas..."
    
    play sound "bototo/Essa conversa não va.mp3"
    
    cp "Essa conversa não vai levar a lugar nenhum..."
    
    play sound "bototo/Ok vou querer uma la.mp3"
    
    cp "Ok vou querer uma lanterna."
    
    "O grupo adquire uma lanterna."
    
    play sound "gnomo/Obrigado Agora me de.mp3"
    
    gn "Obrigado! Agora me deem licença um minuto, vou ascender a luz aqui. Ficar nesse escuro da muito sono."
    
    jump cave_2
    
    
label cave_2:
    
    scene cave
    with fade
    
    show bototo idle at left
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    show feroz idle at left
    with dissolve
    
    show gnomo at right
    with dissolve
    
    play sound "bototo/Mas o que Tinha luz .mp3"
    
    cp "Mas o que??? Tinha luz nessa caverna o tempo todo!"
    
    play sound "gnomo/Ninguém perguntou .mp3"
    
    gn "Ninguém perguntou..."
    
    play sound "bototo/Quero meu dinheiro d.mp3"
    
    cp "Quero meu dinheiro de volta!"
    
    play sound "gnomo/Shhiiiiu fale baixo .mp3"
    
    gn "Shhiiiiu, fale baixo. Fique com a lanterna. É uma ferramenta surpresa que vai ser útil depois."
    
    "Sem entender muito bem, o grupo resolve seguir pela caverna e encontram uma escada."
    
    "Eles sobem e sobem e sobem as escadas. Aparenta ser uma torre."
    
    "Uma escada leva eles até uma sala. A primeira sala com uma janela."
    
    jump garden
    
    
label garden:

    play music "Ship1.ogg"
    
    scene gardening-room
    with fade
    
    show bototo idle at left
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    show feroz idle at right
    with dissolve
    
    fe "Capitão tem uma janela aqui, podemos observar onde estamos."
    
    play sound "bototo/Esta dificil ver alg.mp3"
    
    cp "Está dificil ver algo daqui. Estamos muito altos."
    
    play sound "esquelina/Podemos procurar alg.mp3"
    
    es "Podemos procurar algo nessas gavetas velhas."
    
    "Feroz usa a lanterna para iluminar o cenário e encontrou um binóculos."
    
    play sound "feroz/Achei um binóculos V.mp3"
    
    fe "Achei um binóculos! Vou olhar pela janela!"
    
    fe "hmmmm achei um texto inscrito numa pedra."
    
    play sound "bototo/O que diz .mp3"
    
    cp "O que diz?"
    
    play sound "feroz/Eu não sei Está em e.mp3"
    
    fe "Eu não sei. Está em espanhol."
    
    play sound "bototo/Deixa eu ver aqui .mp3"
    
    cp "Deixa eu ver aqui..."
    
    show rock-wall
    $ renpy.pause (5.0)
    
    hide rock-wall
    
    play sound "bototo/Hmm só nos resta con.mp3"
    
    cp "Hmm só nos resta continuar subindo..."
    
    jump roof
    
label roof:

    scene rooftop-city-night
    with fade
    
    "Ao subir mais umas escadas o grupo encontram uma sala e uma pessoa."
    
    show bototo idle at left
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    show feroz idle at left
    with dissolve
    
    show wesley sniper at right
    with dissolve
    
    play sound "wesley/Olá forasteiros Sou .mp3"
    
    we "Olá forasteiros! Sou um emissário do amor. Meu nome é Wesley Sniper."
    
    play sound "wesley/Vocês estão perdidos.mp3"
    
    we "Vocês estão perdidos?"
    
    play sound "bototo/Sim As coisas estão .mp3"
    
    cp "Sim. As coisas estão muito estranhas. Só quero ir pra casa."
    
    we "Bom eu tenho uma corda de fuga, mas eu estou numa missão agora e não posso emprestar agora."
    
    we "Preciso de ajuda. Tenho que arremessar várias pétalas de flores em um casal que está la embaixo."
    
    we "O problema é que não enxergo bem eles daqui. Poderiam me ajudar a encontrar?"
    
    play sound "feroz/Claro Eu tenho um bi.mp3"
    
    fe "Claro, Eu tenho um binóculos aqui!"
    
    "Wesley Sniper empresta o binóculos e acha o casal."
    
    we "Ótimo! Achei eles!"
    
    we "Porém tem mais um coisa que estava esquecendo... antes de jogar as pétalas, era para eu começar a cantar uma música."
    
    we "Problema que não lembro a canção."
    
    play sound "bototo/Hmmm Yo no sé .mp3"
    
    cp "Hmmm... Yo no sé?"
    
    we "Isso! Era esse o nome dela!"
    
    $ renpy.music.set_volume(.75, 0.0, channel = "music")
    play music "yo-no-se.mp3"
    
    play sound "esquelina/Minha prima Catrina .mp3"
    
    es "Minha prima Catrina Caveira falava muito dessa música."
    
    we "Certo agora sim, temos tudo pronto!"
    
    "Wesley Sniper joga as pétalas de flores."
    
    we "Ok pessoal vamos descer!"
    
    "O grupo desse a torre pela corda e encontra o casal."
    
    jump final
    
label final:

    scene backyard-night
    with fade
    
    show bototo idle at left
    with dissolve
    
    show wesley sniper at left
    with dissolve
    
    show esquelina idle at left
    with dissolve
    
    show feroz idle at left
    with dissolve
    
    show casal at right
    with dissolve
    
    ra "Muito obrigado! Conquistei o coração da minha amada!"
    
    ra "Ela até topou em se mudar comigo. Vou avisar minha família la de Minas!"
    
    ra "Qualquer hora vão lá me visitar! Juiz de Fora é uma cidade boa dimais!"
    
    "E assim o grupo de heróis fizeram exatamente o que o narrador previu:"
    
    "Evidência: porta suspeita"
    
    "Observatório: lanterna"
    
    "Pista: binóculos"
    
    "Solução: música romântica"
    
    scene title
    
    "Obrigado por jogar!"
    
    
    
    
    
    
    
    

    
    
    
    
    