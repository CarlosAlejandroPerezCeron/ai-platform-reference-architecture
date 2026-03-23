# Physical Architecture

AWS Region: us-east-1

Components:

- VPC (10.0.0.0/16)
- Private Subnets (multi-AZ)
- EKS cluster (private endpoint)
- Node Groups:
  - m6i.large (general workloads)
  - g5.xlarge (GPU workloads)

Observability:

- Prometheus
- Grafana dashboards

Security:

- IAM Roles for Service Accounts
- Security Groups restricted
