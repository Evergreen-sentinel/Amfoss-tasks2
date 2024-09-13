defmodule StarPattern do
  # Function to generate and print the star pattern
  def print_star_pattern(n) do
    top_half =
      for i <- 1..n//1, rem(i, 2) == 1 do
        stars = String.duplicate("*", i)
        padding = String.duplicate(" ", div(n - i, 2))
        "#{padding}#{stars}\n" # Return the line as a string
      end

    bottom_half =
      for i <- (n - 2)..1//-1, rem(i, 2) == 1 do
        stars = String.duplicate("*", i)
        padding = String.duplicate(" ", div(n - i, 2))
        "#{padding}#{stars}\n" # Return the line as a string
      end

    # Concatenate top and bottom halves
    Enum.join(top_half ++ bottom_half)
    |> String.trim() # Remove any trailing newlines
  end

  # Function to read the input and write the pattern to a file
  def write_pattern_to_file do
    {:ok, content} = File.read("input2.txt")
    n = String.trim(content) |> String.to_integer()
    pattern = print_star_pattern(n)

    # Write the pattern to output2.txt
    File.write("output2.txt", pattern)
  end
end

# Call the function to write the pattern to a file
StarPattern.write_pattern_to_file()
