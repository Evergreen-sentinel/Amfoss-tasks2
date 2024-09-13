def print_star_pattern(n)
  pattern = ""

  (1..n).step(2) do |i|
    pattern += ' ' * ((n - i) / 2) + '*' * i + "\n"
  end

  (n-2).step(1, -2) do |i|
    pattern += ' ' * ((n - i) / 2) + '*' * i + "\n"
  end

  pattern
end

s = File.read("input2.txt").to_i

pattern = print_star_pattern(s)

File.open("output2.txt", "w") do |f|
  f.write(pattern)
end