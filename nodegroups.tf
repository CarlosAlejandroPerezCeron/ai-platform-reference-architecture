resource "aws_eks_node_group" "gpu_nodes" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "gpu-node-group"
  node_role_arn   = aws_iam_role.eks_role.arn
  subnet_ids      = [aws_subnet.private_a.id]

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  instance_types = [var.gpu_instance_type]
}

resource "aws_eks_node_group" "cpu_nodes" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "cpu-node-group"
  node_role_arn   = aws_iam_role.eks_role.arn
  subnet_ids      = [aws_subnet.private_a.id]

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  instance_types = [var.cpu_instance_type]
}
