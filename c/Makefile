all: book

book: book.o
	gcc book.o -o final
	rm book.o
	chmod +x final

book.o: book.c
	gcc -c book.c

clean:
	rm book.o
