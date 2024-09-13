import System.IO

main :: IO ()
main = do

    inputFile <- readFile "input.txt"
    writeFile "output.txt" inputFile
