terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "ivytech-nexus-production"
  region  = "us-central1"
}

resource "google_container_cluster "swarm_cluster" {
  name     = "ivytech-professors-cluster"
  location = "us-central1-a"

  initial_node_count = 3

  node_config {
    machine_type = "a2-highgpu-1g" # NVIDIA A100 GPU node
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    guest_accelerator {
      type  = "nvidia-tesla-a100"
      count = 1
    }
  }
}
