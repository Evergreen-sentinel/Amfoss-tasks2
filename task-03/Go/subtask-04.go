package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func createStarPattern(n int) string {
	pattern := ""

	for i := 1; i <= n; i += 2 {
		padding := strings.Repeat(" ", (n-i)/2)
		stars := strings.Repeat("*", i)
		pattern += padding + stars + "\n"
	}

	for i := n - 2; i >= 1; i -= 2 {
		padding := strings.Repeat(" ", (n-i)/2)
		stars := strings.Repeat("*", i)
		pattern += padding + stars + "\n"
	}

	return pattern
}

func main() {
	content, err := ioutil.ReadFile("input2.txt")
	if err != nil {
		log.Fatal(err)
	}

	n, err := strconv.Atoi(strings.TrimSpace(string(content)))
	if err != nil {
		log.Fatal(err)
	}

	pattern := createStarPattern(n)
	err = ioutil.WriteFile("output2.txt", []byte(pattern), 0644)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Pattern written to output2.txt")
}
