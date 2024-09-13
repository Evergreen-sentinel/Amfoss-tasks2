s = File.read("input.txt")

File.open("output.txt", "w") do |f|
  f.write(s)
end