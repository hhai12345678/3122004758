import cProfile
import pstats
import io
from main import main  # 假设你的主函数名为main

def profile_code():
    pr = cProfile.Profile()
    pr.enable()

    main()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()

    with open('profile_results.txt', 'w') as f:
        f.write(s.getvalue())

if __name__ == "__main__":
    profile_code()


