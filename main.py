import modules

def main():
    try:
        modules.window.mainloop()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()