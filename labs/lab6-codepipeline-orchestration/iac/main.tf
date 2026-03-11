resource "aws_codepipeline" "main" {
  name     = "WebApp-CI-CD-Pipeline"
  role_arn = var.pipeline_role_arn

  artifact_store {
    location = var.artifact_bucket
    type     = "S3"
  }

  stage {
    name = "Source"
    action {
      name             = "SourceAction"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeCommit"
      version          = "1"
      output_artifacts = ["SourceArtifact"]
      configuration    = { RepositoryName = "portfolio-web-app", BranchName = "main" }
    }
  }

  stage {
    name = "Build"
    action {
      name             = "BuildAction"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = "1"
      input_artifacts  = ["SourceArtifact"]
      output_artifacts = ["BuildArtifact"]
      configuration    = { ProjectName = "WebAppBuild" }
    }
  }

  stage {
    name = "Deploy"
    action {
      name            = "DeployAction"
      category        = "Deploy"
      owner           = "AWS"
      provider        = "CodeDeploy"
      version         = "1"
      input_artifacts = ["BuildArtifact"]
      configuration   = { ApplicationName = "WebAppDeploy", DeploymentGroupName = "DevDeploymentGroup" }
    }
  }
}
