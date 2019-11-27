import birth_names as bn
import matplotlib.pyplot as plt


def plotRankAndScores(name, gender):
    files = bn.getPaths()
    x1, y1 = bn.getAllRanks(name, gender, files)
    x2, y2 = bn.getAllScores(name, gender, files)
    ave = bn.getAverageRank(name, gender, select=False, filez=files)

    fig2, (ax3, ax4) = plt.subplots(2, 1, sharex='all', figsize=(10, 10))
    plt.xlabel("Year")
    ax3.plot(x1, y1, 'b')
    ax3.set_ylabel("Rank")
    ax3.axhline(y1.mean(), label='average = {}'.format(ave), linestyle='--', color='red')
    ax3.legend()
    ax4.plot(x2, y2, 'b')
    ax4.set_ylabel("Number of Births")
    ax4.axhline(y2.mean(), label='average = {}'.format(y2.mean()), linestyle='--', color='red')
    ax4.legend()
    plt.suptitle("Name Rank and Number of Births by Year")
    plt.show(block=False)


if __name__ == '__main__':
    plotRankAndScores("Wesley", "M")
    input("Press Enter to end display")
    print("All Done!")
