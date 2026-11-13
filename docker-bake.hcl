variable "IMAGE" {
  default = "ghcr.io/anthonybnl/tp_dataops_1"
}

variable "TAG" { default = "latest" }

target "docker-metadata-action" {
  tags = ["${IMAGE}:${TAG}"]
}

group "default" {
  targets = ["app"]
}

target "app" {
  inherits   = ["docker-metadata-action"]
  context    = "."
  dockerfile = "Dockerfile"
  cache-from = ["type=registry,ref=${IMAGE}:buildcache"]
  cache-to   = ["type=registry,ref=${IMAGE}:buildcache,mode=max"]
}
