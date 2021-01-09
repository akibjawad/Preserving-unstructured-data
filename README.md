In this experiment, my goal was to implement an existing data anonymization technique. 
For this reason: I took an unlabeled dataset. Since I need unstructured data, I collected the message column of the data file only. 
Data file was bbc.csv.
I took that file and collected message column of the file. My goal was to modify each message in a way so that, each private information from the original text file is replaced with a fake information in the output. 

Observation summary with few examples form the result: 
| message in the input file | anonymized message | Comment |
| ------------------------- | ------------------ | ------- |
| The letter Malaysia's acting Transport Minister Hishammuddin Hussein was handed during the #MH370 press conference | The letter Laura's acting Transport Minister Brian was handed during the #Mark press conference | Here name of the acting Transport Minister Hishamuddin is replace by Brian, Conference name MH370 replaced with Mark, But one problem it replaced "Malaysia" with a person name "Laura" |
| Jack Sanderson was riding his motorbike on one of Europe's most dangerous stretches of tarmac, the A537 Cat and Fiddle road in Cheshire.  He subsequently published this video as a warning to others. | Lori was riding his motorbike on one of Kimberly's most dangerous stretches of tarmac, Gregory road in Billy.  He subsequently published this video as a warning to others. | Here, Jack Sanderson -> Lori, Europe -> Kimberly, "A537 Cat and Fiddle" -> Gregory, Cheshire -> Billy |
| A soldier who served in Iraq has killed three and injured 16 at #FortHood army base in Texas before shooting himself. The attack has left at least one person dead and 14 injured. Other reports speak of four dead.US President Barack Obama has vowed to investigate fully. | A soldier who served in Linda has killed Allison and injured Colleen at #FortHood army base in John before shooting himself. The attack has left Joseph dead and Jason injured. Other reports speak of Samantha dead.US President Janice has vowed to investigate fully. | Iraq -> Linda, "killed 3 and injured 16" -> killed Allison and injured Colleen, Barack Obama -> Janice, Texas-> John | 
| Are children ready to learn at primary school after leaving nursery care? Ofsted's chief inspector says many are not. | Are children ready to learn at primary school after leaving nursery care? Lindsey's chief inspector says many are not. | Ofsted's -> Lindsey's |
| BREAKING NEWS: F1 champion Michael Schumacher shows 'moments of consciousness' after months in a coma, his agent has said http://bbc.in/1mP04zD | BREAKING NEWS: F1 champion Michael shows 'moments of consciousness' after some period in a coma, his agent has said http://bbc.in/1mP04zD | Michael Schumacher -> Michael, months-> some period, |
| Have you ever seen a cross between a goat and a sheep? You have now...Video courtesy of the Irish Farmers | Have you ever seen a cross Meghan? You have now...Video courtesy of Gerald | "a goat and a sheep" -> "Meghan", "Irish Farmers" -> Gerald |


Now let's check problems of current model, Current model detects private info correctly, but it sometimes fail to detect type of private info. See Malaysia is replaced by a person's name. To solve this we need train the model with data. which has enough country names. 
Second problem is sentence meaning is different if we just replace private noun phrases. See the last example, "a goat and a sheep" is replaced by a "person name". 
