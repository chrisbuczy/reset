package main

import (
	"os"
	"path"
	"log"
)

func main() {
	ex, err := os.Executable()
	if err != nil { log.Fatal(err) }
	dir := path.Dir(ex)
	log.Print(dir)
}