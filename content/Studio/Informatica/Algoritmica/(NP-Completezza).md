---
draft: true
---
Gran parte di questo libro `e dedicata agli algoritmi efficienti. La tipica unit`a di
misura dell’efficienza `e la velocit`a, ovvero quanto tempo impiega un algoritmo per
produrre il suo risultato. Ci sono problemi, tuttavia, per i quali non si conosce una
soluzione efficiente. Il Capitolo 34 studia un interessante sottoinsieme di questi
problemi, noti come problemi NP-completi.
Perch´e sono interessanti i problemi NP-completi? In primo luogo, sebbene non
sia stato ancora trovato un algoritmo efficiente per un problema NP-completo,
tuttavia nessuno ha dimostrato che non possa esistere un algoritmo efficiente per
uno di questi problemi. In altre parole, non sappiamo se esistano algoritmi effi-
cienti per i problemi NP-completi. In secondo luogo, l’insieme dei problemi NP-
completi gode dell’importante propriet`a che, se esiste un algoritmo efficiente per
uno di essi, allora esistono algoritmi efficienti per tutti questi problemi. Questa
relazione fra i problemi NP-completi rende molto pi`u attraente la mancanza di
soluzioni efficienti. In terzo luogo, molti problemi NP-completi sono simili, non
identici, ai problemi per i quali conosciamo gli algoritmi efficienti. Una picco-
la variazione della definizione del problema pu`o causare una grande variazione
dell’efficienza del migliore algoritmo conosciuto.
`E importante conoscere i problemi NP-completi perch´e spesso alcuni di essi si
presentano in modo inaspettato nelle applicazioni reali. Se vi chiedessero di creare
un algoritmo efficiente per un problema NP-completo, rischiereste di sprecare
molto del vostro tempo in ricerche inutili. Se riuscite a dimostrare che il problema
`e NP-completo, allora potrete impiegare il vostro tempo a sviluppare un algoritmo
efficiente che fornisce una buona soluzione, non la migliore possibile.
Come esempio concreto, considerate un’impresa di trasporti che abbia un ma-
gazzino centrale. Tutte le mattine un autocarro viene caricato presso il magazzino
e poi indirizzato alle varie destinazioni per consegnare le merci. Alla fine della
giornata l’autocarro deve ritornare al magazzino per essere pronto per il giorno
successivo. Per ridurre i costi, l’azienda intende scegliere un ordine di ferma-
te per le consegne che consenta all’autocarro di percorrere la distanza minima.
Si tratta del cosiddetto “problema del commesso viaggiatore” ed `e un proble-
ma NP-completo. Non esiste un algoritmo efficiente. Sotto opportune ipotesi, tut-
tavia, ci sono algoritmi efficienti che forniscono una distanza complessiva che
non `e molto diversa da quella minima. Il Capitolo 35 tratta questi “algoritmi di
approssimazione”.