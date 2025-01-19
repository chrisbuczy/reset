package main

import "fmt"

// go by default is pass by value
func increment(y int) {
	y++
}
func main() {
	x := 5
	increment(x)

	fmt.Println(x)
}