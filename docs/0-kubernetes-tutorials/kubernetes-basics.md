# kubernetes-basics

![](https://www.shapeblue.com/wp-content/uploads/2020/12/Kubernetes-logo.png)
## Introduction 

[Kubernetes](https://kubernetes.io/) (K8s in short) is an open-source container orchestration platform introduced by Google in 2014. The platform’s main purpose is to automate deployment and management (e.g., update, scaling, security, networking, auto-repair) of containerized application in large distributed computer clusters. To this end, the platform offers a number of API primitives, deployment options, networking, container and storage interfaces, built-in security, and other useful features. 


## High Level Concepts 

### [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) 

Pods are the smallest unit in kubernetes. Pods represent containers that are actually running.

### [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) 

A collection of pods represent a node. Nodes are often a physical machine that are actually running the pods. 

### [Clusters](https://kubernetes.io/docs/concepts/cluster-administration/)

A collection of nodes represent a cluster. Clusters are by geographic region, which is where all the compute resources are hosted in the cloud. 

![](https://miro.medium.com/max/1256/1*gT5K52iFTJf6SDhwWBaClQ.png)
### Notes 

Often when working with kubernetes one does not really create the individual pods and by defauly they don't really have an external IP. As a devops engineer, one would define number of pods required and then for the node have a load balancer than balances traffic between the pods and the load balancer creates a static IP that one uses to access the service. 

## Key Benefits

### Focus on Configuration 

The main benefit of kubernetes is that it allows you to use a yaml file to define the desired state of the application and kubernetes as a system and engine will make sure that that state is always ensured. This allows for less work and hassle for devops engineers is as self managed as possible. As part of configuration, one can define how many replica of pods one wants, these could be defined as minimum and maximum or an exact number. Further, one can define compute resources to be dedicated to the pod creation, exact memory and CPU allocation can be specified for the pods. One can be conservative in terms of resource allocation to save on costs, it all depends on how one defines the system requirements to kubernetes. 

### Auto Repair 

Auto repair is a key feature in kubernetes. For example, if we want 2 pods always running on the minimum for an application and all of a sudden one pod goes down due to high memory usage/CPU usage, kubernetes will either restart or recreate the pod which will be specifically useful. This goes back to show how devops engineers need to focus on config and kubernetes will take care of the rest. 

### Auto Scaling 

Kuberenetes is also really good for scaling and especially autoscaling. It can scale from 3 requests per second to 3 million requests per second very easily. It has autoscaling features that can be enabled from one command. For the use case of CYE, this might be useful if there is unexpected traffic, it can scale and create additional pods or even nodes if required. 


