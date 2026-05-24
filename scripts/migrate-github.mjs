import { readdir, readFile, writeFile } from 'fs/promises';
import { join } from 'path';
import matter from 'gray-matter';

const srcDir = '/home/ubuntu/workspace/my-hugo-blog/content/github';
const destDir = '/home/ubuntu/workspace/my-hugo-blog/src/content/githubTrending';

const files = await readdir(srcDir);

for (const file of files) {
  if (!file.endsWith('.md')) continue;
  if (file.startsWith('_index')) continue;

  const content = await readFile(join(srcDir, file), 'utf-8');
  const parsed = matter(content);
  const data = parsed.data;

  const newData = {};
  if (data.title) newData.title = data.title;
  if (data.date) newData.date = data.date;
  if (data.tags && Array.isArray(data.tags) && data.tags.length > 0) {
    newData.tags = data.tags;
  }
  if (data.author) newData.author = data.author;
  if (data.image) newData.image = data.image;
  if (data.draft) newData.draft = true;

  // Remove HTML comments
  let content2 = parsed.content.replace(/<!-- *more *-->/g, '');

  const newContent = matter.stringify(content2, newData);
  await writeFile(join(destDir, file), newContent);
}

console.log(`Migrated ${files.filter(f => f.endsWith('.md') && !f.startsWith('_index')).length} files`);
