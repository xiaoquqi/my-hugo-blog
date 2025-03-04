---
title: 使用阿里云函数计算构建小程序
date: 2019-12-19 23:19:16
tags: [阿里云, Cloud Computing, Serverless]
---

## 1、需求

在用户使用HyperMotion产品过程中，用户可以通过扫描产品中二维码方式，自助进行Licnese申请。用户提交申请后，请求将发送到钉钉流程中。完成审批后，后台服务将自动根据用户的特征码、申请的数量、可使用的时间将生成好的正式Licnese发送到客户的邮箱中。

<!-- more -->

![](/images/blogs/2019-12-19/architecture.png)

在原有设计中，使用了Python Flask提供WEB界面，后台使用Celery异步的将用户请求发送至钉钉中，之后采用轮询方式监控审批工单状态，当工单完成审批后，将生成好的License发送至客户提供的邮箱中。

实现的效果：

![](/images/blogs/2019-12-19/UI.jpeg)

这种方式虽然可以满足需求，但是在使用过程中也发现有如下痛点：
1、由于对于可用性要求比较高，所以将整套应用以容器化方式部署在云主机上，程序高可用性依赖于底层的平台，基于成本考虑并没有在多可用区进行部署。
2、当业务变化时，需要专人将容器从本地容器库上传后进行更新，更新速度慢，敏捷性低。
3、需要专人对操作系统层进行维护，并且由于该云主机还运行了其他程序，所以管控上也存在安全风险。

基于以上出现的问题，决定对原有二维码程序进行重构，并重新部署在阿里云函数计算服务上。
1、第一阶段的改造主要是将二维码扫描程序移植到函数计算服务中。
2、第二阶段的改造主要是将发送二维码程序改造为函数计算服务，使用钉钉流程接口中的Callback方法调用该接口，在审批结束后触发发送License流程。

## 2、函数计算服务——无服务，零运维

最早接触Serverless的雏形是在2011年开发Cloud Foundry项目时，当时留下一个非常深的印象就是把写好的应用直接上传就完成了部署、扩展等。但是当时Cloud Foundry有一个非常大的局限性，受限于几种开发语言和框架。记得当时的Cloud Foundry只支持Node.js、Python、Java、PHP、Ruby on Rails等，脱离了这个范围则就无法支持，所以当时我其实对这种形态的应用场景存在很大的疑问。
这种困惑直到2013年Docker的出现而逐步解开，Docker的出现让开发语言、框架不再是问题，巧妙的解决了Cloud Foundry上述局限性。但是Docker毕竟只是一种工具形态，还不能称得上是平台，紧接着k8s的出现弥补了这一空白，使得Docker从游击队变成了正规军。
在这个发展过程中我们不难看出，软件领域发展出现了重大变革，从服务器为王逐渐演进到应用为王的阶段。如果说虚拟化改变了整个物理机的格局，那么无服务化的出现则改变了整个软件开发行业。
由于网上各种文档太多了，这里就不对Serverless基本概念进行介绍了，借用一张图说明下。另外还有一点，我们从这里面看到IT行业里的某些岗位，注定要消失的，比如传统运维。

![](/images/blogs/2019-12-19/compare.png)

## 3、应用架构

整个架构上，分为两个函数计算服务完成：

* 二维码前端：主要用于显示页面，并承担HTTP请求转发代理的角色，将请求转发至二维码后端，发给钉钉，采用HTTP触发器，允许公网访问。
* 二维码后端：用于将用户请求发送给钉钉，该部分服务仍然采用HTTP触发器，不同于前端，该服务是不允许公网直接访问的，但是需要配置NAT网关，通过网关访问钉钉，实现固定IP访问钉钉的效果。

![](/images/blogs/2019-12-19/new_architecture.png)

从逻辑上讲，整个应用并不复杂，但是在实际使用时遇到最大的问题来自钉钉白名单。由于函数服务对外连接的IP并不固定，所以无法在钉钉中添加，那么就要求函数服务对外连接的IP地址一定要固定。社区中提供的方法主要分为：
* ECI（运行Nginx充当Proxy），优势是便宜，劣势是高可用性需要自己维护
* NAT网关，优势是高可用性，劣势是比ECI贵

## 4、构建过程

由于篇幅原因，这里只介绍关键步骤。

### 4.1 构建模板

为了后续管理和扩展方便，选用了阿里云函数计算中使用flask-web模板进行构建，同时可以将前端静态文件模板存放于项目下（出于统一管理的需要，也可以存放于阿里云的OSS中，作为静态网站发布）。

