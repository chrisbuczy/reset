package main

import "fmt"

func main() {
	height := 6.4

	// note that you can't put a newline between each if, else if, and else statement
	if height >= 6 {
		fmt.Println("You are tall enough!")
	} else if height < 6 {
		fmt.Println("You are not tall enough!")
	}
	
	// you can also initialize a variable in the if statement
	// the variable is only within the scope of the if, else if, and else statements
	if height := 6; height != 6 {
		fmt.Println("You are not 6 feet tall!")
	} else {
		fmt.Println("You're exactly 6 feet tall")
	}
}