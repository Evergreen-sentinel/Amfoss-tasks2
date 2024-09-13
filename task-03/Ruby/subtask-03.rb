def print_star_pattern(n)
  (1..n).step(2) do |i|
    puts ' ' * ((n - i) / 2) + '*' * i
  end

  (n-2).step(1, -2) do |i|
    puts ' ' * ((n - i) / 2) + '*' * i
  end
end

print "Enter a number: "
n = gets.to_i
print_star_pattern(n)