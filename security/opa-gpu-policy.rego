package ai.platform

deny[msg] {
  input.request.kind.kind == "Deployment"
  not input.request.object.spec.template.spec.tolerations[_].key == "gpu"
  msg = "GPU workloads must declare gpu toleration"
}

deny[msg] {
  input.request.kind.kind == "Deployment"
  not input.request.object.spec.template.spec.containers[_].resources.limits["nvidia.com/gpu"]
  msg = "GPU limit must be explicitly defined"
}
