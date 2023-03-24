# MKDocs to Pandoc

[MKDocs](https://www.mkdocs.org/) is a tool used to easily create documentation for your software projects or to write tutorials for software. The extension [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/) adds more features that help to create beautiful looking websites.

However, converting the site to, e. g. a PDF, can be a hassle, as the avaiable converters relay on software packages that are hard to install on certain operating systems.

Conversely, [Pandoc](https://pandoc.org/) is a tool that makes it easy to convert from markdown into a variety of different output formats. Some extensions done by MKDocs and Material for MKDocs make certain output hard to read.

This [filter](https://pandoc.org/filters.html) for Pandoc converts these special syntax to a format that is better suited for rendering PDF and other document formats.

## Installation and Usage

To use this filter, install it with pip and include it in your pandoc toolchain:

```
pip install mkdocstopandoc
```

```
pandoc --filter mkdocstopandoc -t output.pdf readme.md
```

## Features

- [Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)

  Add this to your metadata:

  ```yaml
  content-tabs:
    - Tab1
    - Tab2
  ```

  Each of the listed content tabs will be rendered in the final output, in sequence. If a tab is missing, it will not be rendered.

- [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

  Admonitions will be converted to blockquotes. The admonition title is added as a bolded header.

  To activate this feature, add the following to your pandoc metadata:

  ```yaml
  admonitions: true
  ```

- [Icons](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

  Icons is a useful feature that allows you to easily customize inline-text with markers. Add the path to the icons to your pandoc metadata:

  ```yaml
  icons: overrides/.icons
  ```

  > Note: this does not (yet) allow for emojis. Only custom icons are supported.

- [Keys](https://facelessuser.github.io/pymdown-extensions/extensions/keys/)

  Keys will be converted to simple text. The output will be capitalized, so that it will stick out more.

  Add the following to your pandoc metadata to enable this feature:

  ```yaml
  keys: true
  ```

- [Figure Captions](https://squidfunk.github.io/mkdocs-material/reference/images/#image-captions)

  MKDocs does not (directly) support image captions. To accomplish this, HTML tags have to be used like this:

  ```markdown
  <figure id="test" markdown>
    ![Test](testimage.png){#test}
    <figcaption>Test</figcaption>
  </figure>
  ```

  Pandoc ignores the HTML Tags and only renders the text. To not duplicate the caption, this feature allows removing the `figcaption` tag from the final render.

  Add the following to the pandoc metadata to remove the `figcaptions`:

  ```yaml
  figcaptions: true
  ```
