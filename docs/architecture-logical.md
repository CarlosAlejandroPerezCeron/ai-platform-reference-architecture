# Logical Architecture

## Layers

1. Client Layer
   - API consumers
   - Model inference clients

2. Application Layer
   - Kubernetes workloads
   - GPU inference services

3. Infrastructure Layer
   - EKS cluster
   - Managed node groups (CPU + GPU)

4. Network Layer
   - Private VPC
   - Isolated subnets
   - No public worker exposure

5. Governance Layer
   - Cost modeling
   - Threat scoring
   - SLO monitoring

## Data Flow

Client → Load Balancer → Inference Service → GPU Node → Metrics Export → Financial Model
