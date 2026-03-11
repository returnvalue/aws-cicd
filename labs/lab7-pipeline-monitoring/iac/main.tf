resource "aws_cloudwatch_event_rule" "pipeline_state" {
  name        = "WebAppPipelineMonitoring"
  description = "Monitor state changes for the CI/CD pipeline"
  event_pattern = jsonencode({
    source      = ["aws.codepipeline"]
    detail-type = ["CodePipeline Pipeline Execution State Change"]
    detail = {
      pipeline = ["WebApp-CI-CD-Pipeline"]
    }
  })
}
