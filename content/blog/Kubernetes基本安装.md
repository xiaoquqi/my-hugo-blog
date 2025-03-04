---
title: Kubernetes All-in-One环境安装
author: 孙琦(Ray)
tags:
  - 常用命令
  - Kubernetes
  - K8S
  - Docker
categories: []
date: 2020-07-31 09:38:00
---
## Kubernetes安装及初始化

研发环境搭建Kubernetes All-in-One环境搭建。

<!-- more -->

### CentOS 7初始化

```
## Set SELinux in permissive mode (effectively disabling it)
setenforce 0
##sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
sed -i 's/^SELINUX=enforcing$/SELINUX=disabled/' /etc/selinux/config
 
systemctl stop NetworkManager
systemctl disable NetworkManager
 
systemctl status firewalld
systemctl stop firewalld
systemctl disable firewalld
systemctl status firewalld
firewall-cmd --state
 
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum clean all && yum makecache
yum update -y
```

### Docker国内源安装

```
## Install Docker
curl -sSL https://get.daocloud.io/docker | sh -s -- "--mirror" "Aliyun"
 
## Replace docker repo
mkdir -p /etc/docker
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": ["https://6m7d428u.mirror.aliyuncs.com"],
  "dns": ["114.114.114.114"],
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
EOF
 
systemctl enable docker && systemctl daemon-reload && systemctl restart docker
 
curl -L https://get.daocloud.io/docker/compose/releases/download/1.28.4/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

### 安装Kubernetes软件

```
## step1 Installation Process
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
exclude=kube*
EOF
 
yum install -y kubelet-1.18.0 kubeadm-1.18.0 kubectl-1.18.0 --disableexcludes=kubernetes
 
systemctl enable kubelet
 
## for CentOS 7
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
vm.swappiness=0
EOF
sysctl --system
 
## from k8s 1.8, swap need to be cloased, otherwise k8s could not be started
## swapoff -a
## Modify /etc/fstab, comment swap mount
```

### 初始化Kubernetes集群

```
## Step2 initialization
## Specify kubernetes-version if mirror do not contain latest kubernetes container. ex: if kubeadm is version 1.18.5, you can only
## install kubernetes = 1.18.x
kubeadm init --pod-network-cidr=10.244.0.0/16 --image-repository registry.aliyuncs.com/google_containers --kubernetes-version=1.18.0
 
## Response from output
## You should now deploy a pod network to the cluster.
## Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
##   https://kubernetes.io/docs/concepts/cluster-administration/addons/
## Then you can join any number of worker nodes by running the following on each as root:
## kubeadm join 192.168.10.111:6443 --token 1odaru.0by05advhbu7edgt \
##     --discovery-token-ca-cert-hash sha256:3efb71c40cce36c5ed90fc8b5831233aba06eec26576088e8e7a7a892d272776

 
## Step3 To use cluster
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
 
## Step4 flannel Network
sysctl net.bridge.bridge-nf-call-iptables=1
kubectl apply -f https://gitee.com/xiaoquqi/flannel/raw/master/Documentation/kube-flannel.yml

```

## 允许Master节点运行Pods

```
kubectl taint nodes --all node-role.kubernetes.io/master-
```

## 测试


### 安装Wordpress和MySQL

```
curl -LO https://raw.githubusercontent.com/xiaoquqi/k8s_demo/master/wordpress/mysql-deployment.yaml
curl -LO https://raw.githubusercontent.com/xiaoquqi/k8s_demo/master/wordpress/wordpress-deployment.yaml
curl -LO https://raw.githubusercontent.com/xiaoquqi/k8s_demo/master/wordpress/kustomization.yaml
```

### 执行安装

```
kubectl apply -k ./
```

### 验证

```
kubectl get secrets
kubectl get pvc
kubectl get pods
kubectl get services wordpress
```

### 资源清理

```
kubectl delete -k ./
```