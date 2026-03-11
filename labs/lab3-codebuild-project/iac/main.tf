resource "aws_codebuild_project" "web_app" {
  name          = "WebAppBuild"
  service_role  = var.build_role_arn
  build_timeout = 5

  artifacts { type = "NO_ARTIFACTS" }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/amazonlinux2-x86_64-standard:3.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"
  }

  source {
    type     = "CODECOMMIT"
    location = "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/portfolio-web-app"
  }
}
