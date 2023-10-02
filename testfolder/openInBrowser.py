import webbrowser
import os.path

def openInBrowser(argv):
    file = "index.html"
    check_file = os.path.isfile(file)
    if check_file:
        webbrowser.open(file, new="new")
    else:
        print("index.html has not been generated yet. Run: `py . -g` to create.")

if __name__ == "__main__":
    openInBrowser(['.','-g'])