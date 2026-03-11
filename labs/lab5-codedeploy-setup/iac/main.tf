resource "aws_codedeploy_app" "web_app" {
  name             = "WebAppDeploy"
  compute_platform = "Server"
}

resource "aws_codedeploy_deployment_group" "dev" {
  app_name              = aws_codedeploy_app.web_app.name
  deployment_group_name = "DevDeploymentGroup"
  service_role_arn      = var.deploy_role_arn
  deployment_config_name = "CodeDeployDefault.OneAtATime"

  ec2_tag_filter {
    key   = "Environment"
    type  = "KEY_AND_VALUE"
    value = "Dev"
  }
}
