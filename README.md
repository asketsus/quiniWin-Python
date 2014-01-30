#QuiniWin Python

QuiniWin Python is an open-source project which gives the most probable option for the spanish lottery game know as “La Quiniela”. It’s calculation is based on the power of probabilities obtained through scraping at different bookmakers. The application is configurable in the number of doubles that you want to play.

######Version:
20120903
######Author:
Antonio J. González
######Email and bug report address:
antonioj85 at gmail.com

##What is ‘La Quiniela’?
La Quiniela is the name of a spanish lottery game, managed by ‘Loterías y Apuestas del Estado’, based at National Football League Championship. The bet is made on a list of 15 games, usually 10 of First Division and 5 on Second Division.

Every game is marked with a sign for simple bets, and can made two or three signs (double and triple) for multiple bets. Permitted signs are 1, if you bet for the victory of the team listed first (usually local), the X in the event that you create that will tie, or 2, if you bet for victory team listed second (usually the visitor).

La Quiniela is intended for 55% of revenue for the awards, which are distributed by category:
* Special category: __14 hits plus fifteen plenary__: to 10% of revenue 
* 1st Category: __14 Hits__: 12% of revenue 
* 2nd Category: __13 Hits__: 8% of revenue 
* 3rd Category: __12 hits__: 8% of revenue 
* 4th Category: __11 hits__: 8% of revenue 
* 5th Category: __10 hits__: 9% of revenue

##How it works?
QuiniWin uses [www.loteriasyapuestas.es](http://www.loteriasyapuestas.es) and [www.oddsportal.com](http://www.oddsportal.com) web sites. In first place it download the current Quiniela.

Once downloaded the lottery it will do scraping in Oddsportal, a website that offers data about Spanish League matches in a point of view relative to betting. When the data is obtained for simple and double bets, the optimal values of each event are stored.

Transforms these odds to probabilities `1/odd`, it will calculate the most probably combination adjust to the limits previously parameterized.  

The whole process is automatic, handles captchas without overloading OddsPortal server to avoid prejudices derived from the use of this application.

###License
>Copyright (C) 2014  Antonio Jesús González León
>
>This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
>
>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
>
>You should have received a copy of the GNU General Public License along with this program. If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).
