---
layout: post
title: "使用Grafana+Diamond+Graphite构造完美监控面板"
date: 2015-12-01 07:59:46 +0800
comments: true
categories: [Cloud Computing]
---

服务器监控软件五花八门，没有一个是对的，但是总有一款是适合你的，本文中将使用Grafana+Dimaond+Graphite构造一款漂亮的监控面板，你可以独自欣赏，也可以让他们和你的应用勾勾搭搭。

本文中的安装测试，主要在CentOS 6.5下完成。先来张Grafna效果图，左边是我们的数据源Graphite，右边是我们的Grafna的效果图：

![](/images/blogs/grafana-screenshot.png)

<!-- more -->

## 安装及配置Dimaond

安装Diamond最直接和简单的方法就是自己编译RPM或者DEB的安装包, Diamond在这方面提供了比较好的支持。

``` bash bash
# cd /root
# yum install -y git rpm-build python-configobj python-setuptools
# git clone https://github.com/python-diamond/Diamond
# cd Diamond
# make rpm
# cd dist
# rpm -ivh diamond-*.noarch.rpm
```

默认情况下，Diamond开启了基本的监控信息，包括CPU、内存、磁盘的性能数据。当然，我们可以通过配置启动相应的监控项，也能通过自定义的方式进行相应的扩展。这里，我们在/etc/diamond/collectors加载额外的插件，下面的例子中开启了网络的监控。

``` bash bash
# cp -f /etc/diamond/diamond.conf.example /etc/diamond/diamond.conf

# cat << EOF | tee -a /etc/diamond/diamond.conf
[configs]
path = "/etc/diamond/collectors/"
extension = ".conf"
EOF

# cat << EOF | tee /etc/diamond/collectors/net.conf
[collectors]

[[NetworkCollector]]
enabled = True
EOF
```

那么到目前为止，Diamond的基本安装和配置已经完成，但是现在只是简单的采集数据，并没有指明数据要发送给谁，所以下一步我们来开始配置Graphite。

## 安装及配置Graphite

Graphite主要做两件事情：按照时间存储数据、生成图表，在我们的场景里面，实质上就是把Graphite作为数据源给Grafana提供数据。另外还需要安装的是carbon，负责通过网络接受数据并保存到后端存储中；另外还需要whisper，负责生成Graphite样式的基于文件的时间序列的数据库。

### 安装软件包

``` bash bash
# yum install -y graphite-web graphite-web-selinux
# yum install -y mysql mysql-server MySQL-python
# yum install -y python-carbon python-whisper
```

### 配置MySQL

``` bash bash
# /etc/init.d/mysqld start

# mysql -e "CREATE DATABASE graphite;" -u root
# mysql -e "GRANT ALL PRIVILEGES ON graphite.* TO 'graphite'@'localhost' IDENTIFIED BY 'sysadmin';" -u root
# mysql -e 'FLUSH PRIVILEGES;' -u root
```

### 配置Graphite

* local setting

``` bash /etc/graphite-web/local_settings.py
# SECRET_KEY=$(md5sum /etc/passwd | awk {'print $1'})

# echo "SECRET_KEY = '$SECRET_KEY'" | tee -a /etc/graphite-web/local_settings.py
# echo "TIME_ZONE = 'Asia/Shanghai'" | tee -a /etc/graphite-web/local_settings.py

# cat << EOF | tee -a /etc/graphite-web/local_settings.py
DATABASES = {
    'default': {
        'NAME': 'graphite',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'graphite',
        'PASSWORD': 'sysadmin',
    }
}
EOF

# cd /usr/lib/python2.6/site-packages/graphite
# ./manage.py syncdb --noinput

# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@hihuron.com', 'sysadmin')" | ./manage.py shell
```

* Apache配置

``` bash /etc/httpd/conf.d/graphite-web.conf
Listen 0.0.0.0:10000
<VirtualHost *:10000>
    ServerName graphite-web
    DocumentRoot "/usr/share/graphite/webapp"
    ErrorLog /var/log/httpd/graphite-web-error.log
    CustomLog /var/log/httpd/graphite-web-access.log common
    Alias /media/ "/usr/lib/python2.6/site-packages/django/contrib/admin/media/"

    WSGIScriptAlias / /usr/share/graphite/graphite-web.wsgi
    WSGIImportScript /usr/share/graphite/graphite-web.wsgi process-group=%{GLOBAL} application-group=%{GLOBAL}

    <Location "/content/">
        SetHandler None
    </Location>

    <Location "/media/">
        SetHandler None
    </Location>
</VirtualHost>
```

* Diamond配置

``` bash bash
# HOST_IP=$(ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p' | head -1)

# sed  -i "/^\[\[GraphiteHandler\]\]$/,/^\[.*\]/s/^host = 127.0.0.1$/host = $HOST_IP/" /etc/diamond/diamond.conf
# sed  -i "/^\[\[GraphitePickleHandler\]\]$/,/^\[.*\]/s/^host = 127.0.0.1$/host = $HOST_IP/" /etc/diamond/diamond.conf
```

