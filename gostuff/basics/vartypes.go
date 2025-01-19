package main

import "fmt"


func main() {
	// you can also do auto-assignment but it's still a static type
	// there is also same line decleration
	// there is also fmt.Sprintf which just returns the string instead of printing it
	// there are many more types that you can see on their website
	averageOpenRate, displayMessage := .23, "is the average open rate of your message"
	penniesPerText := 2.0
	const firstName = "Christian"
	const lastName = "Buczynski"
	const fullName = firstName + " " + lastName
	msg := fmt.Sprintf("my full name is: %s", fullName)
	var smsSendingLimit int = 5
	var costPerSMS float64 = 1.05
	var hasPermission bool = true
	var username string = "chrisbuczy"
	
	
	

	fmt.Printf(
		"%f %s \npenniesPerText is an: %T\n %v %f %v %q\n",
		averageOpenRate,
		displayMessage,
		penniesPerText,
		smsSendingLimit,
		costPerSMS,
		hasPermission,
		username,
	)

	fmt.Println(msg)
}