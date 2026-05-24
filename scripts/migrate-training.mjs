import { readdir, readFile, writeFile } from 'fs/promises';
import { join, extname } from 'path';
import matter from 'gray-matter';

const baseDir = '/home/ubuntu/workspace/my-hugo-blog/src/content/docs';

async function processDir(dir) {
  const entries = await readdir(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = join(dir, entry.name);

    if (entry.isDirectory()) {
      await processDir(fullPath);
      continue;
    }

    const ext = extname(entry.name);
    if (ext !== '.md' && ext !== '.mdx') continue;

    const content = await readFile(fullPath, 'utf-8');
    const parsed = matter(content);
    const data = parsed.data;

    const newData = {};
    if (data.title) newData.title = data.title;
    if (data.date) newData.date = data.date;
    if (data.tags && Array.isArray(data.tags) && data.tags.length > 0) {
      newData.tags = data.tags;
    }
    if (data.author) {
      newData.authors = [data.author];
    }
    if (data.draft) newData.draft = true;
    if (data.linkTitle) newData.linkTitle = data.linkTitle;

    // Remove Hugo-specific fields: slug, weight, prev, next, sidebar
    // These are handled by the gray-matter — we simply don't copy them to newData

    // Remove <!-- more --> and <!--more--> from content
    let content2 = parsed.content.replace(/<!-- *more *-->/g, '');

    const newContent = matter.stringify(content2, newData);
    await writeFile(fullPath, newContent);
    console.log('Processed:', entry.name);
  }
}

await processDir(join(baseDir, 'training'));
await processDir(join(baseDir, 'docs'));
console.log('\nDone!');
