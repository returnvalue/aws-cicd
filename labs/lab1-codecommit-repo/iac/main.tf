resource "aws_codecommit_repository" "web_app" {
  repository_name = "portfolio-web-app"
  description     = "Main repository for the web application"
}
