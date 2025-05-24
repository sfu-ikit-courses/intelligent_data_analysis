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
	% �������
	man("���������� �.").
    	man("������").
    	man("������ �.").
    	man("�����").
    	man("������").
    	man("������ �������").
    	man("��������").
    	man("����").
    	man("�������").
    	man("������ �������").
    	man("����").
    	man("������� �.").
    	man("���� �.").
    	man("������� �.").
    	man("���� �.").
    	man("������").
    	man("������� �.").
    	man("��������").
    	man("�������").
    	man("����������").
    	man("������ �.").
    	man("���������").
    	man("����").
    	man("������").
    	man("������").
    	man("���").
    	man("�����").
    	man("�������").

    	% �������
    	woman("������ �.").
    	woman("�����").
    	woman("��������").
    	woman("����� �.").
    	woman("�������").
    	woman("������").
    	woman("���������").
    	woman("������").
    	woman("�������").
    	woman("�����").
    	woman("��������� �.").
    	woman("������� �.").
    	woman("��������� �.").
    	woman("������").
    	woman("���������").
    	woman("�����").
    	woman("�������").
    	woman("������� �.").
    	woman("������").
    	woman("����").
    	woman("���").
    	woman("��������").

    	% ������������ �����
    	parent("������", "�����").
    	parent("������", "������").
    	parent("������", "����� �.").
    	parent("������", "������").
	
	parent("������ �.", "�����").
	parent("���������� �.", "�����").
	
    	parent("������ �.", "��������� �.").
    	parent("������ �.", "��������").
    	parent("�����", "��������").
    	parent("�����", "��������� �.").

    	parent("��������", "������").
    	parent("��������", "�������").
    	parent("��������", "������ �������").
    	parent("������", "������").
    	parent("������", "�������").
    	parent("������", "������ �������").

    	parent("������ �������", "����").
    	parent("������ �������", "������� �.").
    	parent("������ �������", "�������").
    	
    	parent("������", "���������").
    	parent("������", "������ �������").
    	parent("�������", "���������").
    	parent("�������", "������ �������").

    	parent("��������� �.", "������� �.").
    	parent("��������� �.", "�����").
    	parent("������� �.", "���� �.").

    	parent("������� �.", "������� �.").
    	parent("������� �.", "���� �.").
    	parent("����", "������� �.").
    	parent("����", "���� �.").

    	parent("��������", "���������").
    	parent("��������", "�������").
    	parent("��������", "��������").
    	parent("��������", "������� �.").
    	parent("�������", "���������").
    	parent("�������", "�������").
    	parent("�������", "��������").
    	parent("�������", "������� �.").
    	
    	parent("��������� �.", "������").
    	parent("��������", "������").

    	parent("���������", "�������").
    	parent("���������", "�����").
    	parent("���������", "�������").
    	parent("���������", "�����").

    	parent("�������", "����������").
    	parent("�����", "������ �.").

    	parent("�������", "������").
    	parent("�������", "�������").
    	parent("���", "������").
    	parent("���", "������").
    	parent("���", "�������").

    	parent("������", "����").
    	parent("������� �.", "����").

    	parent("�������", "�����").
    	parent("�������", "����").

    	parent("������", "����").
    	parent("������", "���").
    	parent("�����", "����").
    	parent("�����", "���").

    	% �����
    	married_couple("������ �.", "���������� �.").
    	married_couple("���������� �.", "������ �.").
    	
    	married_couple("������ �.", "�����").
    	married_couple("�����", "������ �.").

    	married_couple("������� �.", "����").
    	married_couple("����", "������� �.").
    	
    	married_couple("�������", "������").
    	married_couple("������", "�������").

    	married_couple("��������", "������").
    	married_couple("������", "��������").
    	
    	    	
    	married_couple("������ �������", "�������").
    	married_couple("�������", "������ �������").
    	
    	married_couple("��������� �.", "��������").
    	married_couple("��������", "��������� �.").

    	married_couple("��������", "�������").
    	married_couple("�������", "��������").

    	married_couple("���������", "���������").
    	married_couple("���������", "���������").

   	married_couple("�������", "���").
    	married_couple("���", "�������").

    	married_couple("������� �.", "������").
    	married_couple("������", "������� �.").

    	married_couple("������", "�����").
    	married_couple("�����", "������").
    	
    	
    	% ������� (grandfather)
	% ���������� ���� [�����] (first_coustin_brother)
	% (N)-������� ���� (n_coustin_uncle)
	% (N)-������� ��������� (������ ������) (any_coustin_nephew)
	% ����� [��� ����������] (husband_of_wifes_sister)
	
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