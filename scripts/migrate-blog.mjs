import { readdir, readFile, writeFile } from 'fs/promises';
import { join } from 'path';
import matter from 'gray-matter';

const srcDir = '/home/ubuntu/workspace/my-hugo-blog/src/content/docs/blog';

const files = await readdir(srcDir);

for (const file of files) {
  if (!file.endsWith('.mdx')) continue;

  const srcPath = join(srcDir, file);
  const content = await readFile(srcPath, 'utf-8');
  const parsed = matter(content);
  const data = parsed.data;

  // Build new frontmatter
  const newData = {};

  if (data.title) newData.title = data.title;
  if (data.date) newData.date = data.date;

  // Handle tags: keep if non-empty
  if (data.tags && Array.isArray(data.tags) && data.tags.length > 0) {
    newData.tags = data.tags;
  }

  // Handle author → authors
  if (data.author) {
    newData.authors = [data.author];
  }

  // Handle draft
  if (data.draft) newData.draft = true;

  // Handle featured image
  if (data.image) {
    newData.cover = { alt: data.title || '', image: data.image };
  }

  // Handle _index files specially
  if (file.startsWith('_index')) {
    const newContent = matter.stringify(parsed.content, { title: data.title || '博客' });
    await writeFile(srcPath, newContent);
    console.log('Index:', file);
    continue;
  }

  const newContent = matter.stringify(parsed.content, newData);
  await writeFile(srcPath, newContent);
  console.log('Blog:', file, '- tags:', newData.tags?.length || 0);
}

console.log('\nDone!');
