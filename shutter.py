import argparse, imgkit, os, time


def screenshot(url):
    if not os.path.exists("shots"):
        os.makedirs("shots")
    file_name = "".join([char.lower() if char.isalnum() else "_" for char in url])
    file_name = f"{os.getcwd()}/shots/{file_name}_{int(time.time())}.jpg"
    try:
    	imgkit.from_url(url, file_name, options={"quiet": ""})
    except:
    	pass
    print(file_name)

parser = argparse.ArgumentParser(
    description="Screenshot sites without having to install chrome"
)
parser.add_argument("--url", metavar="URL", help="url to screenshot", required=False)
parser.add_argument("--stdin", action="store_true", help="accept input from stdin ")

args = parser.parse_args()

if args.stdin:
    while 1:
        try:
            ipt = input()
            screenshot(ipt)
        except EOFError:
            break
elif args.url:
    screenshot(args.url)
else:
    raise Exception("URL or --stdin must be given")