前端我们使用flask-web作为模板创建函数，后端我们直接采用最简单的HTTP函数。

![](/images/blogs/2019-12-19/create_function_template.png)

函数入口配置，及触发器配置：

![](/images/blogs/2019-12-19/create_function.png)

服务配置，包含公网访问权限，专有网络配置，日志配置，权限配置。

* 前端服务需要公网访问权限，不需要专有网络配置，需要的权限为：AliyunLogFullAccess。
* 后端服务不需要公网访问权限，但是需要配置好的NAT映射的专有网络，由于函数服务在北京2区中在cn-beijing-c和cn-beijing-f，所以在新建交换机时需要使用这两个区。还需要选择安全组，由于出方向并没有明确禁止，所以不需要特别的安全组规则设定。需要的权限为：AliyunLogFullAccess/AliyunECSNetworkInterfaceManagementAccess。

配置好后，通过导出功能，分别下载前端和后端代码和配置，在本地进行开发调试。

![](/images/blogs/2019-12-19/export_function.png)

### 4.2 前端开发

我们的前端采用Vue.js进行开发，在main.py同级新建templates目录。Vue编译好的静态文件可以放入该目录中，后续Flask会加载该文件作为入口文件。

```
├── templates
│   ├── index.html
│   ├── static
├── main.py

```

```
## main.py sample
from flask import render_template

LICENSE_URL = "https://[x](https://.cn-beijing-internal.fc.aliyuncs.com/2016-08-15/proxy/QR_code/apply_license/license)x[x](https://xx.cn-beijing-internal.fc.aliyuncs.com/2016-08-15/proxy/QR_code/apply_license/license)x[x](https://xxxx.cn-beijing-internal.fc.aliyuncs.com/2016-08-15/proxy/QR_code/apply_license/license)x[x](https://xxxxxx.cn-beijing-internal.fc.aliyuncs.com/2016-08-15/proxy/QR_code/apply_license/license).cn-beijing-internal.fc.aliyuncs.com/2016-08-15/proxy/QR_code/apply_license/license"

@app.route('/qr_code', methods=['GET'])
def index():
      return render_template('index.html')

      @app.route('/qr_code/license', methods=['POST'])
      def create():
            payload = request.json
                resp = requests.post(LICENSE_URL,
                                                 json=payload,
                                                                              headers=DEFAULT_HEADERS)
                return make_response(resp.text, resp.status_code)
```

### 4.3 后端开发

后端的开发较为简单，实现一个函数支持POST请求，将转发的结果发送至钉钉即可。

### 4.4 本地调试
阿里云在本地开发时提供了fun应用部署和开发工具，详细使用方法见：[https://help.aliyun.com/document_detail/64204.html](https://help.aliyun.com/document_detail/64204.html)。

#### 安装fun

```
npm config set registry [https://registry.npm.taobao.org](https://registry.npm.taobao.org/) --global
npm config set disturl [https://npm.taobao.org/dist](https://npm.taobao.org/dist) --global

npm install @alicloud/fun -g
```

#### 配置fun

```
fun config

(venv) [root@ray-dev test_func]# fun config
? Aliyun Account ID xxxxxxxx
? Aliyun Access Key ID ***********r5Qd
? Aliyun Access Key Secret ***********kCCi
? Default region name cn-beijing
? The timeout in seconds for each SDK client invoking 10
? The maximum number of retries for each SDK client 3
? Allow to anonymously report usage statistics to improve the tool over time? Yes
```

#### Http Trigger本地运行

```
fun local start
```

#### 部署

```
fun deploy
```

### 4.5 配置域名解析

部署完成后有一点需要特别注意，必须要绑定域名，并且设定必要的路由。如果在没有绑定域名的情况下，服务端会为 response header中强制添加 content-disposition: attachment字段，此字段会使得返回结果在浏览器中以附件的方式打开。（[https://www.alibabacloud.com/help/zh/doc-detail/56103.htm](https://www.alibabacloud.com/help/zh/doc-detail/56103.htm)）

## 5、总结

* 灵活使用函数计算对开发成本和运行成本具有“双降”的效果
* 函数计算除了Http Trigger外，还包含了Event Trigger。Event Trigger中包含了连接各个服务之间的作用，在一些服务衔接上的作用越来越明显
* 函数计算在线开发时比较麻烦，并且查看日志不方便，所以尽量在本地开发好在上传的方式
