module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "19.21.0"

  cluster_name    = "ai-platform-cluster"
  cluster_version = "1.29"

  subnet_ids = [
    aws_subnet.private_subnet_1.id,
    aws_subnet.private_subnet_2.id
  ]

  vpc_id = aws_vpc.ai_vpc.id

  eks_managed_node_groups = {
    general = {
      instance_types = ["m6i.large"]
      desired_size   = 2
    }

    gpu_nodes = {
      instance_types = ["g5.xlarge"]
      desired_size   = 1
      taints = [{
        key    = "gpu"
        value  = "true"
        effect = "NO_SCHEDULE"
      }]
    }
  }
}
