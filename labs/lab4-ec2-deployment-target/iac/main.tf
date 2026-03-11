resource "aws_instance" "web_server" {
  ami           = var.ami_id
  instance_type = "t3.micro"
  tags = {
    Name        = "WebServer01"
    Environment = "Dev"
  }
}
