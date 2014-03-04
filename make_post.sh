title=$(echo $@)
name=$(git config user.name)
email=$(git config user.email)
date=$(date +%F)
time=$(date +%R)

if [ -z "$name" -o -z "$email"]; then
  echo "Install git and configure user.name and user.email"
  exit 1
fi

if [ -z "$title" ]; then
  echo "Choose a title"
  read -r -p '> ' title
  if [ -z "$title" ]; then
    echo "Exiting..."
    exit 1
  fi
fi

slug="$(echo -n "${title}" \
      | sed -e 's/[^[:alnum:]]/-/g' \
      | sed -e 's/\([\ä\ö\ü\Ä\Ü\Ö]\)/\1e/g;y/\ä\ö\ü\Ä\Ö\Ü/aouAOU/' \
      | tr -s '-')"
src=blog-src/$slug.rst


if [ -f "$src" ]; then
  echo "File $src exists. Delete it first or choose a different title"
  exit 1
fi

echo "$title
============================================================

:date: $date $time
:author: $name <$email>
:slug: $slug
:category: misc
:tags: unsorted
:summary: Short version for index and feeds (optional)

Help (delete before publishing)
-------------------------------

ReStructuredText and Markdown are supported
(\`\`*.rst\`\` and \`\`*.md\`\` files).
While the rst syntax is not very pretty, it is extremely powerful.

You can get help here:

  * http://docutils.sourceforge.net/docs/user/rst/quickstart.html

Links and paths inside the blog are prefixed with the \`\`{filename}\`\` 
macro. Here are some examples:

* \`An external link <http://cccgoe.de/>\`_

* \`A link to a different document <{filename}/article.rst>\`_

Embedding Code
--------------

.. code-block:: python

    def null():
        return 'yeah!'


" > $src

${EDITOR:-nano} $src

echo "Compile the blog locally:"
echo " make preview"
echo
echo "Submit the file if you are happy with the result:"
echo " git add \"$src\""
echo " git commit && git push"
echo
