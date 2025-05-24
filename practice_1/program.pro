domains
	person = string

predicates
	nondeterm man(person)
	nondeterm woman(person)
	nondeterm parent(person, person)
	nondeterm married_couple(person, person)
	
	nondeterm grandfather(person, person)
	nondeterm first_coustin_brother(person, person)
	nondeterm n_coustin_uncle(person, person, integer)
	nondeterm n_coustin_sibling(person, person, integer)
	nondeterm any_coustin_nephew(person, person, integer)
	nondeterm husband_of_wifes_sister(person, person)
	
clauses
	% Мужчины
	man("Константин Ф.").
    	man("Виктор").
    	man("Михаил Ф.").
    	man("Антон").
    	man("Эдуард").
    	man("Сергей старший").
    	man("Геннадий").
    	man("Артём").
    	man("Евгений").
    	man("Сергей младший").
    	man("Яков").
    	man("Алексей П.").
    	man("Егор П.").
    	man("Алексей К.").
    	man("Егор К.").
    	man("Фабиян").
    	man("Алексей В.").
    	man("Владимир").
    	man("Дмитрий").
    	man("Константин").
    	man("Михаил Б.").
    	man("Александр").
    	man("Семён").
    	man("Рустам").
    	man("Руслан").
    	man("Мир").
    	man("Данил").
    	man("Николай").

    	% Женщины
    	woman("Матрёна П.").
    	woman("Мария").
    	woman("Антонина").
    	woman("Елена П.").
    	woman("Татьяна").
    	woman("Марина").
    	woman("Анастасия").
    	woman("Тамара").
    	woman("Людмила").
    	woman("Елена").
    	woman("Валентина П.").
    	woman("Наталья К.").
    	woman("Валентина В.").
    	woman("Ксения").
    	woman("Екатерина").
    	woman("Елена").
    	woman("Надежда").
    	woman("Наталья Ш.").
    	woman("Родика").
    	woman("Ника").
    	woman("Ева").
    	woman("Серафима").

    	% Родительские связи
    	parent("Виктор", "Антон").
    	parent("Виктор", "Эдуард").
    	parent("Виктор", "Елена П.").
    	parent("Виктор", "Фабиян").
	
	parent("Матрёна П.", "Мария").
	parent("Константин Ф.", "Мария").
	
    	parent("Михаил Ф.", "Валентина П.").
    	parent("Михаил Ф.", "Антонина").
    	parent("Мария", "Антонина").
    	parent("Мария", "Валентина П.").

    	parent("Антонина", "Тамара").
    	parent("Антонина", "Людмила").
    	parent("Антонина", "Сергей старший").
    	parent("Фабиян", "Тамара").
    	parent("Фабиян", "Людмила").
    	parent("Фабиян", "Сергей старший").

    	parent("Сергей старший", "Артём").
    	parent("Сергей старший", "Наталья К.").
    	parent("Сергей старший", "Евгений").
    	
    	parent("Марина", "Анастасия").
    	parent("Марина", "Сергей младший").
    	parent("Евгений", "Анастасия").
    	parent("Евгений", "Сергей младший").

    	parent("Валентина П.", "Алексей П.").
    	parent("Валентина П.", "Елена").
    	parent("Алексей П.", "Егор П.").

    	parent("Наталья К.", "Алексей К.").
    	parent("Наталья К.", "Егор К.").
    	parent("Яков", "Алексей К.").
    	parent("Яков", "Егор К.").

    	parent("Серафима", "Екатерина").
    	parent("Серафима", "Надежда").
    	parent("Серафима", "Владимир").
    	parent("Серафима", "Алексей В.").
    	parent("Николай", "Екатерина").
    	parent("Николай", "Надежда").
    	parent("Николай", "Владимир").
    	parent("Николай", "Алексей В.").
    	
    	parent("Валентина В.", "Ксения").
    	parent("Владимир", "Ксения").

    	parent("Екатерина", "Дмитрий").
    	parent("Екатерина", "Елена").
    	parent("Александр", "Дмитрий").
    	parent("Александр", "Елена").

    	parent("Дмитрий", "Константин").
    	parent("Елена", "Михаил Б.").

    	parent("Надежда", "Рустам").
    	parent("Надежда", "Татьяна").
    	parent("Мир", "Рустам").
    	parent("Мир", "Руслан").
    	parent("Мир", "Татьяна").

    	parent("Рустам", "Семён").
    	parent("Наталья Ш.", "Семён").

    	parent("Татьяна", "Данил").
    	parent("Татьяна", "Артём").

    	parent("Родика", "Ника").
    	parent("Родика", "Ева").
    	parent("Данил", "Ника").
    	parent("Данил", "Ева").

    	% Браки
    	married_couple("Матрёна П.", "Константин Ф.").
    	married_couple("Константин Ф.", "Матрёна П.").
    	
    	married_couple("Михаил Ф.", "Мария").
    	married_couple("Мария", "Михаил Ф.").

    	married_couple("Наталья К.", "Яков").
    	married_couple("Яков", "Наталья К.").
    	
    	married_couple("Евгений", "Марина").
    	married_couple("Марина", "Евгений").

    	married_couple("Антонина", "Фабиан").
    	married_couple("Фабиан", "Антонина").
    	
    	    	
    	married_couple("Сергей старший", "Татьяна").
    	married_couple("Татьяна", "Сергей старший").
    	
    	married_couple("Валентина В.", "Владимир").
    	married_couple("Владимир", "Валентина В.").

    	married_couple("Серафима", "Николай").
    	married_couple("Николай", "Серафима").

    	married_couple("Екатерина", "Александр").
    	married_couple("Александр", "Екатерина").

   	married_couple("Надежда", "Мир").
    	married_couple("Мир", "Надежда").

    	married_couple("Наталья Ш.", "Рустам").
    	married_couple("Рустам", "Наталья Ш.").

    	married_couple("Родика", "Данил").
    	married_couple("Данил", "Родика").
    	
    	
    	% дедушка (grandfather)
	% двоюродный брат [кузен] (first_coustin_brother)
	% (N)-юродный дядя (n_coustin_uncle)
	% (N)-юродный племянник (любого уровня) (any_coustin_nephew)
	% свояк [муж свояченицы] (husband_of_wifes_sister)
	
	grandfather(X, Y) :-
		man(X),
		parent(X, Z),
		parent(Z, Y).
		
	first_coustin_brother(X, Y) :-
		man(X),
		n_coustin_sibling(X, Y, 2).
	
	n_coustin_sibling(X, Y, 1) :-
        	parent(Z, X),
        	parent(Z, Y),
        	X <> Y.
        
    	n_coustin_sibling(X, Y, N) :-
    		N > 1,
        	N1=N-1,
        	parent(Z1, X),
        	parent(Z2, Y),
        	n_coustin_sibling(Z1, Z2, N1),
        	X <> Y.
	
	n_coustin_uncle(X, Y, N) :-
		man(X),
		n_coustin_sibling(X, Z, N),
		parent(Z, Y).
		
	any_coustin_nephew(X, Y, N) :-
		n_coustin_uncle(Y, X, N).
	
	husband_of_wifes_sister(X, Y) :-
		man(X),
		man(Y),
		married_couple(Y, Z),
		n_coustin_sibling(Z, X, 1).
		
		
goal
	grandfather(X, Y).