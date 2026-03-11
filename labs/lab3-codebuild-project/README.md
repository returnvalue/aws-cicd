# Lab 3: Continuous Integration (AWS CodeBuild)

**Goal:** Create a CodeBuild project that pulls code from CodeCommit, looks for a `buildspec.yml` file, runs the build commands, and outputs the result.

```bash
# Create the CodeBuild project
awslocal codebuild create-project \
  --name 'WebAppBuild' \
  --source 'type=CODECOMMIT,location=https://git-codecommit.us-east-1.amazonaws.com/v1/repos/portfolio-web-app' \
  --artifacts 'type=NO_ARTIFACTS' \
  --environment 'type=LINUX_CONTAINER,image=aws/codebuild/amazonlinux2-x86_64-standard:3.0,computeType=BUILD_GENERAL1_SMALL' \
  --service-role $BUILD_ROLE
```

## 🧠 Key Concepts & Importance

- **Continuous Integration (CI):** A DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.
- **AWS CodeBuild:** A fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.
- **Buildspec File:** A collection of build commands and related settings, in YAML format, that CodeBuild uses to run a build. It defines the phases of the build (e.g., `install`, `pre_build`, `build`, `post_build`).
- **Build Environment:** The operating system, programming language runtime, and tools that CodeBuild uses to run a build. These are typically managed via Docker images.
- **Compute Type:** Specifies the CPU and memory for the build environment (e.g., `BUILD_GENERAL1_SMALL`).

## 🛠️ Command Reference

- `codebuild create-project`: Provisions a new build project.
    - `--name`: The name of the build project.
    - `--source`: Specifies the repository type and location.
    - `--artifacts`: Defines where the build output is sent (set to `NO_ARTIFACTS` here as CodePipeline will handle this later).
    - `--environment`: Defines the build container, image, and compute resources.
    - `--service-role`: The IAM role ARN that CodeBuild assumes to access AWS resources.
