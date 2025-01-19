package main

import "fmt"

// you can also only declare type on the last parametre
// this only works if the parametres are all the same type
func concat(x string, y string) string {
	return x + y
}

func main() {
	fmt.Println(concat("hello", "world"))
}