### 启动服务

``` bash bash
# service carbon-cache restart
# service httpd restart
# service diamond restart
```

## 安装和配置Grafana

Grafana最主要的功能就是对数据的呈现，基于一切可提供time series的后台服务。这里面我们使用Graphite为Grafana提供数据。

### 安装及配置

``` bash bash
# yum install -y nodejs
# rpm -ivh https://grafanarel.s3.amazonaws.com/builds/grafana-2.5.0-1.x86_64.rpm
# sudo /sbin/chkconfig --add grafana-server
# sed -i 's/^;http_port = 3000$/http_port = 10001/g' /etc/grafana/grafana.ini
# sudo service grafana-server start
```

### 添加datasource

Grafana提供了非常丰富的REST API，我们不仅可以直接利用Grafana作为数据呈现层，还可以利用REST API直接将Grafana的Graph集成在我们的应用中。下面我们利用REST API为Grafana添加datasource。

``` bash bash
# curl -i 'http://admin:admin@localhost:10001/api/datasources' -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d '{"name": "graphite", "type": "graphite", "url": "http://localhost:10000", "access": "proxy", "basicAuth": false}'
```

## Ceph监控

### 修改ceph脚本兼容性

Diamond是基于Python开发的，但是由于CentOS 6.5的Python版本较低(2.6)，所以直接使用社区版本的Ceph监控时，会导致错误。可以通过简单的修改进行修复。

``` python /usr/share/diamond/collectors/ceph/ceph.py
    def _get_stats_from_socket(self, name):
        """Return the parsed JSON data returned when ceph is told to
        dump the stats from the named socket.

        In the event of an error error, the exception is logged, and
        an empty result set is returned.
        """
        try:
            #json_blob = subprocess.check_output(
            #    [self.config['ceph_binary'],
            #     '--admin-daemon',
            #     name,
            #     'perf',
            #     'dump',
            #     ])
            cmd = [
                 self.config['ceph_binary'],
                 '--admin-daemon',
                 name,
                 'perf',
                 'dump',
            ]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            json_blob = process.communicate()[0]
```

### 增加对ceph osd perf监控

在实际运维Ceph过程中，ceph osd perf是一个非常重要的指令，能够观察出集群中磁盘的latency的信息，通过观察变化，可以辅助判断磁盘出现性能问题。Diamond的设计中，每个Diamond Agent只会采集自己本机的指标，所以我们在添加的时候，只需要在一个节点上增加这个监控就可以了。在ceph.py中结尾处新增加一个类。

``` python /usr/share/diamond/collectors/ceph/ceph.py
class CephOsdCollector(CephCollector):

    def _get_stats(self):
        """Return the parsed JSON data returned when ceph is told to
        dump the stats from the named socket.

        In the event of an error error, the exception is logged, and
        an empty result set is returned.
        """
        try:
            #json_blob = subprocess.check_output(
            #    [self.config['ceph_binary'],
            #     '--admin-daemon',
            #     name,
            #     'perf',
            #     'dump',
            #     ])
            cmd = [
                 self.config['ceph_binary'],
                 'osd',
                 'perf',
                 '--format=json',
            ]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            json_blob = process.communicate()[0]
        except subprocess.CalledProcessError, err:
            self.log.info('Could not get stats from %s: %s',
                          name, err)
            self.log.exception('Could not get stats from %s' % name)
            return {}

        try:
            json_data = json.loads(json_blob)
        except Exception, err:
            self.log.info('Could not parse stats from %s: %s',
                          name, err)
            self.log.exception('Could not parse stats from %s' % name)
            return {}

        return json_data

    def _publish_stats(self, stats):
        """Given a stats dictionary from _get_stats_from_socket,
        publish the individual values.
        """
        for perf in stats['osd_perf_infos']:
            counter_prefix = 'osd.' + str(perf['id'])
            for stat_name, stat_value in flatten_dictionary(
                perf['perf_stats'],
                prefix=counter_prefix,
            ):
              self.log.info('stat_name is %s', stat_name)
              self.log.info('stat_value is %s', stat_value)
              self.publish_gauge(stat_name, stat_value)

    def collect(self):
        """
        Collect stats
        """
        self.log.info('in ceph osd collector')
        stats = self._get_stats()
        self._publish_stats(stats)
```

### 修改Diamond监控配置

``` bash /etc/diamond/collectors/ceph.conf
# cat << EOF | tee /etc/diamond/collectors/ceph.conf
[collectors]

[[CephCollector]]
enabled = True

[[CephOsdCollector]]
enabled = True
EOF
```

``` bash bash
# service diamond restart
```
