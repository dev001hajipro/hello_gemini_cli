import random
import time
import sys

# Windows環境での文字化けを防ぐ
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def roll_dice():
    """1から6までのランダムな整数を返す"""
    return random.randint(1, 6)

def determine_round_winner(player_roll, computer_roll):
    """ラウンドの勝者を判定し、ポイントを返す"""
    # 両者1なら引き分け
    if player_roll == 1 and computer_roll == 1:
        print("-> 両者1のため、このラウンドは引き分けです。\n")
        return 0, 0
    # プレイヤーが1なら負け
    if player_roll == 1:
        print("-> あなたは1を出したので、このラウンドはコンピュータの勝ちです。\n")
        return 0, 1
    # コンピュータが1なら勝ち
    if computer_roll == 1:
        print("-> コンピュータが1を出したので、このラウンドはあなたの勝ちです！\n")
        return 1, 0
    
    # 通常の勝敗判定
    if player_roll > computer_roll:
        if player_roll == 6:
            print("-> 6を出して勝利！ボーナスで2勝分獲得です！\n")
            return 2, 0
        else:
            print("-> このラウンドはあなたの勝ちです！\n")
            return 1, 0
    elif computer_roll > player_roll:
        if computer_roll == 6:
            print("-> コンピュータが6を出して勝利。コンピュータが2勝分獲得です。\n")
            return 0, 2
        else:
            print("-> このラウンドはコンピュータの勝ちです。\n")
            return 0, 1
    else:
        print("-> このラウンドは引き分けです。\n")
        return 0, 0

def main():
    """ゲームのメインロジック"""
    player_wins = 0
    computer_wins = 0
    rounds = 3

    print("--- サイコロ対決ゲーム開始！ ---")
    print(f"{rounds}回戦で勝負します.\n")
    time.sleep(1)

    for i in range(1, rounds + 1):
        print(f"--- ラウンド {i} ---")

        # プレイヤーの番
        print("あなたの番です。")
        time.sleep(1)
        player_roll = roll_dice()
        print(f"あなたの出目: {player_roll}")

        # コンピュータの番
        print("コンピュータの番です。")
        time.sleep(1)
        computer_roll = roll_dice()
        print(f"コンピュータの出目: {computer_roll}")

        # 勝敗判定とスコア加算
        p_points, c_points = determine_round_winner(player_roll, computer_roll)
        player_wins += p_points
        computer_wins += c_points
        
        time.sleep(1.5)

    # 最終結果
    print("--- 最終結果 ---")
    print(f"あなた: {player_wins}勝")
    print(f"コンピュータ: {computer_wins}勝")

    if player_wins > computer_wins:
        print("\nおめでとうございます！あなたの総合勝利です！")
    elif computer_wins > player_wins:
        print("\n残念！コンピュータの総合勝利です。")
    else:
        print("\n総合結果は引き分けでした！")

if __name__ == "__main__":
    main()