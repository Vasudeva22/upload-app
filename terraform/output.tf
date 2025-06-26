output "ecr_repo_url" {
  value = aws_ecr_repository.my_app.repository_url
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main.name
}

output "ecs_service_name" {
  value = aws_ecs_service.app.name
} 