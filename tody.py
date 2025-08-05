<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>All HTML Elements Example</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; line-height: 1.6; }
    section { margin-bottom: 40px; }
    code { background: #f4f4f4; padding: 2px 4px; border-radius: 4px; }
  </style>
</head>
<body>

  <h1>HTML Elements Example Page</h1>

  <!-- Headings -->
  <section>
    <h2>Headings</h2>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>
  </section>

  <!-- Paragraph and Formatting -->
  <section>
    <h2>Text Formatting</h2>
    <p>This is a <b>bold</b> and <i>italic</i> text. Here is <u>underlined</u> and <mark>highlighted</mark> text.</p>
    <p>This is a <small>small</small> and <strong>strong</strong> tag. <em>Emphasized</em> text too.</p>
    <p>This is a <del>deleted</del> and <ins>inserted</ins> text. <sup>Superscript</sup> and <sub>subscript</sub>.</p>
  </section>

  <!-- Links and Images -->
  <section>
    <h2>Links & Images</h2>
    <a href="https://www.google.com" target="_blank">Visit Google</a><br><br>
    <img src="https://via.placeholder.com/150" alt="Placeholder Image" />
  </section>

  <!-- Lists -->
  <section>
    <h2>Lists</h2>
    <h3>Unordered List</h3>
    <ul>
      <li>Item One</li>
      <li>Item Two</li>
      <li>Item Three</li>
    </ul>

    <h3>Ordered List</h3>
    <ol>
      <li>Step One</li>
      <li>Step Two</li>
      <li>Step Three</li>
    </ol>

    <h3>Definition List</h3>
    <dl>
      <dt>HTML</dt>
      <dd>HyperText Markup Language</dd>
      <dt>CSS</dt>
      <dd>Cascading Style Sheets</dd>
    </dl>
  </section>

  <!-- Tables -->
  <section>
    <h2>Tables</h2>
    <table border="1" cellpadding="10">
      <tr>
        <th>Name</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>Alice</td>
        <td>24</td>
      </tr>
      <tr>
        <td>Bob</td>
        <td>30</td>
      </tr>
    </table>
  </section>

  <!-- Forms -->
  <section>
    <h2>Forms</h2>
    <form>
      <label>Name:</label><br>
      <input type="text" name="name" /><br><br>

      <label>Email:</label><br>
      <input type="email" name="email" /><br><br>

      <label>Password:</label><br>
      <input type="password" name="password" /><br><br>

      <label>Gender:</label><br>
      <input type="radio" name="gender" value="male"> Male
      <input type="radio" name="gender" value="female"> Female<br><br>

      <label>Hobbies:</label><br>
      <input type="checkbox" name="hobby" value="reading"> Reading
      <input type="checkbox" name="hobby" value="sports"> Sports<br><br>

      <label>Message:</label><br>
      <textarea rows="4" cols="30"></textarea><br><br>

      <input type="submit" value="Submit" />
    </form>
  </section>

  <!-- Audio and Video -->
  <section>
    <h2>Audio and Video</h2>
    <audio controls>
      <source src="sample-audio.mp3" type="audio/mpeg" />
      Your browser does not support the audio tag.
    </audio><br><br>

    <video width="320" height="240" controls>
      <source src="sample-video.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  </section>

  <!-- Semantic Elements -->
  <section>
    <h2>Semantic Tags</h2>
    <header>Header Section</header>
    <nav>Navigation Bar</nav>
    <main>Main Content</main>
    <article>Article Content</article>
    <aside>Sidebar</aside>
    <footer>Footer Area</footer>
  </section>

  <!-- Code and Preformatted Text -->
  <section>
    <h2>Code Example</h2>
    <pre>
<code>
function greet() {
  console.log("Hello World");
}
</code>
    </pre>
  </section>

</body>
</html>