defmodule StarPattern do
  def print_star_pattern(n) do
    # Use a range with a step value directly after the range definition
    for i <- 1..n//1 do
      if rem(i, 2) == 1 do
        stars = String.duplicate("*", i)
        padding = String.duplicate(" ", div(n - i, 2))
        IO.puts("#{padding}#{stars}")
      end
    end

    for i <- (n - 2)..1//-1 do
      if rem(i, 2) == 1 do
        stars = String.duplicate("*", i)
        padding = String.duplicate(" ", div(n - i, 2))
        IO.puts("#{padding}#{stars}")
      end
    end
  end
end

IO.write "Enter a number: "
n = IO.gets("") |> String.trim() |> String.to_integer()
StarPattern.print_star_pattern(n)