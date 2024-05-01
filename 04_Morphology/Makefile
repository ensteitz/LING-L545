all: 3kor.gen.hfst

3kor.lexc.hfst: 3kor.lexc
	hfst-lexc 3kor.lexc -o 3kor.lexc.hfst
3kor.twol.hfst: 3kor.twol
	hfst-twolc 3kor.twol -o 3kor.twol.hfst
3kor.gen.hfst: 3kor.lexc.hfst 3kor.twol.hfst
	hfst-compose-intersect -1 3kor.lexc.hfst -2 3kor.twol.hfst -o 3kor.gen.hfst
