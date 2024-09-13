package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func printStarPattern(n int) {
	for i := 1; i <= n; i += 2 {
		padding := strings.Repeat(" ", (n-i)/2)
		stars := strings.Repeat("*", i)
		fmt.Println(padding + stars)
	}

	for i := n - 2; i >= 1; i -= 2 {
		padding := strings.Repeat(" ", (n-i)/2)
		stars := strings.Repeat("*", i)
		fmt.Println(padding + stars)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a number: ")
	input, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(input))

	printStarPattern(n)
}
