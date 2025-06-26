resource "aws_ecr_repository" "my_app" {
  name                 = var.app_name
  image_tag_mutability = "MUTABLE"
  force_delete         = true
}