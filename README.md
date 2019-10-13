# Your lazy travel blog

Travel blogging is a lot of work. You have to take pictures and write stuff, and then publish it somewhere as well!

It's hard to take good pictures. Maybe--like me--you sometimes just can't be bothered. And let's just say it: there's so much great photo-content out there already!

This **lazy travel blog builder** helps you create a travel blog by linking places you visited to Instagram hashtags.

![Operating the lazy travel blog](https://gifyu.com/image/kcxW)

## Lazy lazy version

Just run `make.py` (Python>3.6!):

```python
python3 make.py
```

And type the names of the places you went to into the command line prompt. That's it. Your `index.html` page is finished and ready to be hosted e.g. on GitHub.

## Less lazy version

You can get a little fancier, while still staying lazy enough: Create a JSON file name `logs.json` with the following structure:

```json
[
    {
        "title": "your title",
        "text": "whatever there is to say",
        "date": "2019-08-29",
        "tag": "hashtag"
    }
]
```

You can add as many objects to the list as you like to.

Type a sentence as your `text` (or don't), add a `date` (or don't) and give it a `title` (or don't). At minimum you should add an Instagram hashtag under the `tag` key (or don't. it's got 'kitten' as a soothing default 🐱).

Usually, the Instagram tag can just be the place's name. But to be honest, if you're too lazy to add a tag then you should probably use the _lazy lazy version_ described above :)

After creating your `logs.json` file, simply run the script:

```python
python3 make.py
```

Tada! 🎉 Your freshly minted travel blog is ready at `index.html` and can be hosted at any static website hosting service, e.g. <a href="https://martin-martin.github.io/lazy-travel-blog/" target="_blank">here at GitHub</a>.
