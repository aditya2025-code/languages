Deep dive into HTML. Here's everything important you should know:

---

## 📋 Tables — Displaying Data in Rows & Columns

```html
<table border="1">
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>25</td>
      <td>New York</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>30</td>
      <td>London</td>
    </tr>
  </tbody>
</table>
```

| Tag | Purpose |
|-----|---------|
| `<table>` | Creates the table |
| `<thead>` | Table header section |
| `<tbody>` | Table body section |
| `<tr>` | Table row |
| `<th>` | Header cell (bold by default) |
| `<td>` | Regular data cell |

**Spanning columns & rows:**
```html
<td colspan="2">Spans 2 columns</td>
<td rowspan="2">Spans 2 rows</td>
```

---

## 📝 Forms — Deep Dive

Forms are how users send data to a server.

```html
<form action="/submit" method="POST">

  <!-- Text input -->
  <label for="username">Username:</label>
  <input type="text" id="username" name="username" placeholder="Enter username" required>

  <!-- Password -->
  <input type="password" name="password" placeholder="Password">

  <!-- Email -->
  <input type="email" name="email" placeholder="your@email.com">

  <!-- Number -->
  <input type="number" name="age" min="1" max="100">

  <!-- Radio buttons -->
  <input type="radio" name="gender" value="male"> Male
  <input type="radio" name="gender" value="female"> Female

  <!-- Checkboxes -->
  <input type="checkbox" name="hobby" value="reading"> Reading
  <input type="checkbox" name="hobby" value="gaming"> Gaming

  <!-- Dropdown -->
  <select name="country">
    <option value="in">India</option>
    <option value="us">USA</option>
    <option value="uk">UK</option>
  </select>

  <!-- Multi-line text -->
  <textarea name="message" rows="4" cols="40" placeholder="Write here..."></textarea>

  <!-- File upload -->
  <input type="file" name="photo">

  <!-- Submit button -->
  <button type="submit">Submit</button>
  <button type="reset">Reset</button>

</form>
```

### Important Form Attributes:
| Attribute | Purpose |
|-----------|---------|
| `action` | Where to send the data |
| `method` | `GET` (visible in URL) or `POST` (hidden) |
| `required` | Makes the field mandatory |
| `placeholder` | Hint text inside the field |
| `disabled` | Disables the input |
| `readonly` | User can see but not edit |
| `maxlength` | Max number of characters |
| `min` / `max` | For number inputs |

---

## 🖼️ Media Tags — Images, Audio & Video

**Images:**
```html
<img src="photo.jpg" alt="Description" width="300" height="200">

<!-- Clickable image -->
<a href="https://google.com">
  <img src="logo.png" alt="Google">
</a>
```

**Audio:**
```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
  Your browser does not support audio.
</audio>
```

**Video:**
```html
<video width="400" controls autoplay muted loop>
  <source src="video.mp4" type="video/mp4">
  Your browser does not support video.
</video>
```

---

## 🔗 Links — All Types

```html
<!-- External link -->
<a href="https://google.com" target="_blank">Open Google</a>

<!-- Internal page link -->
<a href="about.html">About Page</a>

<!-- Jump to section on same page (anchor) -->
<a href="#contact">Go to Contact Section</a>
<section id="contact">Contact us here</section>

<!-- Email link -->
<a href="mailto:hello@email.com">Send Email</a>

<!-- Phone link -->
<a href="tel:+1234567890">Call Us</a>
```

`target="_blank"` opens the link in a **new tab**.

---

## 🧩 Semantic HTML — Full Picture

Semantic tags describe the **meaning** of content, not just appearance:

```html
<body>

  <header>
    <h1>My Website</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
    </nav>
  </header>

  <main>
    <section>
      <h2>About Me</h2>
      <p>I am a web developer.</p>
    </section>

    <article>
      <h2>Blog Post Title</h2>
      <p>Blog content goes here...</p>
    </article>

    <aside>
      <p>Related links or ads here</p>
    </aside>
  </main>

  <footer>
    <p>© 2026 My Website</p>
  </footer>

</body>
```

---

## 🏷️ Meta Tags — Inside `<head>`

Meta tags give information **about** your page to browsers and search engines:

```html
<head>
  <meta charset="UTF-8">
  <!-- Makes page mobile friendly -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Description shown in Google search results -->
  <meta name="description" content="This is my personal website">
  <!-- Keywords for search engines -->
  <meta name="author" content="Your Name">
  <title>My Page</title>
</head>
```

---

## 📦 Div & Span — Layout Containers

```html
<!-- div = block level, used for sections/layout -->
<div class="card">
  <h2>Card Title</h2>
  <p>Card content here.</p>
</div>

<!-- span = inline, used to style part of text -->
<p>Price: <span style="color:green">₹499</span> only!</p>
```

---

## 🔤 Text Formatting Tags

```html
<strong>Bold (important)</strong>
<em>Italic (emphasis)</em>
<u>Underline</u>
<s>Strikethrough</s>
<mark>Highlighted text</mark>
<small>Small text</small>
<sup>Superscript</sup> like x<sup>2</sup>
<sub>Subscript</sub> like H<sub>2</sub>O
<code>Inline code</code>
<pre>Preserved whitespace text</pre>
<blockquote>A long quoted text</blockquote>
<abbr title="HyperText Markup Language">HTML</abbr>
<br>  ← line break
<hr>  ← horizontal line
```

---

## 🪟 iFrame — Embedding Other Pages

```html
<!-- Embed another webpage -->
<iframe src="https://google.com" width="600" height="400"></iframe>

<!-- Embed a YouTube video -->
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  allowfullscreen>
</iframe>
```

---

## 🆔 id vs class — Very Important!

```html
<!-- id = unique, only ONE element can have it -->
<h1 id="main-title">Hello</h1>

<!-- class = reusable, MANY elements can share it -->
<p class="highlight">First</p>
<p class="highlight">Second</p>
```

| | `id` | `class` |
|--|------|---------|
| Unique? | Yes, only one | No, many elements |
| In CSS | `#main-title` | `.highlight` |
| In JS | `getElementById` | `getElementsByClassName` |

---

## 💡 HTML Best Practices

1. Always add `<!DOCTYPE html>` at the top
2. Use **semantic tags** over plain `<div>` everywhere
3. Always write `alt` on every `<img>`
4. Use **lowercase** for all tag names and attributes
5. Always **close** your tags properly
6. Use `id` for unique elements, `class` for groups
7. Indent your code neatly — 2 or 4 spaces per level
8. Add `<meta viewport>` for mobile-friendly pages
9. Keep your `<head>` clean with proper meta tags
10. Validate your HTML at **validator.w3.org**

---

Now you have a solid foundation in HTML! Once you're comfortable with all of this, you'll be ready to jump into **CSS** to make everything look beautiful. Want me to build a **complete sample webpage** using all these concepts together? 🚀