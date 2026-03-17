from test_tp2 import test_dynamic_controls,test_dynamic_loading,test_infinite_scroll,test_notification_message

def main():
    print("\n" + "=" * 60)
    print("CORRECTION TP2 - SELENIUM PYTHON POM")
    print("=" * 60)

    try:
        test_dynamic_controls()
        test_dynamic_loading()
        test_notification_message()
        test_infinite_scroll()

        print("\n" + "=" * 60)
        print("TOUS LES TESTS DU TP2 SONT PASSÉS")
        print("=" * 60)

    except Exception as e:
        print(f"\nÉCHEC GLOBAL DU TP2 : {e}")


if __name__ == "__main__":
    main()