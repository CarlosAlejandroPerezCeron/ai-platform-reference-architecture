resource "aws_eks_cluster" "main" {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = [
      aws_subnet.private_a.id
    ]
    endpoint_private_access = true
    endpoint_public_access  = false
  }
}
