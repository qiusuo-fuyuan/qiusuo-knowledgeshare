This tutorial contains the analysis of how K8 Pod, Services, Deployments work
on local system. The goal is able to access cluster via Cluster-IP from host



First define deployments. We have created one deployment
https://app.gitbook.com/@qsol-work/s/team-knowledge/~/drafts/-MbG1uav_iX-qIOKCd1U/qiu-suo-gou-jia-da-jian-xiang-jie-xi-lie/chapter-three-kubernetes-deployments/k8s/run-flask-demo-on-docker-and-minikube

docker exect -it minikube-docker-container


API Server is running on the master node of cluster
####get API-Server Kube#####

root@minikube:/# docker ps | grep kube-apiserver
f7effb9eb8ba   ca9843d3b545           "kube-apiserver --ad…"   7 hours ago   Up 7 hours             k8s_kube-apiserver_kube-apiserver-minikube_kube-system_524cecac593a7ad14f29307cb61f56b8_5


By default, there is one Cluster, this Cluster uses the Minikube as the node. In one node, there can be multiple pods running.

