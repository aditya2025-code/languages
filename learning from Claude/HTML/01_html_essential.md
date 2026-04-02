# Welcome to HTML! 🌐

HTML (HyperText Markup Language) is the backbone of every webpage. Let me walk you through the essentials!

---

## 🏗️ What is an HTML Tag?

Tags are the building blocks of HTML. Most come in **pairs** — an opening and a closing tag:

```html
<tagname> content here </tagname>
```

The closing tag has a forward slash `/` before the name.

---

## 📌 Basic Structure of Every HTML Page

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My First Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>This is my first webpage.</p>
  </body>
</html>
```

| Tag | Purpose |
|-----|---------|
| `<!DOCTYPE html>` | Tells the browser this is HTML5 |
| `<html>` | Root of the entire page |
| `<head>` | Metadata (not visible on page) |
| `<title>` | Tab title in the browser |
| `<body>` | Everything visible on the page |

---

## 🔤 Common Tags to Know

**Headings** — `<h1>` to `<h6>` (h1 is biggest)
```html
<h1>Main Title</h1>
<h2>Sub Title</h2>
```

**Paragraph**
```html
<p>This is a paragraph of text.</p>
```

**Links**
```html
<a href="https://google.com">Click me!</a>
```

**Images**
```html
<img src="photo.jpg" alt="A beautiful photo">
```

**Lists**
```html
<!-- Unordered (bullets) -->
<ul>
  <li>Apple</li>
  <li>Banana</li>
</ul>

<!-- Ordered (numbers) -->
<ol>
  <li>Step one</li>
  <li>Step two</li>
</ol>
```

**Bold & Italic**
```html
<strong>Bold text</strong>
<em>Italic text</em>
```

---

## 🎯 What are Attributes?

Attributes give **extra information** to a tag. They go inside the opening tag:

```html
<tagname attribute="value"> content </tagname>
```

| Attribute | Used On | Purpose |
|-----------|---------|---------|
| `href`    | `<a>`   | Link destination |
| `src`     | `<img>`, `<script>` | File source/path |
| `alt`     | `<img>` | Text if image fails to load |
| `id`      | Any tag | Unique identifier |
| `class`   | Any tag | Group elements (for CSS) |
| `style`   | Any tag | Inline CSS styling |
| `type`    | `<input>` | Input type (text, email…) |

---

## 📦 Div & Span — The Layout Tags

```html
<!-- div is a block-level container -->
<div class="box">
  <p>Some content here</p>
</div>

<!-- span is an inline container -->
<p>My name is <span style="color:red">Alex</span>.</p>
```

---

## 📝 Forms — Getting User Input

```html
<form>
  <label for="name">Name:</label>
  <input type="text" id="name" placeholder="Enter your name">

  <label for="email">Email:</label>
  <input type="email" id="email">

  <button type="submit">Submit</button>
</form>
```

---

## 💡 Key Things to Remember

1. **Always close your tags** — `<p>text</p>` ✅ not just `<p>text` ❌
2. **Some tags are self-closing** — `<img>`, `<input>`, `<br>`, `<hr>`
3. **Indentation matters** for readability (not for the browser, but for you!)
4. **Comments** look like this: `<!-- this is a comment -->`
5. **HTML is not case-sensitive**, but lowercase is best practice

---
