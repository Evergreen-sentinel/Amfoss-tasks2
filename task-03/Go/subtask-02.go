package main

import (
	"io/ioutil"
	"log"
)

func main() {

	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	err = ioutil.WriteFile("output.txt", input, 0644)
	if err != nil {
		log.Fatal(err)
	}
}
