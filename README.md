# [Monadical](https://monadical.com)

Simple static blog site.

### Adding a new Post

1. Write your post in Markdown
2. Make sure to add these meta tags at the very beginning

```
Title:          The most amazing blog in the world
Description:    The most amazing description in the world
Date:           2020-12-07
Image:          https://josezy.github.io/static/test-post.jpg
Tags:           tag1
                tag2
                tag3
Length:         1 min read
Author:         Jose Benitez
Author_Image:   https://josezy.github.io/static/jose.jpg
Author_Title:   JoseB
Author_Handle:  @yojosebenitez
Author_URL:     https://twitter.com/yojosebenitez
```

3. Push post as markdown to `markdown/<post-slug>.md` (you can link it from hackmd.io or stackedit.io)
4. Wait some minutes and reload site, post must automatically appear (pushing changes auto-updates post)


## Command Line Interface

### Install

```bash
pip install -r requirements.txt
```

### Update content.json

```bash
./update-content
```

### Build the Static Site

```bash
./build
```
