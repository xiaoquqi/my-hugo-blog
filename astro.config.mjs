import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightBlog from 'starlight-blog';
import sitemap from '@astrojs/sitemap';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({
  site: 'https://sunqi.site/',
  integrations: [
    starlight({
      title: 'IT技术文章分享',
      defaultLocale: 'root',
      locales: {
        root: {
          label: '简体中文',
          lang: 'zh-CN',
        },
      },
      plugins: [
        starlightBlog({
          title: '博客',
          recentPostCount: 5,
          authors: {
            '老孙正经胡说': {
              name: '老孙正经胡说',
            },
            '孙琦(Ray)': {
              name: '孙琦(Ray)',
            },
          },
        }),
        {
          name: 'starlight-blog-zh-cn',
          hooks: {
            'config:setup'() {},
            'i18n:setup'({ injectTranslations }) {
              injectTranslations({
                'zh-CN': {
                  'starlightBlog.authors.count_one': '{{author}} 发布了 {{count}} 篇文章',
                  'starlightBlog.authors.count_other': '{{author}} 发布了 {{count}} 篇文章',
                  'starlightBlog.pagination.prev': '较新的文章',
                  'starlightBlog.pagination.next': '较旧的文章',
                  'starlightBlog.post.lastUpdate': ' - 最后更新: {{date}}',
                  'starlightBlog.post.draft': '草稿',
                  'starlightBlog.post.featured': '精选',
                  'starlightBlog.post.tags': '标签:',
                  'starlightBlog.sidebar.all': '全部文章',
                  'starlightBlog.sidebar.featured': '精选文章',
                  'starlightBlog.sidebar.recent': '最近文章',
                  'starlightBlog.sidebar.tags': '标签',
                  'starlightBlog.sidebar.authors': '作者',
                  'starlightBlog.sidebar.rss': 'RSS',
                  'starlightBlog.tags.count_one': '标签 "{{tag}}" 下有 {{count}} 篇文章',
                  'starlightBlog.tags.count_other': '标签 "{{tag}}" 下有 {{count}} 篇文章',
                },
              });
            },
          },
        },
      ],
      customCss: ['./src/styles/custom.css'],
      components: {
        Footer: './src/components/Footer.astro',
      },
      sidebar: [
        {
          label: '编程开发',
          autogenerate: { directory: 'training' },
        },
        {
          label: '热点趋势',
          autogenerate: { directory: 'docs' },
        },
        {
          label: '关于',
          link: '/about/',
        },
      ],
      pagefind: true,
      lastUpdated: true,
      editLink: {
        baseUrl: 'https://github.com/xiaoquqi/my-hugo-blog/edit/master/content',
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/xiaoquqi/my-hugo-blog',
        },
      ],
      expressiveCode: {
        themes: ['github-light', 'github-dark'],
        styleOverrides: {
          borderRadius: '0.75rem',
        },
      },
    }),
    sitemap(),
  ],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
});
