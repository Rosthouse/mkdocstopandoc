# MKDocs to Pandoc

This provides several filters:

- [Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)

  Add this to your metadata:

  ```yaml
  content-tabs:
    - Tab1
    - Tab2
  ```

  Each of the listed content tabs will be rendered in the final output, in sequence. If a tab is missing, it will not be rendered.

- [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

  Admonitions will be converted to blockquotes

- [Icons](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

  Converts icons to inline images

- [Keys](https://facelessuser.github.io/pymdown-extensions/extensions/keys/)

  Keys will be converted to simple text.
