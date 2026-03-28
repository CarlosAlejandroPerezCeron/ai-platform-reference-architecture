module "network" {
  source = "./modules/network"
}

module "eks" {
  source = "./modules/eks"
}
