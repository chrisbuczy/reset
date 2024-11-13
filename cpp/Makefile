CFLAGS = -std=c++14

output: book.o
	g++ book.o $(CFLAGS) -o book
	rm book.o

book.o: book.cpp
	g++ -c $(CFLAGS) book.cpp

clean:
	rm *.o