from nltk.tokenize import sent_tokenize
import networkx as nx
import math
import matplotlib.pyplot as plt
def sentences(text):
    '''Break text blob into sentences'''
    return sent_tokenize(text,language='norwegian')

def connect(nodes):
    '''Return a list of edges connecting the nodes, where the edges are given a
    weight based on their similarity.'''
    return [(start,end ,similarity(start, end)) for start in nodes for end in nodes if start is not end]

def similarity(c1,c2):
    '''Return the amount of similarity between two chunks.'''
    return len(common_words(c1, c2))/(math.log(len(c1))+math.log(len(c2)))

def common_words(c1,c2):
    elem1 = [x for x in c1.split()]
    elem2 = [x for x in c2.split()]
    #print (c1)
    #print(c2)
    c3=list()
    for item in elem1:
        if item in elem2:
            c3.append(item)
    #print(c3)
    return c3

def rank(nodes,edges):
    '''Return a dicitionary containing the scores for each vertex.'''
    graph=nx.diamond_graph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(edges)
    return nx.pagerank(graph)

def summarize(text,num_summaries=6):
    '''Create small summaries of larger text.'''
    nodes=sentences(text)
    edges=connect(nodes)
    print(edges)
    print(nodes)
    scores=rank(nodes,edges)
    print (scores)
    return sorted(scores,key=scores.get)[:num_summaries]

text= """Endringar i lov om avleveringsplikt for allment tilgjengelege dokument (innsamling av digitale dokument m.m.)
Kulturdepartementet legg med dette fram forslag til endringar i lov 9. juni 1989 nr.32 om avleveringsplikt for allment tilgjengelege dokument.
Pliktavlevering er eit lovpålagt krav til alle utgivarar, trykkjeri, produsentar og importørar av dokument om å levere frå seg eksemplar av alt materiale som er gjort tilgjengeleg for allmenta, til Nasjonalbiblioteket til bevaring og bruk som kjeldemateriale for forsking og dokumentasjon.
Formålet med revisjonen er å klargjere plikta til å avlevere allment tilgjengelege dokument utan omsyn til kva medium dokumenta er gjorde tilgjengelege i. Både fysisk og digitalt materiale er avleveringspliktig og skal behandlast likt, så langt det er formålstenleg. Det er viktig at dei same vilkåra og prinsippa blir lagde til grunn for avlevering, automatisert innsamling (hausting) og bevaring av alle medietypar.
I dag digitaliserer Nasjonalbiblioteket store delar av samlinga av sikrings- og konserveringsomsyn. Dette vil kunne gjerast meir kostnadseffektivt dersom Nasjonalbiblioteket kan få levert det digitale grunnlagsmaterialet saman med utgivingsformatet. Departementet foreslår derfor å påleggje utgivaren å levere frå seg det digitale grunnlagsdokumentet saman med utgivingsformatet. Departementet understrekar samtidig at bruken av dette materialet skal regulerast i forskrift, og at bruken skal vere innanfor dei rammene som blir sette av internasjonale konvensjonar. Dette er behandla nærare i kapittel 4.
Departementet foreslår også ein heimel som gir Nasjonalbiblioteket rett til automatisert innsamling (hausting) av digitale, internettbaserte dokument. Sidan ein slik innsamlingsrett kan reise særlege utfordringar for personvernet, er trygginga av personvernet behandla særskilt. Omsyn til kulturvernet tilseier at det er viktig å ta vare på mest mogleg materiale. Samtidig er det eit viktig personvernprinsipp at kvar enkelt har rett til kontroll over eigne personopplysningar. Det har derfor vore viktig å sikre personvernet gjennom å foreslå ein særskild heimel for bevaring. Av personvernomsyn er det også foreslått strengare reglar for tilgang til nettarkivet enn dei som gjeld for anna pliktavlevert materiale. Forslaget sikrar at bevaringa av informasjonen blir gjord med så få inngrep i personvernet til kvar enkelt som mogleg. Dette er behandla nærare i kapitla 6, 7 og 8.
Det er særlege utfordringar knytte til personvernet for barn i samband med den auka aktiviteten deira på Internett. Ein bør derfor ta ekstra omsyn til personvernet for barn når ein samlar inn materiale frå nettsider. Inngrepet i personvernet til den enkelte blir mindre dersom høvet til klausulering og sletting blir utvida. Dette er behandla nærare i kapittel 7.
Endringsforslaget inneber:Det blir slått fast at både fysiske og digitale dokument skal avleverast. Utgivar eller produsent blir pålagd å avlevere det digitale grunnlagsmaterialet for dokumentet, i tillegg til utgivingsmediet.
Nasjonalbiblioteket får heimel til å gjere ei automatisk innsamling (hauste) av norsk materiale som er gjort allment tilgjengeleg på Internett.
Desse tiltaka er foreslått for å sikre personvernomsyn ved innsamling av nettdokument:Nasjonalbiblioteket skal informere om innsamling av nettmateriale både før og under sjølve innsamlinga.
Passordverna sider som ikkje er allment tilgjengelege, skal ikkje avleverast.Informasjon på passordverna sider som er allment tilgjengelege ved at alle kan få tilgang til dei gjennom registrering eller betaling, skal avleverast i den grad dei ville vore omfatta av avleveringsplikta om dei vert gitte ut i anna format.
Det blir gitt avgrensa tilgang til dei delane av nettarkivet som vil kunne innehalde personsensitivt materiale. Den personopplysningane gjeld, vil kunne be Nasjonalbiblioteket om å søkje etter eigne personlege opplysningar, for så å kunne søkje Nasjonalbiblioteket om å få merknad hefta til dokumentet, eller om at opplysningane blir klausulerte eller i nokre tilfelle sletta.
Informasjon som er lagd ut av privatpersonar under 18 år, eller som omhandlar personar under verjemål med fråtaking av rettsleg handleevne, kan ein krevje klausulert og i somme tilfelle sletta.
Personopplysningar som det aldri har vore meininga å gjere tilgjengelege for allmenta, eller som er lagde ut av tredjemann og ikkje er gjorde alminneleg kjende av den personopplysningane gjeld, kan ein krevje klausulerte eller sletta.
Ein person som har gjort allment tilgjengeleg personopplysningar om seg sjølv, kan krevje at personopplysningane blir klausulerte eller sletta dersom det vil medføre ei vesentleg ulempe at informasjonen blir oppbevart til forskingsformål.
Departementet foreslår at det skal opprettast ei særskild nemnd som skal behandle avslag på søknad om klausulering eller sletting. Definisjonen av omgrepet dokument blir foreslått endra slik at han blir tilsvarande som for dokumentomgrepet i mellom anna arkivlov, forvaltningslov og offentleglov.
Departementet foreslår å fjerne konsesjonskravet som vilkår for pliktavlevering av kringkasting."""

summary=summarize(text)
summary=str(summary).replace('\',','')
summary=summary.replace('\'','')
summary=summary.replace('[','')
summary=summary.replace(']','')

print (summary)