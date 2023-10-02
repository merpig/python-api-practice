import json

filename = "testfolder/config.json"

def htmlBase(body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>
    <div class="container p-2">
        <div class="row text-bg-dark border rounded border-primary p-4 mx-0">
            <h1 class="text-center">Gif Collection</h1>
        </div>
        <div class="rounded bg-dark my-4 py-4">
            {body}
        </div>
    </div>
</body>
</html>'''

def gifRow(term,termGifs):

    cards = ""

    for termGif in termGifs:
        cards += gifCard(termGif) + "\n"

    return f'''<div class="row d-flex justify-content-center border rounded bg-light border-secondary m-4 pb-4">
    <div class="col-12">
        <h2>{term}</h2>
    </div>
    {cards}
</div>'''

def gifCard(link):
    return f'''<div class="col-lg-2 col-md-6 col-sm-12 p-2">
    <img class="card-img-top" src="{link}" alt="gif">
</div>'''

def generateHTML(argv):
    try:   
        file = open(filename, 'r')
    except FileNotFoundError: 
        print("No gifs to display. Run `py . -q {query}` to add gifs")
    else:
        try:
            contents = json.load(file)
        except json.decoder.JSONDecodeError:
            file.close()
            print("No gifs to display. Run `py . -q {query}` to add gifs")
        else:
            file.close()
            keys = list(contents)
            if len(keys):
                gifRows = ""
                for key in keys:
                    gifRows += gifRow(key, contents[key]) + "\n"
                html = htmlBase(gifRows)
                file = open("index.html","w")
                file.write(html)
                file.close()
                print("Successfully generated index.html")
            else:
                print("No gifs to display. Run `py . -q {query}` to add gifs")

if __name__ == '__main__':
    generateHTML(['.','-g'])