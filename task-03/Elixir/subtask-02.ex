defmodule FileHandler do
  def read_and_write do
    {:ok, content} = File.read("input.txt")
    File.write("output.txt", content)
  end
end

FileHandler.read_and_write()
