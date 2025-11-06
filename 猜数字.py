import random

def guess_number():
    print("🎯 猜数字游戏（1~100）")
    target = random.randint(1, 100)
    tries = 0

    while True:
        s = input("请输入你的猜测（或输入 q 退出）：").strip()
        if s.lower() == "q":
            print("已退出游戏~")
            break
        if not s.isdigit():
            print("请输入数字！")
            continue

        n = int(s)
        tries += 1

        if n < target:
            print("太小了 ↑")
        elif n > target:
            print("太大了 ↓")
        else:
            print(f"✅ 恭喜！你用了 {tries} 次就猜对了！答案是 {target}")
            # 继续玩？
            again = input("再玩一次？(y/n)：").strip().lower()
            if again == "y":
                target = random.randint(1, 100)
                tries = 0
                print("\n新的一局开始！")
            else:
                print("感谢游玩～")
                break

if __name__ == "__main__":
    guess_number()
    50