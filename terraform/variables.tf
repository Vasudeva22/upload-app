variable "app_name" {
  default = "my-app"
}

variable "aws_region" {
  default = "us-east-1"
}

variable "image_tag" {
  description = "Docker image tag to deploy"
  type        = string
  default     = "latest"
}
