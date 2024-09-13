import Control.Monad (forM_)
import Text.Printf (printf)

printStarPattern :: Int -> IO ()
printStarPattern n = do
    forM_ [1,3..n] $ \i -> do
        let padding = replicate ((n - i) `div` 2) ' '
        let stars = replicate i '*'
        putStrLn (padding ++ stars)

    forM_ [n-2,n-4..1] $ \i -> do
        let padding = replicate ((n - i) `div` 2) ' '
        let stars = replicate i '*'
        putStrLn (padding ++ stars)

main :: IO ()
main = do
    putStr "Enter a number: "
    input <- getLine
    let n = read input :: Int
    printStarPattern(n)
