# Marie Antoinette to Fersen, June 29, 1791

# Historical context

On the night of June 20, 1791, King Louis XVI, Queen Marie Antoinette, and their children, fearing for their lives, decided to flee Paris for the citadel of Montmédy, near the border in the northeast of the Kingdom of France. Arrested in Varennes, the royal family returned to Paris on June 25 and was placed under house arrest in the Tuileries Palace. On June 29, 1791, Marie Antoinette wrote a coded letter to one of their accomplices in the escape, Count Axel von Fersen. This letter, received by the Count on July 4, 1791, was published at the end of the 19th century, but parts of the text had been deliberately omitted.
But what did this letter contain?

# Letter

7 juil 1791           ce 29 juin
```
fesietsmqnpianfipestseftuoercofskdmra
rnusjxiit&irqeistgexegopsutausjivmug
pbanneditmuccuqceforsfopfarszqepagofr
&onngdinmsroevslbecl&cfebpsr&ebt&re
qeeueblicyv&uxakrnvin&macoicekpksqe
geoantiors&xuoxekegsrraoptqekefepekpes
ccgscucagcpn&rstsxbemngactauscisa
v&uxqciiorstvazxoktndecit&umssrcibp&r
kuxicofsnadafsxisziorsfoxmusyapdiagua
jrukegnriacalfmssgezanepoesieetuafity
xogektualqpibi&nsmkrdipeoakisnfafsa
mllsefertlopsmrqigeuagetdruuefrkdyeplu
p&ueaem&dasdopmsssanmavruesnvqufp&
ueedmsnkg&u&uxpfurmqiyere&ocrpae

pnugvrueeorer&meixrneidknflamrnze
ienegmam&euhsrxegopsfdfrsreufqpaba
popt
```


# Decoding table

|Key| | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|A  |AB |CD |EF |GH |IK |LM |NO |PQ |RS |TU |XY |Z& |
|B  |AC |BK |DU |EI |FL |GN |HO |MY |PS |QX |RT |Z& |
|C  |AD |BG |CZ |EK |FM |HT |IX |LR |NP |OQ |S& |UY |
|D  |AE |BZ |CT |DK |FI |GS |HY |LQ |MX |NR |O& |PU |
|E  |AF |BL |CI |DH |EU |GK |MT |NQ |OR |P& |SX |YZ |
|F  |AH |BF |CL |DG |EQ |IY |KP |MU |NS |O& |RX |TZ |
|G  |AG |BI |CL |DN |ER |FP |HT |KU |M& |OX |QY |SZ |
|H  |AI |BT |CS |DO |EL |F& |GH |KM |NQ |PR |UY |XZ |
|IJ |AK |BT |CS |DX |EI |FL |GZ |HY |M& |NP |OQ |RU |
|K  |AL |BO |CP |DG |ER |FS |HU |IX |KY |MZ |N& |QT |
|L  |AM |BZ |CD |EG |FI |HK |LN |OR |PS |QU |TY |X& |
|M  |AN |BO |CP |DQ |ER |FS |GT |HU |IX |KY |LZ |M& |
|N  |AO |BC |DM |EP |FS |GN |HY |IU |KT |LQ |R& |XZ |
|O  |AP |BL |CK |DQ |ES |FU |GX |HZ |I& |MO |NR |TY |
|P  |AQ |BX |CU |DZ |ES |FO |GY |HT |IN |KR |L& |MP |
|Q  |AR |BZ |CT |DH |EU |FQ |GO |IL |KN |MP |SY |X& |
|R  |AS |BN |CQ |DT |EU |FY |G& |HO |IP |KR |LX |MZ |
|S  |AT |BP |CQ |DR |E& |FS |GU |HX |IY |KZ |LN |MO |
|T  |AU |BY |CM |DX |E& |FH |GQ |IR |KZ |LS |NP |OT |
|UV |AX |BL |CO |DQ |ES |FU |GT |HY |IN |KZ |M& |PR |
|X  |AY |B& |CZ |DE |FX |GU |HI |KT |LS |MR |NP |OQ |
|Y  |AZ |BU |CG |DH |EX |FY |IO |K& |LN |MP |QS |RT |


Decoding table credits go to Isabelle Aristide-Hastir, Valérie Nachef and Florian Kergourlay.
https://books.openedition.org/pupo/23050



# The key

The key used to decode is: depuis

("depuis" means "since")

# Decoding

- The text is encrypted with a key, alternating letters. Thus, the key is used only every other letter.
- The key is used character by character. When all the characters of the key have been used, the process returns to the first character of the key.
- There is no difference between the letters I and J, just as there is no difference between the letters U and V.
- To decode, the key must be used in this way:
1. Search the first column of the decoding table for the key character (here 'd', 'e', ​​'p', 'u', 'i', or 's').
2. Once the character is found, search the corresponding row for the character in the message.
3. This character is located in a cell with another character, which is the substitution character for the decoded message.
4. Repeat this process until the end of the text, using every other character.

# Comments

- "pfur" on line 14 is wrong; last character should be 'p'
- Marie Antoinette wrote verbs with "ez" ending (second-person plural) with "é"
- She used old French and made mistakes
- There are no accents or punctuation
- The blank line separates the front page from the back page


# Decoded letter

Using a python script to decode the text we get:

```
iexistemonbienaimeetcestpouruousadore
rquejaieteinquiettedeuousetquejevous
plainsdetoutcequeuoussouffrezdenauoir
pointdenosnouvelleslecielpermettera
quecellecivousarrivenemecriuezpasce
seraitnousexposeretsurtoutnereuenezpas
icysousaucunpretexteonsaitquecest
vousquinousavezsortidicytoutseroitper
dusiuousparaissieznoussommesgardeauue
jouretnuitcelamestegaleuousnestrasicy
soyeztranquililnemarriuerarienlasse
mbleeueutnoustraiterauecdouceuradieule
plusaimedeshommescalmevoussivouspo
uuezmenageuouspoupmoiienepourrai

plusvousecriremaisriendanslemonde
nepeumempecherdeuousadoreriusquala
mort
```

With corrections and punctuation the text becomes:

(French)
```
J'existe mon bien aimé et c'est pour vous adorer. Que j'ai été inquiète de vous et que je vous plains de tout ce que vous souffrez de n'avoir point de nos nouvelles ! Le ciel permettra que celle-ci vous arrive. Ne m'écrivez pas, ce serait nous exposer, et surtout ne revenez pas ici sous aucun pretexte. On sait que c'est vous qui nous avez sorti d'ici ; tout serait perdu si vous paraissiez. Nous sommes gardés a vue jour et nuit, cela m'est égale, vous n'êtes pas ici. Soyez tranquille, il ne m'arrivera rien. L'Assemblée veut nous traiter avec douceur. Adieu le plus aimé des hommes. Calmez-vous si vous pouvez. Menagez-vous pour moi. Je ne pourrai plus vous écrire mais rien dans le monde ne peut m'empêcher de vous adorer jusqu'à la mort.
```

(English)
```
I exist, my beloved, and it is to adore you. How worried I have been about you, and how I pity you for all that you suffer from not having any news from us! Heaven will allow this to reach you. Do not write to me; it would expose us, and above all, do not return here under any pretext. It is known that it was you who got us out of here; all would be lost if you were to appear. We are under constant surveillance day and night, but I don't care; you are not here. Be at ease, nothing will happen to me. The Assembly wishes to treat us gently. Farewell, most beloved of men. Calm yourself if you can. Take care of yourself for my sake. I will no longer be able to write to you, but nothing in the world can prevent me from adoring you until death.
```
