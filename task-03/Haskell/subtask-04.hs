import System.IO

createStarPattern :: Int -> String
createStarPattern n = 
    let upper = concatMap (\i -> replicate ((n - i) `div` 2) ' ' ++ replicate i '*' ++ "\n") [1,3..n]
        lower = concatMap (\i -> replicate ((n - i) `div` 2) ' ' ++ replicate i '*' ++ "\n") [n-2,n-4..1]
    in upper ++ lower

main :: IO ()
main = do
    content <- readFile "input2.txt"
    let n = read content :: Int

    let pattern = createStarPattern n
    writeFile "output2.txt" pattern
